import psutil
import time
from win10toast import ToastNotifier

def track_vs_code_usage(threshold=30):
    toaster = ToastNotifier()
    while True:
        active_process_names = [p.name() for p in psutil.process_iter(['name'])]
        # print(active_process_names)
        if 'Code.exe' in active_process_names:
            start_time = time.time()
            while 'Code.exe' in active_process_names:
                time.sleep(30) # 30 saniyede bir kontrol et..
                active_process_names = [p.name() for p in psutil.process_iter(['name'])]
            end_time = time.time()
            elapsed_minutes = (end_time - start_time) / 60
            if elapsed_minutes < threshold:
                message = f"VS Code kullanım süreniz {elapsed_minutes:.2f} dakikadır. Daha fazla çalışmaya ihtiyacınız var!"
                toaster.show_toast("VS Code Kullanım Uyarısı", message, duration=10)
        time.sleep(30) # 30 saniyede bir kontrol et..
