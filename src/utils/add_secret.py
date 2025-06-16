def add_secret(client, secret_id, username, password):
    """This function adds a new secret to the AWS secrets manager.
    It takes the secret name(id), username, and password as parameters and stores them.

    Args:
        client (boto3): The boto3 client for AWS Secrets Manager
        secret_id (string): The name(ID) of the secret to be added
        username (string):  The username associated with the secret
        password (string): The password associated with the secret

    Raises:
        Exception: If there is an error adding the secret to the secrets manager
    """
    try:
        secret_string = str({"username": username, "password": password})
        client.create_secret(
            Name=secret_id,
            SecretString=secret_string,
        )
        print("Secret saved.")
    except Exception as error:
        print(f"Failed to add_secret: {error}")
        raise error
