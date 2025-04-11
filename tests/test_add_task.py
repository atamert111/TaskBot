import unittest
from database import add_task, show_tasks, init_db

class TestTaskAddition(unittest.TestCase):
    def setUp(self):
        # Her testten önce veritabanını sıfırla
        init_db()

    def test_task_is_added_and_visible(self):
        task_description = "Kütüphaneye kitap iade et"
        add_task(task_description)

        task_list = show_tasks()
        descriptions = [task[1] for task in task_list]

        self.assertIn(task_description, descriptions, msg="Görev listeye eklenmemiş gibi görünüyor.")

if __name__ == "__main__":
    unittest.main()
