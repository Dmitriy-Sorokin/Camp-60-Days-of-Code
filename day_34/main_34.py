import re

with open("miracle_in_the_andes.txt", "r", encoding="utf-8") as file:
    book = file.read()
    # print(book.count("Chapter"))
    # # With regex
    # pattern = re.compile("Chapter [0-9]+")
    # print(re.findall(pattern, book))
    #
    # pattern = re.compile("[^.]* love [a-zA-Z]*")
    # finding = re.findall(pattern, book)
    # # print(finding)

    pattern = re.compile("[a-zA-Z]+")
    finding = re.findall(pattern, book.lower())
    # print(finding)
    d = {}
    for word in finding:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1
    # print(d)
    d_list = [(value, key) for (value, key) in d.items()]
    sorted_list = sorted(d_list, reverse=True)
    print(sorted_list)