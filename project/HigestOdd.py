def number(digital):
    largest = digital[0]

    for num in digital:
        if num % 2 != 0:
            if num > largest:
                largest = num

    return largest


odd = [709, 703, 705, 707, 600, 7, 105]
call = number(odd)
print(f"Largest: {call}")
