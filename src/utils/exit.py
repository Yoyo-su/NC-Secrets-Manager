from time import sleep


def check_exit(user_input):
    """This function checks if the user input is 'x' or 'X' to exit the program.

    Args:
        user_input (string): The user input to check if it is an exit command

    Returns:
        Bool: True if user input is 'x' or 'X', False otherwise
    """
    if user_input == "x":
        print("Thank you. Goodbye.")
        sleep(2)
        return True
    return False
