user_password = input("Type pass: ")

if len(user_password) >= 8 and any(char.isdigit() for char in user_password) and\
        any(char.isupper() for char in user_password):
    print("Strong password")
else:
    print("Eazy password")
