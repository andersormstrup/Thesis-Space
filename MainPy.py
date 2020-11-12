## - Main Python script to run on machine. 
## - Imports for all scripts --
from ttkthemes import ThemedTk


import sys
import time
#from watchdog.observers import Observer
#from events import ImagesEventHandler

#import os
# from PIL import Image
# from PIL.ImageOps import grayscale
# from watchdog.events import RegexMatchingEventHandler

# -----Own Setup Script
from UIsetup import MainWindow
from WatcherTest1 import FileWatcher

## - Main Loop -------------------------------------------------------------------------------
#src_path = sys.argv[1] if len(sys.argv) > 1 else '.'



window = ThemedTk(theme="equilux")

#deep = LoadDetection()

rootwin = MainWindow(window) #, deep)

watcher = FileWatcher(rootwin)

#FileWatcher.my


window.mainloop()




## - Execute procedure / Close Program:

#window.destroy






