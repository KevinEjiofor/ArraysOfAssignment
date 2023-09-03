def divisible():
    for num in range(1500,1700):
        if num % 5 == 0 and num % 7 == 0:
            print("number can be divided by 5 and 7")
        elif num % 5 == 0 :
            print(" number can be divided only 5")
        elif num % 7 == 0:
            print(" number can be divided only 7")
        else:
            print(num)


if __name__ == '__main__':

    result = divisible()

    print(result)