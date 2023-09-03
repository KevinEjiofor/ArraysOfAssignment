def sameColor(list , list2):
    return set(list2) & set(list)



if __name__ == '__main__':
    color_list_1 = {"White", "Black", "Red"}
    color_list_2 = {"Red", 'Green'}
    result = sameColor(color_list_1,color_list_2)
    print(result)