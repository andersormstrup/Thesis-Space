## - Imports for UI SETUP --
from tkinter import *   # For GUI creation.
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as font

class MainWindow():

    # Load & Resize img funktion.
    def loadimgf(self, inputimg):
        imgx = Image.open(inputimg)
        imgxre = imgx.resize((self.xwidth, self.yhight), Image.ANTIALIAS)
        return ImageTk.PhotoImage(imgxre)

    # Load & Resize img funktion.
    def loadimgf2(self, inputimg):
        # imgx = Image.open(inputimg)
        imgx = inputimg
        imgxre = imgx.resize((self.xwidth, self.yhight), Image.ANTIALIAS)
        return ImageTk.PhotoImage(imgxre)


    # -----------------------
    def __init__(self, window): #, deep):
        window['bg'] = '#464646'
        #window['bg'] = '#6a6a6a'


        window.title('Vision Kontrol Linje 4')
        window.geometry("1250x650")
        #window.attributes('-fullscreen', True)
        #window.state('zoomed')
        window.iconbitmap(r'veluxlogo.ico') # Window icon

        #StopKnap
        self.button1 = ttk.Button(window, text='Stop', width=25, command=window.destroy)  # Opret knap i root.
        self.button1.grid(row = 8, column = 8, sticky = S)            # Placering af knap. 



        # - Settings
        self.xwidth = 320 # Billede Bredde  Ratio = 1:1 
        self.yhight = self.xwidth # Billede Højde
        self.borderx = 5 # Størrelse af Border omkring billeder
        self.Pad = 5 # Widget afstand i Grid.
        self.PictureHeading = font.Font(size = 16) #Navne over 
        self.ListHeadingFont = font.Font(size = 14) #Navne over 

        

        ## billeder til indlæsning 
        self.image1 = ("22.jpeg")  
        self.image2 = ("22.jpeg")
        self.image3 = ("22.jpeg")

        self.det3img = ("13.jpeg")




        # - Billede 1
        self.photo1 = self.loadimgf(self.image1) # Load and resize
        self.canvas1 = Canvas(window, width = self.xwidth+self.borderx, height = self.yhight+self.borderx)
        self.text1 = ttk.Label(text='Camera 1')
        self.text1['font'] = self.PictureHeading
        self.text1.grid(row = 1, column = 1, padx = self.Pad, pady = self.Pad)
        self.canvas1.grid(row = 2, column = 1, padx = self.Pad, pady = self.Pad)
        self.img_canv1 = self.canvas1.create_image(self.borderx, self.borderx, anchor = NW, image = self.photo1) #Set Image on Canvas 1.
        # - Billede 2
        self.photo2 = self.loadimgf(self.image2) # Load and resize
        self.canvas2 = Canvas(window, width = self.xwidth+self.borderx, height = self.yhight+self.borderx)
        self.text2 = ttk.Label(text='Camera 2')
        self.text2['font'] = self.PictureHeading
        self.text2.grid(row = 1, column = 2, padx = self.Pad, pady = self.Pad)
        self.canvas2.grid(row = 2, column = 2, padx = self.Pad, pady = self.Pad)
        self.img_canv2 = self.canvas2.create_image(self.borderx, self.borderx, anchor = NW, image = self.photo2) #Set Image on Canvas 2.
        # - Billede 3
        self.photo3 = self.loadimgf(self.image3) # Load and resize
        self.canvas3 = Canvas(window, width = self.xwidth+self.borderx, height = self.yhight+self.borderx)
        self.text3 = ttk.Label(text='Camera 3')
        self.text3['font'] = self.PictureHeading
        self.text3.grid(row = 1, column = 3, padx = self.Pad, pady = self.Pad)
        self.canvas3.grid(row = 2, column = 3, padx = self.Pad, pady = self.Pad)
        self.img_canv3 = self.canvas3.create_image(self.borderx, self.borderx, anchor = NW, image = self.photo3) #Set Image on Canvas 3.



        # # Detect1 Knap
        # self.button2 = ttk.Button(window, text='Detect1', width=20, command=self.detection1)
        # self.button2.grid(row = 8, column = 1)
        # # Detect2 Knap
        # self.button3 = ttk.Button(window, text='Detect2', width=20, command=self.detection2)
        # self.button3.grid(row = 8, column = 2)
        # # Detect2 Knap
        # self.button4 = ttk.Button(window, text='Detect3', width=20, command=self.detection3)
        # self.button4.grid(row = 8, column = 3)


        #LISTBOX CAM 1
        self.textq1 = ttk.Label(text='Classes fra Cam 1')
        self.textq1['font'] = self.ListHeadingFont
        self.textq1.grid(row = 3, column = 1, padx = self.Pad, pady = self.Pad)
        self.list1 = Listbox(window)
        self.list1.grid(row = 4, column = 1 , padx = self.Pad, pady = self.Pad)
        #LISTBOX CAM 2        
        self.textq2 = ttk.Label(text='Classes fra Cam 2')
        self.textq2['font'] = self.ListHeadingFont
        self.textq2.grid(row = 3, column = 2, padx = self.Pad, pady = self.Pad)
        self.list2 = Listbox(window)
        self.list2.grid(row = 4, column = 2 , padx = self.Pad, pady = self.Pad)
        #LISTBOX CAM 3
        self.textq3 = ttk.Label(text='Classes fra Cam 2')
        self.textq3['font'] = self.ListHeadingFont
        self.textq3.grid(row = 3, column = 3, padx = self.Pad, pady = self.Pad)
        self.list3 = Listbox(window)
        self.list3.grid(row = 4, column = 3 , padx = self.Pad, pady = self.Pad)


    # Detect/Action 1-----------------
    def detection1(self, img1, detClasses):
        self.imgq1 = self.loadimgf2(img1) #2
        self.canvas1.itemconfig(self.img_canv1, image = self.imgq1)
        self.list1.delete(0,END)
        self.list1.insert(END, *detClasses)

    # Detect/Action 2-----------------
    def detection2(self, img2, detClasses):
        self.imgq2 = self.loadimgf2(img2) #2
        self.canvas2.itemconfig(self.img_canv2, image = self.imgq2)
        self.list2.delete(0,END)
        self.list2.insert(END, *detClasses)




    # Detect/Action 3-----------------
    def detection3(self, img3):
        self.imgq3 = self.loadimgf(img3)
        self.canvas3.itemconfig(self.img_canv3, image = self.imgq3)