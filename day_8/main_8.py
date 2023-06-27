user_data = input("Enter today's date: ")

mood = input("How do you rate your mood 1 to 10?: ")

with open(f"{user_data}.txt", "w") as file:
    file.write(f"Your day have {mood} point")

with open(f"{user_data}.txt", "r") as file:
    print(file.read())