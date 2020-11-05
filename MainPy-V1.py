## - Main Python script to run on machine. 



## - Imports for all scripts --
from tkinter import *   # For GUI creation.
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as font
#import keyboard

#------------------------------------------------------------------------------------

## - Functions


class MainWindow():

    # -----------------------
    def __init__(self, window):
        window['bg'] = '#464646'
        #window['bg'] = '#6a6a6a'


        window.title('Vision Kontrol Linje 4')
        window.geometry("700x600")
        #window.attributes('-fullscreen', True)
        window.state('zoomed')
        window.iconbitmap(r'veluxlogo.ico') # Window icon

        #StopKnap
        self.button1 = ttk.Button(window, text='Stop', width=25, command=window.destroy)  # Opret knap i root.
        self.button1.grid(row = 8, column = 8, sticky = S)            # Placering af knap. 



        # - Settings
        self.xwidth = 350 # Billede Bredde  Ratio = 1:1 
        self.yhight = self.xwidth # Billede Højde
        self.borderx = 5 # Størrelse af Border omkring billeder
        self.Pad = 5 # Widget afstand i Grid.
        self.PictureHeading = font.Font(size = 22)

        ## billeder til indlæsning 
        self.image1 = Image.open("22.jpeg")  
        self.image2 = Image.open("22.jpeg")
        self.image3 = Image.open("22.jpeg")
        
        self.det3img = ("13.jpeg")

        # - Billede 1
        self.imagex1 = self.image1.resize((self.xwidth,self.yhight), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.imagex1)
        self.canvas1 = Canvas(window, width = self.xwidth+self.borderx, height = self.yhight+self.borderx)
        self.text1 = ttk.Label(text='Camera 1')
        self.text1['font'] = self.PictureHeading
        self.text1.grid(row = 1, column = 1, padx = self.Pad, pady = self.Pad)
        self.canvas1.grid(row = 2, column = 1, padx = self.Pad, pady = self.Pad)
        self.img_canv1 = self.canvas1.create_image(self.borderx, self.borderx, anchor = NW, image = self.photo1) #Set Image on Canvas 1.
        # - Billede 2
        self.imagex2 = self.image2.resize((self.xwidth,self.yhight), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.imagex2)
        self.canvas2 = Canvas(window, width = self.xwidth+self.borderx, height = self.yhight+self.borderx)
        self.text2 = ttk.Label(text='Camera 2')
        self.text2['font'] = self.PictureHeading
        self.text2.grid(row = 1, column = 2, padx = self.Pad, pady = self.Pad)
        self.canvas2.grid(row = 2, column = 2, padx = self.Pad, pady = self.Pad)
        self.img_canv2 = self.canvas2.create_image(self.borderx, self.borderx, anchor = NW, image = self.photo2) #Set Image on Canvas 2.
        # - Billede 2
        self.imagex3 = self.image3.resize((self.xwidth,self.yhight), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(self.imagex3)
        self.canvas3 = Canvas(window, width = self.xwidth+self.borderx, height = self.yhight+self.borderx)
        self.text3 = ttk.Label(text='Camera 3')
        self.text3['font'] = self.PictureHeading
        self.text3.grid(row = 1, column = 3, padx = self.Pad, pady = self.Pad)
        self.canvas3.grid(row = 2, column = 3, padx = self.Pad, pady = self.Pad)
        self.img_canv3 = self.canvas3.create_image(self.borderx, self.borderx, anchor = NW, image = self.photo3) #Set Image on Canvas 3.


        self.button2 = ttk.Button(window, text='Detect', width=10, command=self.detection)
        self.button2.grid(row = 8, column = 7)
        
    # Detect/Action -----------------
    def detection(self):
        self.image3new = Image.open(self.det3img)
        self.imagexnew = self.image3new.resize((self.xwidth,self.yhight), Image.ANTIALIAS)
        self.photoNew = ImageTk.PhotoImage(self.imagexnew)
        self.canvas3.itemconfig(self.img_canv3, image = self.photoNew)







## - Main Loop -------------------------------------------------------------------------------

window = ThemedTk(theme="equilux")
MainWindow(window)
window.mainloop()


## - Execute procedure / Close Program:

