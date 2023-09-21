import unittest

import unittest

from test.diaryApp.diary import Diary


class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("world war", "good")
        self.diary.create_entry("word", "bad")
        self.diary.lock_diary()

    def test_if_diary_is_locked(self):
        check = self.diary.is_locked
        self.assertTrue(check)

    def test_unlock_with_password(self):
        self.diary.unlock("good")
        new_check = self.diary.is_locked
        self.assertFalse(new_check)

    def test_to_unlock_with_wrong_password(self):
        with self.assertRaises(Exception):
            self.diary.unlock("pppp")

    def test_to_create_an_entry(self):
        self.diary.create_entry("ziggy", "word")
        self.assertEqual(1, self.diary.find_entry(1).get_id())

    def test_to_get_more_entries(self):
        self.diary.create_entry("ziggy", "word")
        self.assertEqual("word bad", self.diary.find_entry(1).get_diary_details())
        self.assertEqual("ziggy word", self.diary.find_entry(2).get_diary_details())

    def test_for_deleting_entry(self):
        self.diary.unlock("good")
        self.diary.create_entry("ziggy", "word")
        self.assertEqual(2, self.diary.find_entry(2).get_id())
        self.diary.delete_entry(1)
        check_size = self.diary.get_size()
        self.assertEqual(1, check_size)

    def test_to_update_diary(self):
        self.diary.unlock("good")
        self.diary.create_entry("ziggy", "word")
        self.assertEqual("word bad", self.diary.find_entry(1).get_diary_details())
        self.assertEqual("ziggy word", self.diary.find_entry(2).get_diary_details())
        self.diary.update_entry(2, "war", "run")
        check = self.diary.find_entry(2).get_diary_details()
        self.assertEqual("war run", check)

