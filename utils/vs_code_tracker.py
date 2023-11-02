import psutil
import time
from win10toast import ToastNotifier


def track_vs_code_usage(threshold=30):
    toaster = ToastNotifier()
    while True:
        print("TRACKING VS CODE SCREENTIME")
        active_process_names = [p.name()
                                for p in psutil.process_iter(['name'])]
        # print(active_process_names)
        if 'Code.exe' in active_process_names:
            start_time = time.time()
            print("Timer Started..")
            while 'Code.exe' in active_process_names:
                time.sleep(15)  # check every 15 seconds
                active_process_names = [p.name()
                                        for p in psutil.process_iter(['name'])]
            end_time = time.time()
            print("VS Code Closed, timer stopped")
            elapsed_minutes = (end_time - start_time) / 60
            print("Elapsed time is: ", elapsed_minutes)
            if elapsed_minutes < threshold:
                message = f"You've been using vs code for {elapsed_minutes:.2f} minutes. You need to study more!"
                toaster.show_toast("VS Code Usage Notifier",
                                   message, duration=10)
        time.sleep(15)  # check every 15 seconds
