## - Main Python script to run on machine. 
## - Imports for all scripts --
from ttkthemes import ThemedTk


import sys
import time
from watchdog.observers import Observer
#from events import ImagesEventHandler

import os
from PIL import Image
from PIL.ImageOps import grayscale
from watchdog.events import RegexMatchingEventHandler

# ----- Setup Script
from UIsetup import MainWindow

## - Main Loop -------------------------------------------------------------------------------

window = ThemedTk(theme="equilux")
MainWindow(window)



window.mainloop()

## - Execute procedure / Close Program:








