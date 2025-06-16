import pytest
import os
import sys
import boto3
from moto import mock_aws
from unittest.mock import patch
from src.utils.get_user_input import get_user_input
from src.utils.add_secret import add_secret
from src.utils.fetch_secret import fetch_secret
from src.utils.list_secrets import list_secrets
from src.utils.exit import check_exit
from src.utils.delete_secret import delete_secret
from botocore.exceptions import ClientError

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../secrets"))
)

"""Test suite for the password manager application.
This suite tests the functionality of adding, fetching, deleting, and listing secrets,
as well as checking for exit commands.
"""


@pytest.fixture
def aws_creds():
    os.environ["AWS_ACCESS_KEY_ID"] = "Test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "Test"
    os.environ["AWS_SESSION_TOKEN"] = "Test"
    os.environ["AWS_SECURITY_TOKEN"] = "Test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture
def secrets_client(aws_creds):
    with mock_aws():
        secrets_client = boto3.client("secretsmanager")
        yield secrets_client


class TestGetUserInput:
    @pytest.mark.it("should accept valid inputs of 'e', 'r', 'd', 'l' and 'x'")
    @patch("src.utils.get_user_input.input")
    def test_get_user_input_returns_valid_inputs(self, mock_input):
        mock_input.return_value = "e"
        assert get_user_input() == "e"
        mock_input.return_value = "r"
        assert get_user_input() == "r"
        mock_input.return_value = "d"
        assert get_user_input() == "d"
        mock_input.return_value = "l"
        assert get_user_input() == "l"
        mock_input.return_value = "x"
        assert get_user_input() == "x"

    @patch("src.utils.get_user_input.input")
    @pytest.mark.it("should return valid letters in lowercase")
    def test_get_user_input_returns_valid_capitals_in_lower_case(self, mock_input):
        mock_input.return_value = "E"
        assert get_user_input() == "e"

    @patch("src.utils.get_user_input.input")
    @pytest.mark.it("should return zero if input invalid")
    def test_get_user_input_return_zero_for_invalid_input(self, mock_input):
        mock_input.return_value = "p"
        assert get_user_input() == 0
        mock_input.return_value = "3"
        assert get_user_input() == 0
        mock_input.return_value = "?"
        assert get_user_input() == 0


class TestAddSecret:
    @pytest.mark.it("should add a secret to the secrets manager")
    def test_add_secret_stores_secret_in_secret_manager(self, secrets_client):
        test_secret = "testsecret"
        test_username = "testusername"
        test_password = "testpassword"
        add_secret(secrets_client, test_secret, test_username, test_password)
        secret_list = secrets_client.list_secrets()["SecretList"]
        assert len(secret_list) == 1
        assert test_secret == secret_list[0]["Name"]

    @pytest.mark.it("should add multiple secrets to the secrets manager")
    def test_add_secret_stores_many_secrets_in_secret_manager(self, secrets_client):
        test_secret = "testsecret"
        test_username = "testusername"
        test_password = "testpassword"
        add_secret(secrets_client, test_secret, test_username, test_password)
        test_secret = "testsecret2"
        add_secret(secrets_client, test_secret, test_username, test_password)
        secret_list = secrets_client.list_secrets()["SecretList"]
        assert len(secret_list) == 2

    @pytest.mark.it("returns an error messsage if fails to add secret")
    def test_add_secret_returns_error_if_secret_not_added(self, secrets_client):
        test_secret = "testsecret"
        test_username = "testusername"
        test_password = "testpassword"
        add_secret(secrets_client, test_secret, test_username, test_password)
        with pytest.raises(Exception):
            add_secret(secrets_client, test_secret, test_username, test_password)


class TestFetchSecrets:
    @pytest.mark.it("should retrieve a secret and save it locally")
    def test_fetch_secret_saves_secret(self, secrets_client):
        test_secret = "testsecret"
        test_username = "testusername"
        test_password = "testpassword"
        add_secret(secrets_client, test_secret, test_username, test_password)
        fetch_secret(secrets_client, test_secret)
        with open(f"secrets/{test_secret}.txt", "r", encoding="utf-8") as file:
            secret = file.read()
            assert secret == "{'username': 'testusername', 'password': 'testpassword'}"

    @pytest.mark.it("should raise error if secret doesn't exist")
    def test_fetch_secret_rasies_error_if_no_secrets(self, secrets_client):
        test_secret = "testsecret"
        with pytest.raises(Exception):
            fetch_secret(secrets_client, test_secret)


class TestListSecrets:
    @pytest.mark.it("should return empty list if no secrets")
    def test_list_secrets_return_empty_list(self, secrets_client):
        secret_list = list_secrets(secrets_client)
        assert isinstance(secret_list, list)
        assert len(secret_list) == 0

    @pytest.mark.it("should return a list containing a secret")
    def test_add_secret_stores_a_secret_in_secret_manager(self, secrets_client):
        test_secret = "testsecret"
        test_username = "testusername"
        test_password = "testpassword"
        add_secret(secrets_client, test_secret, test_username, test_password)
        secret_list = list_secrets(secrets_client)
        assert len(secret_list) == 1
        assert test_secret == secret_list[0]["Name"]
        assert isinstance(secret_list, list)

    @pytest.mark.it("should return a list containing secrets")
    def test_add_secret_stores_many_secrets_in_secret_manager(self, secrets_client):
        test_secret1 = "testsecret"
        test_secret2 = "testsecret2"
        test_username = "testusername"
        test_password = "testpassword"
        add_secret(secrets_client, test_secret1, test_username, test_password)
        test_secret = "testsecret2"
        add_secret(secrets_client, test_secret2, test_username, test_password)
        secret_list = list_secrets(secrets_client)
        assert len(secret_list) == 2
        assert test_secret1 == secret_list[0]["Name"]
        assert test_secret2 == secret_list[1]["Name"]
        assert isinstance(secret_list, list)

    @pytest.mark.it("should raise error if client doesn't exist")
    def test_list_secrets_raises_error_if_no_client(self, secrets_client):
        secrets_client = "bad_client"
        test_secret = "testsecret"
        with pytest.raises(Exception):
            fetch_secret(secrets_client, test_secret)


class TestExit:
    @pytest.mark.it("should return false if user input is not 'x'")
    def test_exit_returns_false_if_input_not_x(self):
        test_input = "l"
        assert check_exit(test_input) is False

    @pytest.mark.it("should return true if user input is 'x'")
    def test_exit_returns_true_if_input_is_x(self):
        test_input = "x"
        assert check_exit(test_input) is True


class TestDelete:
    @pytest.mark.it("should delete the secret with  geven ecret")
    def test_delete_secret_with_secret_id(self, secrets_client):
        test_secret1 = "testsecret"
        test_username = "testusername"
        test_password = "testpassword"
        add_secret(secrets_client, test_secret1, test_username, test_password)
        secret_list = list_secrets(secrets_client)
        assert len(secret_list) == 1
        delete_secret(secrets_client, test_secret1)
        secret_list = list_secrets(secrets_client)
        assert len(secret_list) == 0

    @pytest.mark.it("should raise error if secret doesn't exist")
    def test_delete_secret_rasies_error_if_no_secrets(self, secrets_client):
        test_secret = "dummysecret"
        secret_list = list_secrets(secrets_client)
        assert len(secret_list) == 0

        error_response = {"Error": {"Code": "Exception"}}

        with patch.object(
            secrets_client,
            "delete_secret",
            side_effect=ClientError(error_response, "DeleteSecret"),
        ):
            with pytest.raises(Exception):
                delete_secret(secrets_client, test_secret)
