import datetime


def current_time(user):

   return user - datetime.datetime.now()

if __name__ == '__main__':

    user_entry = int(input("Enter the date: "))
    time = current_time(user_entry)
    print(time)