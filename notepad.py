from Tkinter import *
from tkFileDialog import *
import ConfigParser
import Tkinter

config = ConfigParser.ConfigParser()
config.read('config')
filename = "temp.txt"



class Prompt:
    def button_action(self):
        self.find = self.ent.get() #this is the variable I wanna use in another function
        self.replace = self.ent1.get() #this is the variable I wanna use in another function
        findAndReplace(self.find,self.replace);
        self.destroy();

    def __init__(self, den):
        self.lbl = Tkinter.Label(den, text="Find")
        self.ent = Tkinter.Entry(den)
        self.lbl1 = Tkinter.Label(den, text="Replace")
        self.ent1 = Tkinter.Entry(den)
        self.btn = Tkinter.Button(den, text="Find and Replace", command=self.button_action)
        self.lbl.pack()
        self.ent.pack()
        self.lbl1.pack()
        self.ent1.pack()
        self.btn.pack()

####################### Editor APIs ########################
def newFile():
    text.delete(0.0, END)


def saveFile():
    root.title(filename)
    t = text.get(0.0, END)
    f = open(filename, "w+")
    f.write(t)
    f.close()


def saveAs():
    f = asksaveasfile(mode = 'w', confirmoverwrite ='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="ERROR",message="Unable to save file...")


def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text = text.delete(0.0, END)
    text.insert(0.0,t)


def findAndReplace(findFor, replaceWith):
    t = text.get(0.0, END)
    txt = t;
    text.delete(0.0, END)
    txt = txt.replace(findFor,replaceWith);
    print txt.find(findFor)
    text.insert(0.0,txt);


def findAndReplaceRecursively():
    den = Tkinter.Tk()
    den.title("Widget Example")
    prompt = Prompt(den)
    st = den.mainloop()
    print st
    t = text.get(0.0, END)
    print t

def findString():
    print "Comming soon Find"



####################### Editor Configuration  ########################
root = Tk()
def decorateWindow(input_width, input_height):
    root.title("New File")
    root.minsize(width=input_width,height=input_height)
    root.maxsize(width=input_width,height=input_height)

def placeMenubar():
    menubar = Menu(root)
    filemenu = Menu(menubar)
    filemenu.add_command(label="New",command=newFile)
    filemenu.add_command(label="Open",command=openFile)
    filemenu.add_command(label="Save",command=saveFile)
#   filemenu.add_command(label="Save as..",command=saveAs)
    filemenu.add_separator()
    filemenu.add_command(label="Find", command =findString)
    filemenu.add_command(label="Find & Replace", command =findAndReplace)
    filemenu.add_command(label="Find & Replace Recursively", command =findAndReplaceRecursively)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command = root.quit)
    menubar.add_cascade(label="File",menu=filemenu)
    root.config(menu=menubar)



functionKeyBind = {
        '\x13' : saveFile,
        '\x11' : root.quit,
        '\x06' : findString,
        'asdsad`' : findAndReplace,
        '\x12' : findAndReplaceRecursively,
        '\x0e' : newFile
}

def keyEventListner(event):
    print "pressed", repr(event.char)
    if(event.char in functionKeyBind):
        functionKeyBind[event.char]()



####################### Parser Configuration  ########################

input_width_window = config.get('Window','width')
input_height_window = config.get('Window','height')

input_width_text = config.get('TextArea','width')
input_height_text = config.get('TextArea','height')

#other_windows_width =

####################### Text Configuration  ########################
text = Text(width=input_width_text,height=input_height_text)
text.bind("<Key>", keyEventListner)
text.pack()

decorateWindow(input_width_window,input_height_window)
placeMenubar()
root.mainloop()
newFile()






