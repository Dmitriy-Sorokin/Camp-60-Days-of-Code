while True:
    list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    try:
        foundation = input("Type foundation: ")
        height = input("Type height ")

        s = 0.5 * int(foundation) * int(height)
        print(s)
        break
    except ValueError:
        print("C заного")
