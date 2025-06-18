# Password Manager

## 🤝 Pair Programmed by 

<table>
  <tr>
    <td><strong>Iohane</strong><br>
      <a href="https://github.com/Yoyo-su">
        <img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white" />
      </a><br>
      <a href="https://www.linkedin.com/in/iohane-annan-07b722a0/">
        <img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white" />
      </a>
    </td>
    <td><strong>Fidele</strong><br>
      <a href="https://github.com/fmunyaneza">
        <img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white" />
      </a><br>
      <a href="https://www.linkedin.com/in/fidele-munyaneza-b87372328/">
        <img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white" />
      </a>
    </td>
  </tr>
</table>

## 🔰 Overview
A simple password manager that allows users to securely store and manage their passwords using AWS Secrets Manager. This application provides functionalities to add, fetch, delete, and list secrets, ensuring that sensitive information is handled securely and efficiently.

Upon running the application the user is prompted to choose from the following options:
- **\[e]ntry**: Store a username and password as a secret in AWS Secrets Manager
- **\[r]etrieval**: Retrieve a secret and save the username and password to a `.txt` file in the `secrets` folder
- **\[d]eletion**: Remove a secret from AWS Secrets Manager
- **\[l]isting**: Display all stored secrets
- **E\[x]it**: Exit the application


## 🔧 Tech Stack
- **Python 3.13** - Primary programming language
  - **Pytest** - Test Driven Development (TDD)
- **Github** - Repository management, CI/CD (Github-Actions)
- **AWS** - Secrets Manager


## 🏛️ Architecture
# Password Manager

The application uses a python script (password_manager.py) to call on a class object with the following structure:

    class PasswordManager

        def add_secret - store a user ID and password as a secret in secretsmanager
        
        def fetch_secret - retrieve a secret - the resulting user ID and password will be stored in a .txt file (not printed). This file is saved in the secrets folder (gitignored)
        
        def delete_secret - delete a secret from secretsmanager
        
        def list_secrets - list all the stored secrets
        
        def check_exit - Allows the application to be exited if 'x' pressed


The script will get the users inputs utilising a function

    def get_user_input - captures a valid user input and raises errors for invalid inputs

Each function is tested individually using TDD in the test/test_password_manager.py file.


## 📁 File Structure

```
NC-PASSWORD-MANAGER
├── .github
│   └── workflows
│       └── PM_deployment.yml       # CI/CD Automated deployment via Github Actions
├── secrets/                        # Downloaded secrets from AWS Secrets Manager
├── src
│   ├── utils/                      # Utility functions for the password manager                           
│   └── password_manager.py         # Main application file for the password manager
├── tests/                          
│   └── test_password_manager.py    # Unit and integration tests for python functions (pytest)
├── .gitignore                      # Files not to be pushed to remote repository
├── Makefile                        # Automated environment setup & configuration
├── README.md                       # Project overview
├── PLAN.md                         # Project plan and requirements
└── requirements.txt                # Third party Python modules
```

## 🚀 Setup & Deployment

This project uses GitHub Actions for continuous integration and deployment, the workflow automatically runs tests and checks.

The CI/CD pipeline is triggered on:
  - Pushes to the main branch

### Continuous Integration  
The run-tests job performs the following steps:

 - Configures the Python environment and installs dependancies
 - Runs python security, format and linting checks
 - Runs pytests and checks test coverage

### Local Setup
To run locally, you can use the provided Makefile to set up the environment and run tests, please follow these steps:

1. Ensure you have Python 3.13 installed on your machine.

2. Clone the repository to your local machine:
    ```bash
        git clone https://github.com/Yoyo-su/NC-Secrets-Manager.git
    ```

3. Navigate to the project directory:
    ```bash
        cd NC-Secrets-Manager
    ```

4. Setup the local virtual environment by running the following commands:
    ```bash
    make setup
    ```

5. To run the tests, use:
    ```bash
    make run-checks
    ```

6. Ensure you have the necessary AWS credentials configured in your environment. You can set them up using the AWS CLI:
    ```bash
    aws configure
    ```

7. To run the application, use:
    ```bash
    python src/password_manager.py
    ```


##
*A Northcoders Data Engineering Bootcamp Project*
