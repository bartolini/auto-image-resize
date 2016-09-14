import config
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
from resizeimage import resizeimage

class ImageObserver(FileSystemEventHandler):

    def __init__(self, sizes):
        self.sizes = sizes
        self.expected_files = set()

    def on_created(self, event):
        filename, extension = os.path.splitext(event.src_path)
        if extension.lower() not in ['.jpg', '.jpeg', '.png']:
            return
        if event.src_path in self.expected_files:
            self.expected_files.remove(event.src_path)
            return
        with open(event.src_path, 'rb') as original_image:
            for size in self.sizes:
                expected_file = '%s_%s%s' % (filename, size, extension)
                self.expected_files.add(expected_file)
                try:
                    with Image.open(original_image) as image:
                        cover = resizeimage.resize_cover(image, self.sizes[size])
                        cover.save(expected_file, image.format)
                except:
                    self.expected_files.remove(expected_file)

def watch_folder(folder, sizes):
    observer = Observer()
    observer.schedule(ImageObserver(sizes), folder)
    observer.start()
    return observer

if __name__ == '__main__':
    observers = [watch_folder(os.path.abspath(folder), config.SIZES) for folder in config.FOLDERS]
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for observer in observers:
            observer.stop()
    for observer in observers:
        observer.join()
