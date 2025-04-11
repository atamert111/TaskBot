import unittest
from database import add_task, show_tasks, init_db

class TestTaskListing(unittest.TestCase):
    def setUp(self):
        # Her testten önce veritabanını temizle
        init_db()

    def test_multiple_tasks_are_visible_in_list(self):
        # İki farklı görev ekle
        add_task("Müşteri toplantısı planla")
        add_task("Haftalık raporu gönder")

        # Görev listesini al
        task_list = show_tasks()
        task_descriptions = [task[1] for task in task_list]

        # Her iki görev de listede yer almalı
        self.assertIn("Müşteri toplantısı planla", task_descriptions, msg="İlk görev listede görünmüyor.")
        self.assertIn("Haftalık raporu gönder", task_descriptions, msg="İkinci görev listede görünmüyor.")

if __name__ == "__main__":
    unittest.main()
