# from test.bankApp.exception import CustomerException
from test.bankApp.exception import CustomerException
from test.diaryApp.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add_new_user(self, user_name, password):
        diary = Diary(user_name, password)
        self.diaries.append(diary)

    def find_user(self, user_name):
        for diary in self.diaries:
            if diary.get_user_name().lower() == user_name.lower():
                return diary
        raise CustomerException("USER NOT FOUND")

    def delete_user(self, user_name):
        user = self.find_user(user_name)
        self.diaries.remove(user)

    def get_all_users(self):
        return len(self.diaries)

    def user_exists(self, user_name):
        if any(diary.get_user_name().casefold() == user_name.casefold() for diary in self.diaries):
            return True

        raise CustomerException("USER NOT FOUND")
