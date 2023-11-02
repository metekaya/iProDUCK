import time
import threading

from utils.vs_code_tracker import track_vs_code_usage
from utils.file_organizer import DownloadHandler
from watchdog.observers import Observer


def main():
    print("it works!")

    # vs_code_thread = threading.Thread(target=track_vs_code_usage(120))
    # vs_code_thread.start()
    
    download_path = 'C:\\Users\\username\\Downloads'
    event_handler = DownloadHandler(download_path)
    observer = Observer()
    observer.schedule(event_handler, download_path, recursive=False)
    observer.start()
    print("OBSERVER IS LOOKING FOR FILE CHANGES")
    try: 
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
