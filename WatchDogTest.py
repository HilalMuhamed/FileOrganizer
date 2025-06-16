import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv

source = os.getenv("SOURCE")
destPdf = os.getenv("DEST_PDF")
destDoc = os.getenv("DEST_DOC")
destPpt = os.getenv("DEST_PPT")
destSound = os.getenv("DEST_SOUND")
destImg = os.getenv("DEST_IMG")

imgExtentions = [".jpg", ".jpeg", ".jpe", ".png", ".gif", ".svg"]
soundExtentions = [".mp3", ".wav"]
documentExtentions = [".doc",".docx",".txt",".xls",".xlsx"]
pptExtentions = [".ppt",".pptx"]
pdfExtentions = [".pdf"]

def move_file(dest,entry,name):
    shutil.move(entry,dest)

class FileMovement(FileSystemEventHandler):
    path = source
    def on_modified(s,event):
        try:
            with os.scandir(path) as entries:
                for entry in entries:
                    name = entry.name.lower()
                    if entry.stat().st_size < 100000000:  # Less than 100MB
                        s.isPdf(name,entry)
                        s.isDoc(name,entry)
                        s.isImg(name,entry)
                        s.isPpt(name,entry)
                        s.isSound(name,entry)
        except Exception as e:
            print("Cant affect this file",e);
    def isPdf(s,name,entry):
            for pdfExtention in pdfExtentions:
                    if name.endswith(pdfExtention):
                        print(entry.name)
                        move_file(destPdf,entry,name)
    def isDoc(s,name,entry):
            for docExtention in documentExtentions:
                    if name.endswith(docExtention):
                        print(entry.name)
                        move_file(destDoc,entry,name)
    def isPpt(s,name,entry):
            for pptExtention in pptExtentions:
                    if name.endswith(pptExtention):
                        print(entry.name)
                        move_file(destPpt,entry,name)
    def isSound(s,name,entry):
            for soundExtention in soundExtentions:
                    if name.endswith(soundExtention):
                        print(entry.name)
                        move_file(destSound,entry,name)
    def isImg(s,name,entry):
            for imgExtention in imgExtentions:
                    if name.endswith(imgExtention):
                        print(entry.name)
                        move_file(destImg,entry,name)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source
    event_handler = FileMovement()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()