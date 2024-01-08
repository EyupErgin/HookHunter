def get_user_input():
    while True:
        user_input = input("[INFO] Please enter domain: ")
        print(" ")
        if user_input.strip():
            return user_input.strip()