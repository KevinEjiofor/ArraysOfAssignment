def check_intersection(list, list2):
    # intersection = set(list2) & set(list)
    #
    # return tuple(intersection)


    new_line = {element for element in list if element in list2}



    return tuple(new_line)



if __name__ == '__main__':
    list1 = [20, 30, 60, 65, 65, 75,65, 80, 85]
    list2 = [42, 30, 30, 80, 65, 68, 88, 95]

    print(check_intersection(list1,list2))


