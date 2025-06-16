def fetch_secret(client, secret_id):
    """This function retrieves a secret with the given secret_id from the AWS Secrets Manager.
    It saves the secret to a file in the 'secrets' directory with the secret_id as the filename.

    Args:
        client (boto3): The boto3 client for AWS Secrets Manager
        secret_id (string): The ID of the secret to be fetched

    Raises:
        Exception: If there is an error retrieving the secret to the secrets manager
    """
    try:
        response = client.get_secret_value(SecretId=secret_id)
        with open(f"../secrets/{secret_id}.txt", "w", encoding="utf-8") as file:
            file.write(response["SecretString"])
        print("Secret saved.")
    except Exception as error:
        print(f"Failed to retrieve secret: {error}")
        raise error
