import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#
# # tkinter._test()
#
# create the window which will act as the GUI

# this is the pack geometry manager

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')


label = tkinter.Label(mainWindow, text='Hello World')
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill = tkinter.Y, expand= False)

# Makes the canvas be on the left
canvas = tkinter.Canvas(leftFrame, relief ='raised', borderwidth=1)
#canvas.pack(side='left',fill =tkinter.Y, expand=True)
canvas.pack(side='left',anchor ='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

# Puts buttons in the right frame
button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')


# stacks the buttons on top of eavh other
button1.pack(side='top', anchor='n')
button2.pack(side='top', anchor='s')
button3.pack(side='top', anchor='e')

mainWindow.mainloop()