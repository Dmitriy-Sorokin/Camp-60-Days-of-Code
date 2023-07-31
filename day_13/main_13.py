# def get_age(year_of_birth: int, current_year=2023):
#     ears_old = current_year - year_of_birth
#     return ears_old
# print(get_age(1992))

# def get_nr_items(lsit_str):
#
#     a = lsit_str.split()[0].split(",")
#
#     return len(a)
#
# print(get_nr_items('apple,banana,orange'))

# def foo(temp: int):
#     if temp > 7:
#         return "Warm"
#     elif temp <= 7:
#         return "Cold"

# def foo(string: str):
#     if len(string) < 8:
#         return False
#     elif len(string) >= 8:
#         return True

def calculate_time(h ,g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(h=100)
print(time)
