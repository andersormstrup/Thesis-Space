## - Main Python script to run on machine. 
## - Imports for all scripts --
from ttkthemes import ThemedTk



# ----- Setup Script
from UIsetup import MainWindow




## - Main Loop -------------------------------------------------------------------------------

window = ThemedTk(theme="equilux")
MainWindow(window)
window.mainloop()


## - Execute procedure / Close Program:

