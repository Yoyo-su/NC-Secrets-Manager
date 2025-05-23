# Password Manager

The application will use a python script (password_manager.py) to call on a class object with the following layout:

    class PasswordManager

        def add_secret - store a user ID and password as a secret in secretsmanager
        
        def fetch_secret - retrieve a secret - the resulting user ID and password will be stored in a .txt file (not printed). This file is saved in the secrets folder (gitignored)
        
        def delete_secret - delete a secret from secretsmanager
        
        def list_secrets - list all the stored secrets
        
        def check_exit - Allows the application to be exited if 'x' pressed


The script will get the users inputs utilising a function

    def get_user_input - captures a valid user input and raises errors for invalid inputs

Each function will be tested individually using TDD.
        
    
    
    