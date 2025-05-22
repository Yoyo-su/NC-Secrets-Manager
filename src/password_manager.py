from utils.get_user_input import get_user_input
from utils.add_secret import add_secret
from utils.exit import check_exit
import boto3

"""Initialise values"""
user_input = 0
Check_Exit = False
secrets_client = boto3.client('secretsmanager')
"""Begin application loop - Checks exit command on each iteration"""
while not Check_Exit:
    Check_Exit = check_exit(user_input)
    if Check_Exit:
        exit()
    
    """Capture initial user input"""
    print("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:")
    while user_input == 0:
        user_input = get_user_input()

    if user_input == 'e':
        user_input = 0
        secret_name = input("Secret identifier: ")
        username = input("UserId:   ")
        password = input("Password: ")
        add_secret(secrets_client, secret_name, username, password)