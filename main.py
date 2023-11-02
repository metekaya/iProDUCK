import os
import time
import threading

from dotenv import load_dotenv
from watchdog.observers import Observer

from utils.vs_code_tracker import track_vs_code_usage
from utils.file_organizer import DownloadHandler


def main():
    load_dotenv()
    DOWNLOAD_FOLDER_PATH = os.getenv('DOWNLOAD_FOLDER_PATH')
    print("SCRIPT STARTED")

    vs_code_thread = threading.Thread(target=track_vs_code_usage, args=(120,))
    vs_code_thread.start()
    
    
    event_handler = DownloadHandler(DOWNLOAD_FOLDER_PATH)
    observer = Observer()
    observer.schedule(event_handler, DOWNLOAD_FOLDER_PATH, recursive=False)
    observer.start()
    print("OBSERVER IS LOOKING FOR FILE CHANGES")
    try: 
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program stopped by the user")
