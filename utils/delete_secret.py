def delete_secret(client, secret_id):
    """This function removes an existing secret with the given secret_id from the AWS secrets manager.

    Args:
        client (boto3): The boto3 client for AWS Secrets Manager
        secret_id (string): The ID associated with the secret to be deleted
    Raises:
        Exception: If there is an error removing the secret to the secrets manager
    """
    try:
        client.delete_secret(SecretId=secret_id, ForceDeleteWithoutRecovery=True)
        print("Secret deleted.")
    except Exception as error:
        print(f"Failed to delete secret: {error}")
        raise Exception
