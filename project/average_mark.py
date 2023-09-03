counter = 0
total = 0
while counter < 20:
    student = int(input("Enter student score: "))
    total = total + student
    counter = counter + 1
average = total/counter
print(f"""
**************************************************************************************
                Aso Rock ,Secondary School, Abuja Nigeria
**************************************************************************************
Class: SSS 3
Number of Student in class:  {counter}
Total score = {total} 
average =  {average}""")