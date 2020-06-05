from Tkinter import *
root1=Tk()
root1.title("Information")
Label(root1).grid(row=0,column=1)
Label(root1,text="PHONEBOOK PROJECT",font='times 20 bold italic',fg='blue').grid(row=1,column=1)
Label(root1,text="Project of Python and Database",font='times 15 bold').grid(row=3,column=6)
Label(root1,text="Developed by: Abhishek Gupta(181B009)",font='times 14 bold italic',fg='light green').grid(row=4,column=6)
def kill(*args):
    root1.destroy()
root1.bind('<Motion>',kill)
root1.geometry('700x650')

mainloop()


