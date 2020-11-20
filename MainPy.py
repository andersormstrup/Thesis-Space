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

from DLtester2 import DLObjectDetector

## - Main Loop -------------------------------------------------------------------------------
#src_path = sys.argv[1] if len(sys.argv) > 1 else '.'



window = ThemedTk(theme="equilux")



rootwin = MainWindow(window) #, deep)

deep = DLObjectDetector()

watcher = FileWatcher(rootwin, deep)


#FileWatcher.my


window.mainloop()




## - Execute procedure / Close Program:
#window.destroy


#& "C:/Users/Anders Ormstrup/anaconda3/envs/gpuee/python.exe" "c:/Users/Anders Ormstrup/Documents/GitHub/Thesis-Space/MainPy.py"

#"python.pythonPath": "C:\\Users\\Ander\\AppData\\Local\\Programs\\Python\\Python39\\python.exe",