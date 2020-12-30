## - Main Python script to run on machine. 
## - Imports for all scripts --
from ttkthemes import ThemedTk
import sys
import time
# -----Own Setup Script
from x02UiSetup import MainWindow           # Script UI setup
from x03DeepLearningDetection import DLObjectDetector # Script Object detection
from x04FileWatcher import FileWatcher      # Script File triggering
## - Main Loop --------------------------
window = ThemedTk(theme="equilux")          # Creating UI instance
rootwin = MainWindow(window)                # Passing it into UI setup.
deep = DLObjectDetector()                   # Creating Detection instance.
watcher = FileWatcher(rootwin, deep)        # Passing on Detection and UI.
window.mainloop()                           # Run as Main loop.
