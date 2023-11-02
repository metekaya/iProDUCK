import psutil
import time
import sqlite3
import os
import datetime

from pynput.keyboard import Listener
from win10toast import ToastNotifier

# WILL LOOK UP TO THIS LATER..

# def get_chrome_history(site_url, threshold_minutes=60):
#     toaster = ToastNotifier()
#     while True:
#         data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default'
#         files = os.listdir(data_path)
#         history_file = os.path.join(data_path, 'History')

#         c = sqlite3.connect(history_file)
#         cursor = c.cursor()
#         select_statement = "SELECT urls.url, urls.visit_count, urls.last_visit_time FROM urls WHERE urls.url LIKE '%" + site_url + "%'"

#         cursor.execute(select_statement)
#         results = cursor.fetchall()

#         total_time_spent = 0

#         for row in results:
#             visit_time = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=row[2])
#             current_time = datetime.datetime.now()
#             time_difference = current_time - visit_time
#             total_time_spent += time_difference.total_seconds()

#         total_time_spent /= 60  # to get total time in minutes

#         if total_time_spent > threshold_minutes:
#             message = f"You have spent {total_time_spent} minutes on {site_url}. Take a break!"
#             toaster.show_toast("VS Code Kullanım Uyarısı", message, duration=10)
#             print(f"You have spent {total_time_spent} minutes on {site_url}. Take a break!")


#         time.sleep(10)




# def track_chrome_activity(url, threshold=60):
#     toaster = ToastNotifier()
#     is_chrome_running = False
#     site_timer = 0

#     def on_press(key):
#         nonlocal is_chrome_running, site_timer
#         if is_chrome_running and key == 'Key.space':
#             site_timer += 1
    
#     with Listener(on_press=on_press) as listener:
#         while True:
#             active_processes = psutil.process_iter(['name', 'cmdline'])
#             for p in active_processes:
#                 if p.info['name'] == 'chrome.exe':
#                     is_chrome_running = True
#                     if url in psutil.Process(p.pid).cmdline():
#                         if site_timer >= threshold:
#                             message = f"You have spent {site_timer} minutes on {url}. You need more!!!"
#                             toaster.show_toast("VS Code Kullanım Uyarısı", message, duration=10)
#                         site_timer = 0
#                 else:
#                     is_chrome_running = False

#             time.sleep(30) # 30 saniyede bir kontrol et.