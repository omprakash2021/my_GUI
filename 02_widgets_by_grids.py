from tkinter import *
root = Tk()
# Ceating a lable widget
#alternate way of griding of lables
myLable1 = Label(root,text='Hello World!').grid(row=0,column=0)
myLable3 = Label(root,text='               ').grid(row=1,column=1)
myLable2 = Label(root,text='This is my PC').grid(row=1,column=5)
#shoving it into the screen by grid(coordinate system)
# myLable1.grid(row=0,column=0)
# myLable2.grid(row=1,column=5)
# myLable3.grid(row=1,column=1)

root.mainloop()