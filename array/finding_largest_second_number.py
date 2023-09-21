def largest():
    largest_number = 0
    second_largest_number = 0
    word = "dfa12321afd"
    num = word.isdigit()

    if num > largest_number:
        second_largest_number = largest_number
        largest_number = num
    elif num > second_largest_number != largest_number:
        second_largest_number = num

    return second_largest_number


