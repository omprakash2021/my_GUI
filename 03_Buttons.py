from tkinter import *
root = Tk()

# myButton = Button(root,text = "Click me!",state = DISABLED)
# myButton = Button(root,text = "Click me!",padx=40,pady=30) #resizing the button
'''let's define a function that will dipict into our screen by clicking button'''
def myClick():
    myLable = Label(root,text="Oooh!,You have clicked the button!")
    myLable.pack()
myButton = Button(root,text="Click me!",command=myClick,fg='green',bg='#000000') #button's foreground(fg) color,bg(background)
myButton.pack()

root.mainloop()