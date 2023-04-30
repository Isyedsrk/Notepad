from tkinter import *
import tkinter .messagebox as tmsg
from tkinter .filedialog import askopenfilename,asksaveasfilename
import os



root=Tk()

def ext():
    root.destroy()

def new():
    global file
    root.title("Untitled-Notepad")
    file=None
    textarea.delete(1.0,END)


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("all files","*.*",),("Text Documents","*.txt")])
        if file == "":
            file = None

        else:
            f = open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"- Notepad")
            print("file saved")
    else:
     f = open(file, "w")
     f.write(textarea.get(1.0, END))
     f.close()

def saveas():
    pass

def openn():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("all files","*.*",),("Text Documents","*.txt")])
    if file =="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
    textarea.delete(1.0,END)
    f =open(file,"r")
    textarea.insert(1.0,f.read())
    f.close()


def printt():
    pass

def cut():
    textarea.event_generate("<<Cut>>")

def copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")

def delete():
    pass

def find():
    pass

def word():
    pass

def font():
    pass

def zoom():
    pass

def status():
    pass

def views():
    pass

def feedback():
    pass

def about():
    tmsg.showinfo("Notepad","This text editor is created by SYED")



root.geometry("550x440")
root.title("Untitled-Notepad")
root.wm_iconbitmap("1.ico")

#Menubar
menubar = Menu(root,)

#textarea

textarea = Text(root,font="lucida 13")
textarea.pack(expand= True, fill=BOTH)

#Adding scrollbar

scroll = Scrollbar(textarea)
scroll.pack(side=RIGHT,fil=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)


#file option
file = Menu(menubar,tearoff=0,)
file.add_command(label="New",command=new)
file.add_command(label="Save",command=save)
file.add_command(label="Save as",command=saveas)
file.add_command(label="Open",command=openn)
file.add_command(label="Exit",command=ext)

#edit option

edit = Menu(menubar,tearoff=0)
edit.add_command(label="Cut",command=cut)
edit.add_command(label="Copy",command=copy)
edit.add_command(label="Paste",command=paste)
edit.add_command(label="Delete",command=delete)
edit.add_command(label="Find",command=find)

#format option

format = Menu(menubar,tearoff=0)
format.add_command(label="Word wrap",command=word)
format.add_command(label="Font...",command=font)

#view option

view = Menu(menubar,tearoff=0)
view.add_command(label="Zoom",command=zoom)
view.add_command(label="Status bar",command=status)

#help option

help = Menu(menubar,tearoff=0)
help.add_command(label="View Help",command=views)
help.add_command(label="Send Feedback",command=feedback)
help.add_command(label="About notepad",command=about)



#adding of menu options

root.configure(menu=menubar)
menubar.add_cascade(label="File",menu=file)
menubar.add_cascade(label="Edit",menu=edit)
menubar.add_cascade(label="Format",menu=format)
menubar.add_cascade(label="View",menu=view)
menubar.add_cascade(label="Help",menu=help)





root.mainloop()
