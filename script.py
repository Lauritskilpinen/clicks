import win32api
import time
import math
import ctypes
from ctypes import windll, Structure, c_long, byref
from tkinter import *
from tkinter import ttk

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    time.sleep(5)
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return [pt.x,pt.y]

FrstBtn = [5,6]
SecnBtn = []

    
def selFrstBtn(res):
    userInput.delete(0, END)
    userInput.insert(0, res)
    FrstBtn[0] = int(res[0])
    FrstBtn[1] = int(res[1])
    return

def selSecnBtn(res):
    userInput.delete(0, END)
    userInput.insert(0, res)
    SecnBtn = res
    print(SecnBtn)
    print(userInput1.get())
    return


def printy(x,y,z):
    x1 = x
    for pages in range(z):
        if (pages > 9):
            x1 = x +10
            ctypes.windll.user32.SetCursorPos(x1,y)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
            time.sleep(3)
    return

ws = Tk()
ws.title("Automate clicks")
ws.geometry("400x250")

frame = Frame(ws)
userInput = Entry(frame, width=40, justify=CENTER)
userInput.grid(row=0, columnspan=3, padx=5, pady= 10)

userInput1 = Entry(frame, width=40, justify=CENTER)
userInput1.grid(row=1, columnspan=3, padx=5, pady= 10)

Button(frame,text="Select: next btn",command=lambda:selFrstBtn(queryMousePosition())).grid(row=2, column=0)
Button(frame,text="Select: dwn btn",command=lambda:selSecnBtn(queryMousePosition())).grid(row=2, column=1)
Button(frame,text="Run the program",command=lambda:printy(FrstBtn[0],FrstBtn[1],int(userInput1.get()))).grid(row=3, column=0)

frame.pack()

ws.mainloop()
