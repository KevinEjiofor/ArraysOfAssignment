def look(element):
    duplicate = [i for i in element if element.count(i) > 1]

    return max(duplicate)


def without_count(element):
    element_counts = {}
    max_value = None
    max_count = 0

    for item in element:
        if item in element_counts:
            element_counts[item] += 1
        else:
            element_counts[item] = 1

        if element_counts[item] > 1 and (max_value is None or element_counts[item] > max_count):
            max_value = item
            max_count = element_counts[item]

    return max_value


if __name__ == '__main__':
    nums = [3, 2, 3]

    num2 = [2, 2, 1, 1, 1, 2, 2]

    result = without_count(nums)
    result2 = without_count(num2)

    print(result)
    print(result2)
