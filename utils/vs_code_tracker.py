import psutil
import time
from win10toast import ToastNotifier

elapsed_minutes = 0


def track_vs_code_usage(threshold=30):
    toaster = ToastNotifier()
    global elapsed_minutes
    while True:
        print("TRACKING VS CODE SCREENTIME")
        active_process_names = [p.name()
                                for p in psutil.process_iter(['name'])]
        # print(active_process_names)
        if 'Code.exe' in active_process_names:
            if elapsed_minutes == 0:
                print("Timer Started for this session")
                start_time = time.time()
            while 'Code.exe' in active_process_names:
                time.sleep(15)  # check every 15 seconds
                active_process_names = [p.name()
                                        for p in psutil.process_iter(['name'])]
            end_time = time.time()
            print("VS Code closed, timer stopped")

            elapsed_minutes += (end_time - start_time) / 60
            elapsed_seconds = int(
                (elapsed_minutes - int(elapsed_minutes)) * 60)
            formatted_time = "{:02d}:{:02d}".format(
                int(elapsed_minutes), elapsed_seconds)
            print("Elapsed time is: ", elapsed_minutes)
            if elapsed_minutes < threshold:
                message = f"You've been on VS Code for {formatted_time} minutes. If you need to be a \"REAL GIGACHAD Programmer\" you need to code more!"
                toaster.show_toast("Today's VS Code Usage",
                                   message, duration=15, icon_path="assets\iProDUCK.ico")
        time.sleep(15)  # check every 15 seconds
