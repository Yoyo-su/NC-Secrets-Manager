def delete_secret(client, secret_id):
    try:
        client.delete_secret(SecretId=secret_id, ForceDeleteWithoutRecovery=True)
        print("Secret deleted.")
    except Exception as error:
        print(f"Failed to delete secret: {error}")
        raise Exception
