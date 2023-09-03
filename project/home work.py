# fail = 0
# counter = 1
# player = 0
# while player != 1 or player != 2:
#
#     print("you entered a wrong number")
#     player = int(input("Enter a number: "))
#     fail = counter - 1
#     counter = counter + 1
#     if player == 1:
#         break
#     if player == 2:
#         break
# print(f"number of time you failed : = {fail}")

passes = 0
failures = 0
wrong_entry = 0
student_grade = 1
while student_grade <= 10:
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes = passes + 1
        student_grade = student_grade + 1
    elif result == 2:
        failures = failures + 1
        student_grade = student_grade + 1
    else: wrong_entry = wrong_entry + 1

print('Passed:', passes)
print('Failed:', failures)
if passes > 8:
    print('Bonus to instructor')







