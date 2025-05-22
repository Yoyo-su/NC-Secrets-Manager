# Password Manager

The application will use a python script (password_manager.py) to call on a class object with the following layout:

    class PasswordManager

        def Entry - store a user ID and password as a secret in secretsmanager
        
        def Retrieval - retrieve a secret - the resulting user ID and password will be stored in a .txt file (not printed).
        
        def Deletion - delete a secret from secretsmanager
        
        def Listing - list all the stored secrets
        
        def Exit - Exit the application if 'x' pressed


The script will get the users inputs utilising a function

    def get_user_input - captures a valid user input and raises errors for invalid inputs

Each function will be tested individually using TDD.
        
    
    
    