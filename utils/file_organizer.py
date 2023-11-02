import os
import shutil
from watchdog.events import FileSystemEventHandler

class DownloadHandler(FileSystemEventHandler):
    def __init__(self, download_path):
        self.download_path = download_path

    def on_modified(self, event):
        if not event.is_directory:
            self.organize_files()

    def organize_files(self):
        file_types = {
            'Images': ['.jpg', '.jpeg', '.png', ".webp",'.gif', '.svg'],
            'PDF': ['.pdf'],
            'Documents': ['.xlsx', '.doc', '.docx', '.pptx','.txt'],
            'Videos': ['.mp4', '.mov', '.avi'],
            'Archives': ['.zip', '.rar', '.tar', '.gz'],
            'Torrents': ['.torrent'],
        }

        for filename in os.listdir(self.download_path):
            file_extension = os.path.splitext(filename)[1]
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    category_path = os.path.join(self.download_path, category)
                    if not os.path.exists(category_path):
                        os.mkdir(category_path)
                    shutil.move(os.path.join(self.download_path, filename), os.path.join(category_path, filename))