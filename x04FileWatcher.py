## - Imports for FileWatcher --
import time                 # Time Handling
import os                   # Path Handling
# Import observer functions from watchdog libary.
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# Creating Filewatcher class with file observer instances.
class FileWatcher():
    # Initilization, only runs ONCE.
    def __init__(self, rootwin, deep):
        # Settings for filewatcher.
        patterns = "*"
        ignore_patterns = ""
        ignore_directories = False
        case_sensitive = True
        # Event Handlers for triggering.
        my_event_handler1 = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
        my_event_handler2 = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
        my_event_handler3 = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

        # Event for Camera 1. 
        def on_created1(event):
            time.sleep(0.1)                 # Sleep to prevent open error.
            start_time = time.time()        # Start timer.
            print(f"Oprettet {event.src_path} has been created! - Detection started")
            rootwin.OutUpdate(f"Oprettet {event.src_path} - Detection started") # Update output.
            # Passing filename and calling detection event from DL script, getting image and classes.
            detectimg, detClasses = deep.DetectOnImage(event.src_path)
            # Pass image and classes for UI presentation and reject/accept function.
            rootwin.detection1(detectimg, detClasses, event.src_path)
            end_time = time.time()          # Stop timer and print elapsed time.
            rootwin.OutUpdate(f"Behandlingstid: {end_time - start_time:.4f} sek")

        # Event for Camera 2.
        def on_created2(event):
            time.sleep(0.1)                 # Sleep to prevent open error.
            start_time = time.time()
            print(f"Oprettet {event.src_path} has been created! - Detection started")
            rootwin.OutUpdate(f"Oprettet {event.src_path} - Detection started") # Update output.
            # Passing filename and calling detection event from DL script, getting image and classes.
            detectimg, detClasses = deep.DetectOnImage2(event.src_path)
            # Pass image and classes for UI presentation and reject/accept function.
            rootwin.detection2(detectimg, detClasses, event.src_path)
            end_time = time.time()          # Stop timer and print elapsed time.
            rootwin.OutUpdate(f"Behandlingstid: {end_time - start_time:.4f} sek")

        # Event for Camera 3.
        def on_created3(event):
            time.sleep(0.1)                 # Sleep to prevent open error.
            start_time = time.time()
            print(f"Oprettet {event.src_path} has been created! - Detection started")
            rootwin.OutUpdate(f"Oprettet {event.src_path} - Detection started") # Update output.
            # Passing filename and calling detection event from DL script, getting image and classes.
            detectimg, detClasses = deep.DetectOnImage3(event.src_path)
            # Pass image and classes for UI presentation and reject/accept function.
            rootwin.detection3(detectimg, detClasses, event.src_path)
            end_time = time.time()          # Stop timer and print elapsed time.
            rootwin.OutUpdate(f"Behandlingstid: {end_time - start_time:.4f} sek")            

        # On create event function callers.
        my_event_handler1.on_created = on_created1
        my_event_handler2.on_created = on_created2
        my_event_handler3.on_created = on_created3
        # Setting paths for observing for filechanges.
        basepath = os.path.dirname(os.path.realpath(__file__))
        path1 = os.path.join(basepath, 'FTPBilleder1')
        path2 = os.path.join(basepath, 'FTPBilleder2')
        path3 = os.path.join(basepath, 'FTPBilleder3')
        go_recursively = True # Repeatable events!
        # Observer instances for three folders.
        my_observer1 = Observer()
        my_observer1.schedule(my_event_handler1, path1, recursive=go_recursively)
        my_observer2 = Observer()
        my_observer2.schedule(my_event_handler2, path2, recursive=go_recursively)
        my_observer3 = Observer()
        my_observer3.schedule(my_event_handler3, path3, recursive=go_recursively)
        # Start observers.
        my_observer1.start()
        my_observer2.start()
        my_observer3.start()

        