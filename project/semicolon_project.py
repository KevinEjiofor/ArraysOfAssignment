First_name = input('Enter your First name: ')
if First_name == '':
    print('First name can not be empty')
    exit()
last_name = input('Enter your last name: ')
if last_name == '':
    print('last name can not be empty')
    exit()

age = int(input('Enter your age '))
if age == '':
    print('put your age ')
if age < 0:
    print('Age can not be negative ')
elif age < 18:
    print('you are under age')
elif age > 65:
    print('you are too old')

print('your name is ', First_name, last_name)
print('your age is', age)

