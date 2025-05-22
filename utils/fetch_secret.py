def fetch_secret(client, secret_name):
    try:
        response = client.get_secret_value(SecretId=secret_name)
        with open(f'{secret_name}.txt', 'w', encoding='utf-8') as file:
            file.write(response['SecretString'])
        print("Secret saved.")
    except Exception as error:
        print(f'Failed to retrieve secret: {error}')
        raise error