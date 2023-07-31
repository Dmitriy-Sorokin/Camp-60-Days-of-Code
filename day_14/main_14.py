import simple


def foo(temp):
    if int(temp) > 25:
        return "Hot"
    elif 15 <= int(temp) <= 25:
        return "Warm"
    elif int(temp) < 15:
        return "Cold"

print(foo(26))