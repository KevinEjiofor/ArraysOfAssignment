total = 0
counter = 0
while True:
    student = int(input("Enter student score 0r input -25 to break : "))
    if student >= 0:
        total = total + student
        counter = counter + 1
    if student == -25:
        break
average = total / counter
print(f""""
**************************************************************************************     
               Aso Rock, Secondary School, Abuja Nigeria
****************************************************************************************
Class: SSS 3
Number of student: {counter}
Total score = {total}
average = {average}""")
