from utils.get_user_input import get_user_input
from utils.exit import check_exit

"""Initialise values"""
user_input = 0
Check_Exit = False

"""Begin application loop - Checks exit command on each iteration"""
while not Check_Exit:
    Check_Exit = check_exit(user_input)
    if Check_Exit:
        exit()
    
    """Capture initial user input"""
    print("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:")
    while user_input == 0:
        user_input = get_user_input()

