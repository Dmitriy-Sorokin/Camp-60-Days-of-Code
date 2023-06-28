
while True:
    user_chose = input("Head ro tail here?: ")

    with open("head_or_tail.txt", "a") as file:
        file.write(f"{user_chose}\n")

    with open("head_or_tail.txt", "r") as f:
        a = [item.strip("\n") for item in f.readlines()]
        len_list = len(a)
        b = a.count("head")
        final_pro = (b / len_list) * 100
        print(f"Heads {final_pro}%")
