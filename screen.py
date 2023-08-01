
import pyautogui # module used for the screenshot
import tkinter as tk
from tkinter.filedialog import *


# the UI OF THE SCREEN
root = tk.Tk()

#windows of the screen 
canvas1 = tk.Canvas(root, height= 300, width=300,)
canvas1.pack()

#screenshot function
def takeScreenshot():
    '''function to take screenshot  '''
    myscreen = pyautogui.screenshot()
    # asking the user the name file should be saved as 
    save_path = asksaveasfilename()
    myscreen.save(save_path+'_screenshot.png')

#button
myButton = tk.Button(text="Click to take a screenshot ", command=takeScreenshot, font=10)
canvas1.create_window(150,150,window=myButton)
tk.mainloop()