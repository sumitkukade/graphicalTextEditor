from Tkinter import *
from tkFileDialog import *
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config')
filename = "temp.txt"



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

def findAndReplace():
    t = text.get(0.0, END)
    root = Tk()
    find = Text(root, height=2, width=30)
    find.pack()
    find.get()
    mainloop()
    print find
    print t


def findAndReplaceRecursively():
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
        '\x17' : findAndReplaceRecursively,
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
