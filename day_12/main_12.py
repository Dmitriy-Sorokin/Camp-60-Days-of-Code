user_input = input("Enter feet and inches: ")

list_user = user_input.split()


def converter(user_inp1, user_inp2):
    return user_inp1 * 0.3048 + user_inp2 * 0.0254


print(converter(float(list_user[0]), float(list_user[1])))
