#
# questions = [{"What color grass?": {
#     "red": 1,
#     "green": 2
# }},
#     {"What color is the sky?": {
#         "eloy": 1,
#         "blue": 2
#     }}]
#
# count = 0
# tr = 0
# fl = 0
# result = []
#
# while count < len(questions):
#     print(count,"asfsaf")
#     print(str(questions[count].keys()).replace("dict_keys(['", "").replace("'])", ""))
#
#     for item in questions[count].values():
#         for keys in item:
#             counter = 0
#             print(f"{counter + 1}-{keys}")
#
#     user_input = int(input("Enter your answer: "))
#
#     if user_input == 2:
#         write_answer = f"{count + 1} Correct answer: User answer: 2, Correct answer: 2"
#         result.append(write_answer)
#         tr += 1
#         count += 1
#     else:
#         looser_answer = f"{count + 1} Incorrect answer: User answer: 1, Correct answer: 2"
#         result.append(looser_answer)
#         fl += 1
#         count += 1
#
#
# for item in result:
#     print(item)
# print(f"Score {tr}/{fl}")


def append_list(list=[]):
    list.append(len(list))
    return list

for i in range(4):
    append_list()

result_1 = append_list([0])
result_2 = append_list()

print(result_1, result_2, sep="\n")
