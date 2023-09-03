def fibonacci():
       n1 ,n2= 0,1

       n = 50

       for _ in range(n + 1):
              if n1 <= 50:
               print(n1, end= " ")

              nth = n1 + n2
              n1 = n2
              n2 = nth


if __name__ == '__main__':
       print( fibonacci())




