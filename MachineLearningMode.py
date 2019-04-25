from tkinter import *
import socket
import threading
from subprocess import call

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
print("Connecting Established")

class ThreadedTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            letter = s.recv(1024).decode()
            text_area.insert(INSERT,letter)

def activate():
        text_area.config(state=NORMAL)
        ThreadedTask().start()

def deactivate():
    text_area.config(state=DISABLED)

def clear():
    '''
    Deletes the content of textBox
    :return: Null
    '''
    text_area.config(state=NORMAL)
    text_area.delete('1.0',END)

def save():
    pass

def freeHandMode():
    call(['python','FreeHandMode.py'])

master = Tk()
master.geometry("500x500+500+200")
master.title("Machine Learning Mode")


#----------------- CODE FOR CREATING MENU -------------->
menubar = Menu(master)
# File Menu
file_menu = Menu(master)
# file_menu.add_command(label='Save as ',command=save)
file_menu.add_command(label='Clear', command=clear)
menubar.add_cascade(label='File', menu=file_menu)
master.config(menu=menubar)

#-------------------- CODE FOR ENTRY -------------------->
text_area  = Text(master,state=DISABLED,font=("Google Sans",15))
text_area.pack()


# Button for selecting Mode
button1 = Button(master,text='Activate',command=activate,bd=3,pady=10).pack()
button2 = Button(master,text='Deactivate',command=deactivate,bd=3,pady=10).pack()
button3 = Button(master,text='Free Hand Mode' ,command=freeHandMode,bd=3,pady=10).pack()

master.mainloop()
