from tkinter import *

root = Tk()

#we are creating the label widget
button0 = Entry(root, width=50,padx = 5 , pady = 5)
button1 = Button(root, text="1",padx = 5,pady=5,border=0)
button2 = Button(root, text="2",padx = 5,pady=5,border=0)
button3 = Button(root, text="3",padx = 5,pady=5,border=0)
button4 = Button(root, text="4",padx = 5,pady=5,border=0)
button5 = Button(root, text="5",padx = 5,pady=5,border=0)
button6 = Button(root, text="6",padx = 5,pady=5,border=0)
button7 = Button(root, text="7",padx = 5,pady=5,border=0)
button8 = Button(root, text="8",padx = 5,pady=5,border=0)
button9 = Button(root, text="9",padx = 5,pady=5,border=0)

#we are showing in the screen

button0.grid(Text  = )

button1.grid(row = 1 , column = 0)
button2.grid(row = 1 , column = 1)
button3.grid(row = 1 , column = 2)
button4.grid(row = 2 , column = 0)
button5.grid(row = 2 , column = 1)
button6.grid(row = 2 , column = 2)
button7.grid(row = 3 , column = 0)
button8.grid(row = 3 , column = 1)
button9.grid(row = 3 , column = 2)

root.mainloop()
