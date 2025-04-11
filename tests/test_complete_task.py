import unittest
from database import add_task, complete_task, show_tasks, init_db

class TestTaskCompletion(unittest.TestCase):
    def setUp(self):
        # Teste başlamadan önce veritabanını başlat
        init_db()
        # Tamamlanacak bir görev ekle
        add_task("Sunum için slaytları hazırla")

    def test_task_completion_updates_status(self):
        task_list = show_tasks()
        task_id = task_list[0][0]

        # Görevi tamamla
        complete_task(task_id)

        # Güncel durumu kontrol et
        updated_task = next(task for task in show_tasks() if task[0] == task_id)
        is_completed = updated_task[2]

        self.assertEqual(is_completed, 1, msg="Görev tamamlandı olarak işaretlenmemiş.")

if __name__ == "__main__":
    unittest.main()
