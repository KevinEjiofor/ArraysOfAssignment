import datetime


def current_time():

   return datetime.datetime.now()

if __name__ == '__main__':
    time = current_time()
    print(time)