def look(element):
    duplicate = [i for i in element if element.count(i) == 1]

    return duplicate


if __name__ == '__main__':
    inputElement = [2, 2, 1]
    inputElement2 = [4, 3, 2, 2, 3, 3]

    print(look(inputElement), look(inputElement2))
