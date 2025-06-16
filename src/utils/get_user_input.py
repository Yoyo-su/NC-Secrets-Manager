def get_user_input():
    """This function captures user input for the password manager commands.
    Only specific inputs are accepted and returned in lowercase.

    Returns:
        string: The user input for the password manager command

    Raises:
        ValueError: If the user input is not one of the acceptable inputs
        KeyError: If the user input is not a recognized command
    """
    try:
        user_input = input()
        acceptable_inputs = ["e", "r", "d", "l", "x", "E", "R", "D", "L", "X"]
        if user_input in acceptable_inputs:
            return user_input.lower()
        else:
            raise (ValueError)
    except (ValueError, KeyError) as error:
        print(
            "Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:"
        )
        return 0
