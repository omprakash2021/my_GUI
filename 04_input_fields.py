from tkinter import *

root = Tk()

# e = Entry(root,width =50,bg='grey',fg='orange',borderwidth=50)  #it will make text box for getting text from user
e = Entry(root,width =50)
e.pack()
e.insert(0,"Enter your name: ") # it will already show text inside the Entry box
# e.get() #it will take input from to print

def myClick() :
    # myLable = Label(root,text="Hello " + e.get()) or below
    hello ="Hello " + e.get()
    myLable = Label(root,text=hello)
    myLable.pack()

myButton = Button(root,text= "Enter Your Name",command = myClick)
myButton.pack()

root.mainloop()