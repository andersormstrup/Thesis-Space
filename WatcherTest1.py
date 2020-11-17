import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class FileWatcher():

    def __init__(self, rootwin, deep):
        #if __name__ == "__main__":
        patterns = "*"
        ignore_patterns = ""
        ignore_directories = False
        case_sensitive = True
        my_event_handler1 = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
        my_event_handler2 = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
        my_event_handler3 = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


        def on_created1(event):
            start_time = time.time()
            print(f"hey, {event.src_path} has been created! - Detection started")
            detecimg = deep.DetectOnImage(event.src_path)
            rootwin.detection1(detecimg)
            print(f"hey, {event.src_path} has been created! - Detection ended")
            end_time = time.time() 
            print(end_time - start_time)


        def on_created2(event):
            rootwin.detection2(event.src_path)
            print(f"hey, {event.src_path} has been created!")

        def on_created3(event):
            rootwin.detection3(event.src_path)
            print(f"hey, {event.src_path} has been created!")
    
        # def on_deleted(event):
        #     print(f"what the f**k! Someone deleted {event.src_path}!")
            
        # def on_modified(event):
        #     print(f"hey buddy, {event.src_path} has been modified")

        # def on_moved(event):
        #     print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")


        my_event_handler1.on_created = on_created1
        my_event_handler2.on_created = on_created2
        my_event_handler3.on_created = on_created3

        # my_event_handler.on_deleted = on_deleted
        # my_event_handler.on_modified = on_modified
        # my_event_handler.on_moved = on_moved

        basepath = os.path.dirname(os.path.realpath(__file__))
        path1 = os.path.join(basepath, 'FTP1')
        path2 = os.path.join(basepath, 'FTP2')
        path3 = os.path.join(basepath, 'FTP3')
        

        go_recursively = True

        my_observer1 = Observer()
        my_observer1.schedule(my_event_handler1, path1, recursive=go_recursively)
        my_observer2 = Observer()
        my_observer2.schedule(my_event_handler2, path2, recursive=go_recursively)
        my_observer3 = Observer()
        my_observer3.schedule(my_event_handler3, path3, recursive=go_recursively)


        my_observer1.start()
        my_observer2.start()
        my_observer3.start()



# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     my_observer.stop()
#     my_observer.join()

