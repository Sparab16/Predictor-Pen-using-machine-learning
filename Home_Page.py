from tkinter import *
from os import system
from subprocess import call


def quit_loop():
    global selection
    selection = var.get()
    master.destroy()
    if selection == 1:

        print("Machine Learning Mode selected")
        # system('python ./MachineLearningMode.py')
        # import MachineLearningMode
        call(['python','MachineLearningMode.py'])
    else:

        print("Free Hand Mode selected")
        # system('python ./FreeHandMode.py')
        import FreeHandMode




master = Tk()
master.geometry("300x300+500+200")
master.title("Predictor Pen")

# Label for choosing between Machine Learning mode or Free hand mode
choose_label = Label(master, text='Choose the Mode',font=("Google Sans",20),padx=10,pady=10).pack()


# Radiobutton for choosing between two modes
var = IntVar()
var.set(1)
radioButton_ML = Radiobutton(master, text='Machine Learning Mode', variable=var,value=1,font=("Google Sans",10),padx=10,pady=10).pack()
radioButton_FH = Radiobutton(master, text='Free Hand Mode', variable=var,value=2,font=("Google Sans",10),padx=10,pady=10).pack()



# Button for selecting Mode
button = Button(master,text='Select',command=quit_loop,bd=3,pady=10).pack()




if __name__ == '__main__':
    master.mainloop()

print("END OF HOMEPAGE")