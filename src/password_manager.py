from utils.get_user_input import get_user_input
from utils.add_secret import add_secret
from utils.fetch_secret import fetch_secret
from utils.list_secrets import list_secrets
from utils.exit import check_exit
from utils.delete_secret import delete_secret
import boto3


"""This script is a simple password manager that interacts with AWS Secrets Manager.
It takes user inputs to add, retrieve, delete, and list secrets securely.
"""


def run_your_password_manager():
    """Initialise values"""
    user_input = 0
    Check_Exit = False
    secrets_client = boto3.client("secretsmanager")

    """Begin application loop - Checks exit command on each iteration"""
    while not Check_Exit:
        try:
            Check_Exit = check_exit(user_input)
            if Check_Exit:
                exit()

            """Capture initial user input"""
            print(
                "Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:"
            )
            while user_input == 0:
                user_input = get_user_input()

            """If user input is 'e', prompts for secret to add"""
            if user_input == "e":
                user_input = 0
                print("Secret identifier:")
                secret_name = input()
                print("UserId:")
                username = input()
                print("Password:")
                password = input()
                add_secret(secrets_client, secret_name, username, password)

            """If user input is 'r', prompts for secret to fetch"""
            if user_input == "r":
                user_input = 0
                print("Specify secret to retrieve:")
                secret_id = input()
                fetch_secret(secrets_client, secret_id)

            """If user input is 'd', prompts for secret to delete"""
            if user_input == "d":
                user_input = 0
                print("Specify secret to delete:")
                secret_id = input()
                delete_secret(secrets_client, secret_id)

            """If user input is 'l', lists all secrets in the secrets manager"""
            if user_input == "l":
                user_input = 0
                list_secrets(secrets_client)
        except Exception as error:
            continue


"""Run the password manager"""
if __name__ == "__main__":
    run_your_password_manager()
