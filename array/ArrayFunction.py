def Max(numbers):
    largest = numbers[0]
    for num in numbers:
        num > largest
        largest = num

    return largest


numbers = [3, 4, 56, 5, 6]
call = max(numbers)
print(f"largest: {call}")


