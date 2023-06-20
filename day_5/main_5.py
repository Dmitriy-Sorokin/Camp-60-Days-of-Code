countries = ['a', "b", "v",]

while True:
    user_choice = input("Add or show or exit or edit: ")
    user_choice = user_choice.strip()
    match user_choice:
        case "show":
            for index, i in enumerate(countries):
                print(f"{index}-{i}")
        case "add":
            add_countries = input("add country: ")
            countries.append(add_countries)
        case "edit":
            number_country = input("Type number country: ")
            countries[int(number_country) - 1] = input("add country")
        case "exit":
            break

# waiting_list = ["sen", "ben", "john"]
# a = sorted(waiting_list)
# for index, item in enumerate(a):
#     print(f"{index+1}.{item.capitalize()}")

