# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     max_num = 0
#     for item in grades:
#         if item > max_num:
#             max_num = item
#     print(max_num)
#
# get_max()

# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     max_i = grades.sort()
#     print(grades)
#     min_i = 10
#     # for item in grades:
#     #     if item > max_i:
#     #         max_i = item
#     #     if item < min_i:
#     #         min_i = item
#     # return print(f"Max:{max_i},Min:{min_i}")
#
#
# get_max()


def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)