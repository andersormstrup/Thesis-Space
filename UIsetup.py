## - Imports for UI SETUP --
from tkinter import *   # For GUI creation.
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as font
import pandas as pd
import os
from shutil import copyfile
import subprocess as sub

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

        #Prompt Output
        #prom = sub.Popen('./MainPy.py',stdout=sub.PIPE,stderr=sub.PIPE)
        #output, errors = prom.communicate()


        # - Settings -------------
        self.xwidth = 350 # Billede Bredde  Ratio = 1:1 
        self.yhight = self.xwidth # Billede Højde
        self.borderx = 5 # Størrelse af Border omkring billeder
        self.Pad = 5 # Widget afstand i Grid.
        self.PictureHeading = font.Font(size = 16) #Navne over 
        self.ListHeadingFont = font.Font(size = 14) #Navne over 
        self.listboxhojde = 6 #Højde på resultat-listbox'es
        # VarionsDatabase
        self.MapName = r'Varationmap.xlsx'
        # - Reject MappeNavne
        self.reje1 = r'Reject1'
        self.reje2 = r'Reject2'
        self.reje3 = r'Reject3'

        ## billeder til indlæsning 
        self.image1 = ("ProgramLogo2.jpg")  
        self.image2 = ("ProgramLogo2.jpg")
        self.image3 = ("ProgramLogo2.jpg")

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
        self.list1 = Listbox(window, height=self.listboxhojde)
        self.list1.grid(row = 4, column = 1 , padx = self.Pad, pady = self.Pad)
        #LISTBOX CAM 2        
        self.textq2 = ttk.Label(text='Classes fra Cam 2')
        self.textq2['font'] = self.ListHeadingFont
        self.textq2.grid(row = 3, column = 2, padx = self.Pad, pady = self.Pad)
        self.list2 = Listbox(window, height=self.listboxhojde)
        self.list2.grid(row = 4, column = 2 , padx = self.Pad, pady = self.Pad)
        #LISTBOX CAM 3
        self.textq3 = ttk.Label(text='Classes fra Cam 2')
        self.textq3['font'] = self.ListHeadingFont
        self.textq3.grid(row = 3, column = 3, padx = self.Pad, pady = self.Pad)
        self.list3 = Listbox(window, height=self.listboxhojde)
        self.list3.grid(row = 4, column = 3 , padx = self.Pad, pady = self.Pad)
        #CommandLISTBOX 4
        #self.textq4 = ttk.Label(text='Classes fra Cam 2')
        #self.textq4['font'] = self.ListHeadingFont
        #self.textq4.grid(row = 3, column = 3, padx = self.Pad, pady = self.Pad)
        self.list4 = Listbox(window, height=4)
        self.list4.grid(row = 6, rowspan = 2, column = 1, columnspan = 2, padx = self.Pad, pady = self.Pad, sticky = NSEW)
        #self.list4.insert(END, *output)


        #DropDownMenu
        self.drop11 = ttk.Label(text = 'Vælg Variant')
        self.drop11['font']=self.ListHeadingFont
        self.drop11.grid(row = 6, column = 3, padx = self.Pad, pady = self.Pad)
        #self.Muligheder = ["EDJ FK06 2000", "EDJ MK04 0000", "EDJ MK06 0000", "EDJ MK06 2000"] # load fra fil istedet!
        self.MulighederData = pd.read_excel(self.MapName, header=None)
        self.Muligheder = self.MulighederData[0].tolist()
        self.varianter1 = StringVar(window)
        self.drop1 = ttk.OptionMenu(window, self.varianter1, *self.Muligheder, command = self.setVariant)
        #self.varianter1.set(self.Muligheder[2])
        self.drop1.grid(row = 7, column = 3, padx = self.Pad, pady = self.Pad, sticky = N)

        #KravLabels
        self.kravtext1 = ttk.Label(text='krav til cam 1')
        self.kravtext1['font'] = self.ListHeadingFont
        self.kravtext1.grid(row = 5, column = 1, padx = self.Pad, pady = self.Pad)
        self.kravtext2 = ttk.Label(text='krav til cam 1')
        self.kravtext2['font'] = self.ListHeadingFont
        self.kravtext2.grid(row = 5, column = 2, padx = self.Pad, pady = self.Pad)
        self.kravtext3 = ttk.Label(text='krav til cam 1')
        self.kravtext3['font'] = self.ListHeadingFont
        self.kravtext3.grid(row = 5, column = 3, padx = self.Pad, pady = self.Pad)

        self.Krav1 = []
        self.Krav2 = []
        self.Krav3 = []
    
    def setVariant(self, typex):
        index123 = self.Muligheder.index(typex)
        self.Krav1 = self.MulighederData[1][index123].split(",")
        self.kravtext1.config(text = self.Krav1)
        self.Krav2 = self.MulighederData[2][index123].split(",")
        self.kravtext2.config(text = self.Krav2)
        self.Krav3 = self.MulighederData[3][index123].split(",")
        self.kravtext3.config(text = self.Krav3)

    def SaveReje(self, img, path1, path2):
        Basepath = os.path.dirname(os.path.realpath(__file__)) #Få basepath i for program
        pathtosave = os.path.join(Basepath, path2) #Vælg undermappe til rejected img.
        head, tail = os.path.split(path1) # Split original, for at få filnavn. 
        name, ext = os.path.splitext(tail) # Split filnavnt for at tilføje til box img.
        newname = name + r'BOX' + ext # Til føj string i filnavn, så box img har anden navn.
        pathtocopyname = os.path.join(pathtosave, tail) #Navn på original, med box og ny sti.
        pathtosavename = os.path.join(pathtosave, newname) #Nyt navn på Originalen
        copyfile(path1, pathtocopyname) #Kopier originalen
        bil = img # img holder
        bil.save(pathtosavename) # gem boxed image.

    def OutUpdate(self, toprint):
        if int(self.list4.size()) > 40:
            self.list4.delete(0,END)
        self.list4.insert(END, toprint)
        self.list4.see("end")

    # Detect/Action 1-----------------
    def detection1(self, img1, detClasses, path):
        self.imgq1 = self.loadimgf2(img1) #2
        self.canvas1.itemconfig(self.img_canv1, image = self.imgq1)
        self.list1.delete(0,END)
        self.list1.insert(END, *detClasses)

        Err1 = False # Error state handler
        MissingList = [] #Missing component list
        self.list1['bg'] = '#009933'
        for krav in self.Krav1: # Sammenligning af krav og fundne classes
            try:
                detClasses.index(krav) # Tjekker om det fundne findes i krav.
                #print('Fandt korrekt krav ' + krav)
            except: # Case handler til fejlmelding.
                MissingList.append('MANGLER:')
                MissingList.append(krav)
                Err1 = True
                #print('Fandt IKK ' + krav)
        
        if Err1: #Action on Error/missing Components.
            print(MissingList)
            print("STOP")
            #self.kravtext1['background'] = '#cc0000'
            self.list1['bg'] = '#cc0000'
            self.list1.insert(END, *MissingList)
            self.SaveReje(img1, path, self.reje1)

    # Detect/Action 2-----------------
    def detection2(self, img2, detClasses, path):
        self.imgq2 = self.loadimgf2(img2) #2
        self.canvas2.itemconfig(self.img_canv2, image = self.imgq2)
        self.list2.delete(0,END)
        self.list2.insert(END, *detClasses)

        Err1 = False # Error state handler
        MissingList = [] #Missing component list
        self.list2['bg'] = '#009933'
        for krav in self.Krav2: # Sammenligning af krav og fundne classes
            try:
                detClasses.index(krav) # Tjekker om det fundne findes i krav.
                #print('Fandt korrekt krav ' + krav)
            except: # Case handler til fejlmelding.
                MissingList.append('MANGLER:')
                MissingList.append(krav)
                Err1 = True
                #print('Fandt IKK ' + krav)
        
        if Err1: #Action on Error/missing Components.
            print(MissingList)
            print("STOP")
            #self.kravtext1['background'] = '#cc0000'
            self.list2['bg'] = '#cc0000'
            self.list2.insert(END, *MissingList)
            self.SaveReje(img2, path, self.reje2)


    # Detect/Action 3-----------------
    def detection3(self, img3, detClasses, path):
        self.imgq3 = self.loadimgf2(img3)
        self.canvas3.itemconfig(self.img_canv3, image = self.imgq3)
        self.list3.delete(0,END)
        self.list3.insert(END, *detClasses)

        Err1 = False # Error state handler
        MissingList = [] #Missing component list
        self.list3['bg'] = '#009933'
        for krav in self.Krav3: # Sammenligning af krav og fundne classes
            try:
                detClasses.index(krav) # Tjekker om det fundne findes i krav.
                #print('Fandt korrekt krav ' + krav)
            except: # Case handler til fejlmelding.
                MissingList.append('MANGLER:')
                MissingList.append(krav)
                Err1 = True
                #print('Fandt IKK ' + krav)
        
        if Err1: #Action on Error/missing Components.
            print(MissingList)
            print("STOP")
            #self.kravtext1['background'] = '#cc0000'
            self.list3['bg'] = '#cc0000'
            self.list3.insert(END, *MissingList)
            self.SaveReje(img3, path, self.reje3)
