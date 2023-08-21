
import pyautogui # module used for the screenshot
import tkinter as tk
from tkinter.filedialog import *


# the UI OF THE SCREEN
root = tk.Tk()
root.geometry('320x200+350+100') # the size of the window width * height + x + y
root.configure(background='teal')
root.title('Screenshot App')# title of the window

#windows of the screen 
# canvas1 = tk.Canvas(root, height= 300, width=300,background='pink', )
text_show = tk.Label(root,text='Welcome, I\'m your screenshot app,\n kindly click on the button below \nto take a screenshot',bg='teal', font=('sans-serif',12),fg='white')
# canvas1.pack()
text_show.pack(pady=15)

#screenshot function
def takeScreenshot():
    '''function to take screenshot  '''
    myscreen = pyautogui.screenshot()
    # asking the user the name file should be saved as 
    save_path = asksaveasfilename()
    myscreen.save(save_path+'_screenshot.png')

#button
myButton = tk.Button(root,text="Click to take a screenshot ", command=takeScreenshot, font=10,bg='wheat',activebackground='yellow')
myButton.pack(pady=25)
root.mainloop()