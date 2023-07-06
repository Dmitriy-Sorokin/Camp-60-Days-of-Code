# user_input = input("Enter feet and inches: ")
#
# list_user = user_input.split()
#
#
# def converter(user_inp1, user_inp2):
#     return user_inp1 * 0.3048 + user_inp2 * 0.0254
#
#
# print(converter(float(list_user[0]), float(list_user[1])))

# def check_password(user_pass):
#     if len(user_pass) >= 8 and any(char.isdigit() for char in user_pass) and \
#             any(char.isupper() for char in user_pass):
#         return "Strong password"
#     else:
#         return "Eazy password"
#
# print(check_password("asfasf8S"))

# def checker(list_user: list):
#     final = sum(list_user) / len(list_user)
#     return final


def input_string(name: str):
    return name.title()

print(input_string("jo"))
