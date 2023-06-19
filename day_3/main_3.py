countries = ['a', "b", "v",]

while True:
    user_choice = input("Add or show or exit or edit: ")
    user_choice = user_choice.strip()
    match user_choice:
        case "show":
            b = ""
            for i in countries:
                b += f" {i}"
            print(b)
        case "add":
            add_countries = input("add country: ")
            countries.append(add_countries)
        case "edit":
            number_country = input("Type number country: ")
            countries[int(number_country) - 1] = input("add country")
        case "exit":
            break

# members = ["john smith", "sen plakay", "dora ngacely"]
# for item in members:
#     words = item.split()
#     a = [i.capitalize() for i in words]
#     my_str = " ".join(a)
#     print(my_str)
#
# for item in ["sandals", "glasses", "trousers"]:
#     print(item.capitalize())
