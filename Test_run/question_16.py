

def number(sample):
   return {nums for nums in sample    if nums % 2 == 0 and nums <= 237}





if __name__ == '__main__':
    sample_number = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219,
                     918, 237, 412, 566,
                     826, 248, 866, 950, 626, 949, 687, 217, 816, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 370,
                     843,
                     831, 445, 742, 717, 958, 743, 527]

    result = number(sample_number)
    print(sorted(result))

