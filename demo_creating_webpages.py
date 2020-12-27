"""
import the tkinter module
create the gui app main window
add one or more of the above-mentioned wid
"""


import tkinter

Top = tkinter.Tk()

Top.geometry("900x900")

def Change_Label():
    ThanksLbl = tkinter.Label(Top, text="You have clicked Button, Thank You").pack()
   for r in range(3):
       for c in range(4):
         TLabel = tkinter.Label(Top, text='R%s/C%s' % (r, c), borderwidth=1)
         TLabel = tkinter.grid(row=r, Column=c)

name_Label = tkinter.Label(Top, text="Hello World").pack()
ThankYouBtn = tkinter.Button(Top, text="Click to submit", command=Change_Label).pack()

Top.mainloop()

