# TaskBot – Discord Görev Takip Botu

TaskBot, bireysel olarak geliştirdiğim bir Discord görev takip botudur. Python programlama dili ve `discord.py` kütüphanesi kullanılarak yazılmıştır.

Bot, kullanıcıların sohbet üzerinden kolayca görev eklemesini, mevcut görevleri görüntülemesini, tamamlamasını ve silmesini sağlar.  
Tüm görev verileri, yerel bir SQLite veritabanında güvenli şekilde saklanır ve bot yeniden başlatıldığında dahi korunur.

Bu proje, hem Discord bot geliştirme pratiği yapmak hem de yazılım testleri (unit test) konusundaki yetkinliğimi artırmak amacıyla hazırlanmıştır.

---

##  Nasıl Çalışır

- Proje klasörüne geç:  
  `cd task_manager_bot`

- (Opsiyonel) Sanal ortam oluştur:  
  `python3 -m venv venv`  
  `source venv/bin/activate`

- Gereksinimleri yükle:  
  `pip install -r requirements.txt`

- Görevleri test et:  
  `python run_tests.py`  

###  Örnek Çıktı:

test_add_single_task (test_add_task.TestAddTask.test_add_single_task) ... ok test_complete_task_marks_as_done (test_complete_task.TestCompleteTask.test_complete_task_marks_as_done) ... ok test_delete_task (test_delete_task.TestDeleteTask.test_delete_task) ... ok test_show_tasks_returns_correct_data (test_show_tasks.TestShowTasks.test_show_tasks_returns_correct_data) ... ok

Ran 4 tests in 0.005s

OK

- Botu başlat:  
  `python bot.py`

- Discord sunucuna gidip komutları kullan:  
  `!add_task Bu bir görevdir`  
  `!show_tasks`

---

##  Özellikler

-  Görev ekle: `!add_task <görev açıklaması>`
-  Görevleri listele: `!show_tasks`
-  Görev tamamla: `!complete_task <görev_id>`
-  Görev sil: `!delete_task <görev_id>`

---

##  Geliştirici

**Ata Mert Erdihan**  
🎓 Kodland Python Eğitmenlik başvuru projesi  
💻 Python • Discord.py • SQLite • Unit Test

---

## 🗂️ Proje Klasör Yapısı

```bash
task_manager_bot/
├── bot.py                  # Discord bot komutları
├── database.py             # SQLite veritabanı işlemleri
├── tests/                  # Otomatik testler
│   ├── test_add_task.py
│   ├── test_delete_task.py
│   ├── test_show_tasks.py
│   └── test_complete_task.py
├── requirements.txt        # Bağımlılık listesi
├── README.md               # Bu dosya
└── run_tests.py            # Tüm testleri çalıştıran script
