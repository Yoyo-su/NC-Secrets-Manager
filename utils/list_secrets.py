def list_secrets(client):
    """This function retrieves and lists all secrets currently stored in the AWS Secrets Manager.
    It prints the number of secrets available and their names(ID).

    Args:
        client (boto3): The boto3 client for AWS Secrets Manager

    Raises:
        Exception: If there is an error retrieving the secrets from the secrets manager

    Returns:
        list: list of secrets available in the AWS Secrets Manager
    """
    try:
        secret_list = client.list_secrets()["SecretList"]
        secret_count = len(secret_list)
        print(f"{secret_count} secret(s) available")
        for secret in secret_list:
            print(secret["Name"])
        return secret_list
    except Exception as error:
        print(f"Failed to list secrets: {error}")
        raise error
