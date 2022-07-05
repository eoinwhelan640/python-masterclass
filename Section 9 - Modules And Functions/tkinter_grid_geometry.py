import tkinter


# this is a version of code done tkinter_pack, they're doing the same thing really
# this is grid geometry manager
mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry('640x480-8-200')


label = tkinter.Label(mainWindow, text='Hello World')
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row = 1, column = 1)

# Makes the canvas be on the left
canvas = tkinter.Canvas(leftFrame, relief ='raised', borderwidth=1)
#canvas.pack(side='left',fill =tkinter.Y, expand=True)
canvas.grid(row=1, column =0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')

# Puts buttons in the right frame
button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')


# stacks the buttons on top of eavh other
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='nes')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')


mainWindow.mainloop()





