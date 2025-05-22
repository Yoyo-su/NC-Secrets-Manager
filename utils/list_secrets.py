def list_secrets(client):
    secret_list = client.list_secrets()['SecretList']
    secret_count = len(secret_list)
    print(f'{secret_count} secret(s) available')
    for secret in secret_list:
        print(secret['Name'])
    return secret_list