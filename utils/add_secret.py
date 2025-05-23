def add_secret(client, secret_name, username, password):
    try:
        secret_string = str({"username": username, "password": password})
        client.create_secret(
            Name=secret_name,
            SecretString=secret_string,
        )
        print("Secret saved.")
    except Exception as error:
        print(f"Failed to add_secret: {error}")
        raise error
