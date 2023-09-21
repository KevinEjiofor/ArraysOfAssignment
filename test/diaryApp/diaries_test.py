import unittest

from test.bankApp.exception import CustomerException
from test.diaryApp.diaries import Diaries


class TestDiaries(unittest.TestCase):
    def setUp(self):
        self.diary = Diaries()
        self.diary.add_new_user("GodPower", "home")

    def test_diaries_for_multiple_user(self):
        self.diary.add_new_user("Hope", "joy")
        self.assertEqual(2, self.diary.get_all_users())

    def test_diaries_to_find_user_exist(self):
        self.diary.add_new_user("Hope", "joy")
        is_user_existing = self.diary.user_exists("Godpower")
        self.assertTrue(is_user_existing)

    def test_diaries_to_find_user_exist_in_lower_casing(self):
        self.diary.add_new_user("Hope", "joy")
        is_user_existing = self.diary.user_exists("godpower")
        self.assertTrue(is_user_existing)

    def test_diaries_for_non_existing_user(self):
        with self.assertRaises(CustomerException):
            self.diary.user_exists("godpowers")

    def test_diaries_to_delete_user(self):
        self.diary.delete_user("GodPower")
        number_of_users = self.diary.get_all_users()
        self.assertEqual(0, number_of_users)





