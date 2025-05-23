from time import sleep
def check_exit(user_input):
    if user_input == "x":
        print("Thank you. Goodbye.")
        sleep(2)
        return True
    return False
