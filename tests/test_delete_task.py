import unittest
from database import add_task, delete_task, show_tasks, init_db

class TestTaskDeletion(unittest.TestCase):
    def setUp(self):
        # Veritabanını sıfırla ve bir görev ekle
        init_db()
        add_task("Eski projeyi temizle")

    def test_task_is_removed_from_list(self):
        # Mevcut görev listesini al ve ID'yi yakala
        initial_tasks = show_tasks()
        task_id = initial_tasks[0][0]

        # Görevi sil
        delete_task(task_id)

        # Güncellenmiş listede görev ID’si var mı kontrol et
        remaining_tasks = show_tasks()
        task_ids = [task[0] for task in remaining_tasks]

        self.assertNotIn(task_id, task_ids, msg="Görev silinememiş gibi görünüyor.")

if __name__ == "__main__":
    unittest.main()
