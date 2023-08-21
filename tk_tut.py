from tkinter import *

root = Tk() # creating a main window

# creating a widget
my_label = Label(root,text='hello world')
my_label2 = Label(root,text='hello world,i am using the grid system')

#adding the widget into the screen
my_label.grid(row=0,column=1)
#grid with attributes of row and column
my_label2.grid(row=0,column=4)


# creating a widget and placing in on the screen
my_label3 = Label(root,text='hello world').grid(row=0,column=2)

my_label4 = Label(root,text='hello world,i am using the grid system').grid(row=0,column=3)


## creating a function for click command 
def myclick():
    my_label= Label(root,text='i HAVE BEING CLICKED')
    my_label.grid(column=4)

def my_entry():
    my_label2= Label(root,text='hello '+e.get().split(':')[-1])
    my_label2.grid(column=4)

#creating a button
myButton = Button(root,text='click me',padx=20,pady=20,command=my_entry,fg='green',bg='black',font=10).grid(row=2,column=4)

# creating an input box
e = Entry(root,width=50,bg='black',borderwidth=5,fg='white')
e.insert(0,'Enter your name : ')
e.grid(row=1,column=4)














#to run the program continuously
root.mainloop()