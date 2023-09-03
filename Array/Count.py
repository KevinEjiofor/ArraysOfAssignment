def check(word_list):
    word_counts = {}

    for word in word_list:
        lowercase_word = word.casefold()
        if lowercase_word not in word_counts:
            word_counts[lowercase_word] = 1
        else:
            word_counts[lowercase_word] += 1

    return word_counts


if __name__ == "__main__":
    Student = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male',
               'Female']
    result = check(Student)
    print(result)
