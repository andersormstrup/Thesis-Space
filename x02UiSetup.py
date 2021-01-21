## - Imports for UI SETUP --
from tkinter import *           # For GUI creation.
from PIL import Image, ImageTk  # Handling of Image on UI.
from tkinter import ttk         # Base TTK import.
from ttkthemes import ThemedTk  # For Themed UI's.
import tkinter.font as font     # Special Fonts.
import pandas as pd             # For data calculations.
import os                       # To handle os paths.
from shutil import copyfile     # CopyFile Functions.
import subprocess as sub        # To create lower prio tasks.

class MainWindow():

    # Load & Resize img funktion 1.
    def loadimgf(self, inputimg):
        imgx = Image.open(inputimg)
        imgxre = imgx.resize((self.xwidth, self.yhight), Image.ANTIALIAS)
        return ImageTk.PhotoImage(imgxre)

    # Load & Resize img funktion 2.
    def loadimgf2(self, inputimg):
        imgx = inputimg
        imgxre = imgx.resize((self.xwidth, self.yhight), Image.ANTIALIAS)
        return ImageTk.PhotoImage(imgxre)

    def __init__(self, window): # Runs only once!
        window['bg'] = '#464646' # UI background color.
            #Setup for UI
        window.title('Vision Kontrol Linje 4')
        window.geometry("1250x650")
        window.state('zoomed')
        window.iconbitmap(r'veluxlogo.ico') # Window icon
                # - Execute procedure / Close Program: #Stopbutton.
        self.button1 = ttk.Button(window, text='Stop', width=25, command=window.destroy)
        self.button1.grid(row = 1, column = 3, sticky = E) # Placement of Stop button.
        # - Settings -------------
        self.xwidth = 500               # Image widths-> Ratio = 1:1 
        self.yhight = self.xwidth       # Widht = hight.
        self.borderx = 5                # Size of border for images.
        self.Pad = 5                    # Widget distance in grid (px).
        self.PictureHeading = font.Font(size = 16) #Font sice for names ABOVE.
        self.ListHeadingFont = font.Font(size = 14) #Font sice for Listbox. 
        self.listboxhojde = 6           #Højde på resultat-listbox'es
        # VariationonsDatabase
        self.MapName = r'Varationmap.xlsx'
        # - Reject folder names
        self.reje1 = r'Reject1'
        self.reje2 = r'Reject2'
        self.reje3 = r'Reject3'
        ## Pictures to load on startUp. 
        self.image1 = ("ProgramLogo2.jpg")  
        self.image2 = ("ProgramLogo2.jpg")
        self.image3 = ("ProgramLogo2.jpg")
        # - Image 1 Creation.
        self.photo1 = self.loadimgf(self.image1) # Load and resize
        self.canvas1 = Canvas(window, width = self.xwidth+self.borderx, height = self.yhight+self.borderx)
        self.text1 = ttk.Label(text='Camera 1')
        self.text1['font'] = self.PictureHeading
        self.text1.grid(row = 1, column = 1, padx = self.Pad, pady = self.Pad)
        self.canvas1.grid(row = 2, column = 1, padx = self.Pad, pady = self.Pad)
        #Set Image on Canvas 1.
        self.img_canv1 = self.canvas1.create_image(self.borderx, self.borderx, anchor = NW, image = self.photo1) 
        # - Image 2 Creation.
        self.photo2 = self.loadimgf(self.image2) # Load and resize
        self.canvas2 = Canvas(window, width = self.xwidth+self.borderx, height = self.yhight+self.borderx)
        self.text2 = ttk.Label(text='Camera 2')
        self.text2['font'] = self.PictureHeading
        self.text2.grid(row = 1, column = 2, padx = self.Pad, pady = self.Pad)
        self.canvas2.grid(row = 2, column = 2, padx = self.Pad, pady = self.Pad)
        #Set Image on Canvas 2.
        self.img_canv2 = self.canvas2.create_image(self.borderx, self.borderx, anchor = NW, image = self.photo2) 
        # - Image 3 Creation.
        self.photo3 = self.loadimgf(self.image3) # Load and resize
        self.canvas3 = Canvas(window, width = self.xwidth+self.borderx, height = self.yhight+self.borderx)
        self.text3 = ttk.Label(text='Camera 3')
        self.text3['font'] = self.PictureHeading
        self.text3.grid(row = 1, column = 3, padx = self.Pad, pady = self.Pad)
        self.canvas3.grid(row = 2, column = 3, padx = self.Pad, pady = self.Pad)
        #Set Image on Canvas 3.
        self.img_canv3 = self.canvas3.create_image(self.borderx, self.borderx, anchor = NW, image = self.photo3) 

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
        self.textq3 = ttk.Label(text='Classes fra Cam 3')
        self.textq3['font'] = self.ListHeadingFont
        self.textq3.grid(row = 3, column = 3, padx = self.Pad, pady = self.Pad)
        self.list3 = Listbox(window, height=self.listboxhojde)
        self.list3.grid(row = 4, column = 3 , padx = self.Pad, pady = self.Pad)
        
        # Program output as Listbox, bottom of UI.
        self.list4 = Listbox(window, height=4)
        self.list4.grid(row = 6, rowspan = 2, column = 1, columnspan = 2, padx = self.Pad, pady = self.Pad, sticky = NSEW)

        # DropDownMenu For variant selection.
        self.drop11 = ttk.Label(text = 'Vælg Variant')
        self.drop11['font']=self.ListHeadingFont
        self.drop11.grid(row = 6, column = 3, padx = self.Pad, pady = self.Pad)
        self.VariationData = pd.read_excel(self.MapName, header=None)
        self.OptionsX = self.VariationData[0].tolist()
        self.varianter1 = StringVar(window)
        self.drop1 = ttk.OptionMenu(window, self.varianter1, *self.OptionsX, command = self.setVariant)
        self.drop1.grid(row = 7, column = 3, padx = self.Pad, pady = self.Pad, sticky = NSEW)

        # Requirement labes, from variation selection.
        self.Requirementtext1 = ttk.Label(text='Krav til cam 1')
        self.Requirementtext1['font'] = self.ListHeadingFont
        self.Requirementtext1.grid(row = 5, column = 1, padx = self.Pad, pady = self.Pad)
        self.Requirementtext2 = ttk.Label(text='Krav til cam 2')
        self.Requirementtext2['font'] = self.ListHeadingFont
        self.Requirementtext2.grid(row = 5, column = 2, padx = self.Pad, pady = self.Pad)
        self.Requirementtext3 = ttk.Label(text='Krav til cam 3')
        self.Requirementtext3['font'] = self.ListHeadingFont
        self.Requirementtext3.grid(row = 5, column = 3, padx = self.Pad, pady = self.Pad)
        # Allocate empty on startup. 
        self.Requirement1 = []
        self.Requirement2 = []
        self.Requirement3 = []
    
    # Load variation from EXCEL file onto dropdown menu. 
    def setVariant(self, typex):
        indexOptions = self.OptionsX.index(typex)
        self.Requirement1 = self.VariationData[1][indexOptions].split(",")
        self.Requirementtext1.config(text = self.Requirement1)
        self.Requirement2 = self.VariationData[2][indexOptions].split(",")
        self.Requirementtext2.config(text = self.Requirement2)
        self.Requirement3 = self.VariationData[3][indexOptions].split(",")
        self.Requirementtext3.config(text = self.Requirement3)

    # Save rejected images function.
    def SaveReje(self, img, path1, path2):
        Basepath = os.path.dirname(os.path.realpath(__file__)) # get basepath for program.
        pathtosave = os.path.join(Basepath, path2)  # Choose path to save rejected img.
        head, tail = os.path.split(path1)           # Split originalpath, to get filename. 
        name, ext = os.path.splitext(tail)          # Split filename to add "box".
        newname = name + r'BOX' + ext
        pathtocopyname = os.path.join(pathtosave, tail)    #Name of original, with box and new path.
        pathtosavename = os.path.join(pathtosave, newname) #New name for Originalen.
        copyfile(path1, pathtocopyname)             #copy originalen.
        bil = img                                   # img holder.
        bil.save(pathtosavename)                    # save boxed image.

    # Update function for program Output.
    def OutUpdate(self, toprint):
        if int(self.list4.size()) > 40:
            self.list4.delete(0,END)
        self.list4.insert(END, toprint)
        self.list4.see("end")

    # Detect/Action for camera 1 Function.
    def detection1(self, img1, detClasses, path):
        self.imgq1 = self.loadimgf2(img1) #2 Resize and display.
        self.canvas1.itemconfig(self.img_canv1, image = self.imgq1)
        self.list1.delete(0,END)
        self.list1.insert(END, *detClasses) # Show found classes.

        Err1 = False         # Error state handler
        MissingList = []     # Missing component list
        self.list1['bg'] = '#009933'  # Green
        # Compare requirements with detected.
        for Requirement in self.Requirement1: 
            try:
                detClasses.index(Requirement) # Checking reqirements.
            except:         # Case handler for missing.
                MissingList.append('MANGLER:')
                MissingList.append(Requirement)
                Err1 = True
        if Err1:            #Action on Error/missing Components.
            print(MissingList)
            print("STOP")
            self.list1['bg'] = '#cc0000'
            self.list1.insert(END, *MissingList)
            self.SaveReje(img1, path, self.reje1)

    # Detect/Action for camera 2 Function.
    def detection2(self, img2, detClasses, path):
        self.imgq2 = self.loadimgf2(img2)  #2 Resize and display.
        self.canvas2.itemconfig(self.img_canv2, image = self.imgq2)
        self.list2.delete(0,END)
        self.list2.insert(END, *detClasses) # Show found classes.

        Err1 = False        # Error state handler
        MissingList = []    #Missing component list
        self.list2['bg'] = '#009933'
        # Compare requirements with detected.
        for Requirement in self.Requirement2:
            try:
                detClasses.index(Requirement) # Checking reqirements.
            except:         # Case handler for missing.
                MissingList.append('MANGLER:')
                MissingList.append(Requirement)
                Err1 = True
        if Err1:            #Action on Error/missing Components.
            print(MissingList)
            print("STOP")
            self.list2['bg'] = '#cc0000'
            self.list2.insert(END, *MissingList)
            self.SaveReje(img2, path, self.reje2)

    # Detect/Action for camera 2 Function.
    def detection3(self, img3, detClasses, path):
        self.imgq3 = self.loadimgf2(img3) #2 Resize and display.
        self.canvas3.itemconfig(self.img_canv3, image = self.imgq3)
        self.list3.delete(0,END)
        self.list3.insert(END, *detClasses) # Show found classes.

        Err1 = False        # Error state handler
        MissingList = []    #Missing component list
        self.list3['bg'] = '#009933'
        # Compare requirements with detected.
        for Requirement in self.Requirement3:
            try:
                detClasses.index(Requirement) # Checking reqirements.
            except:         # Case handler for missing.
                MissingList.append('MANGLER:')
                MissingList.append(Requirement)
                Err1 = True
        if Err1:            #Action on Error/missing Components.
            print(MissingList)
            print("STOP")
            self.list3['bg'] = '#cc0000'
            self.list3.insert(END, *MissingList)
            self.SaveReje(img3, path, self.reje3)
