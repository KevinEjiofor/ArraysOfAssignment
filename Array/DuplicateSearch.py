from os import remove


def look(word):
    duplicate = [i for i in word if word.count(i) == 1]
    # list = []
    # for i in word:
    #     if i not in list:
    #         list += [i]

    return duplicate


dup = ["james", "paul", "peter", "james"]
print(look(dup))


def size(list1):
    element = 0

    for i in list1:
        element += 1

    return element


john = ["a", "b", "c", ]
call = size(john)
print(call)
