def get_user_input():
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
