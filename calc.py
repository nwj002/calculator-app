# IMPORT TKINTER LIBRARY
from tkinter import *

#  IMPORT MATH MODULE
import math

# CREATING WINDOW
root=Tk()

# ASSINING THE TITLE AND ICON
root.iconbitmap("calc.ico")
root.title("calculator")

# BACKGROUND COLOUR
root.configure(bg="black")

#  ENTRY WIDGET
e=Entry(root,width=60,borderwidth=10, relief=GROOVE,)
e.grid( row=0,column=0,columnspan=4,padx=10,pady=10, ipady=10,)


# DEFINING FUNCTIONS
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num 
    global math
    math="Addition"
    f_num=int(first_number)
    e.delete(0,END)


def button_sub():
    first_number=e.get()
    global f_num  
    global math
    math="Subtract"
    f_num=int(first_number)
    e.delete(0,END)


def button_mun():
    first_number=e.get()
    global f_num  
    global math
    math="muntiply"
    f_num=int(first_number)
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_num  
    global math
    math="divide"
    f_num=int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="Addition":
        e.insert(0,f_num + int(second_number))
    elif math=="Subtract":
        e.insert(0,f_num - int(second_number))
    elif math=="muntiply":
        e.insert(0,f_num * int(second_number))
    elif math=="divide":
        e.insert(0,f_num / int(second_number))

#  BUTTON WIDGET
button_1=Button(root,text="1",padx=40,pady=20,font='Helvetica 18 bold',command=lambda : button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,font='Helvetica 18 bold',command=lambda : button_click(2))
button_3=Button(root,text="3",padx=41,pady=20,font='Helvetica 18 bold',command=lambda : button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,font='Helvetica 18 bold',command=lambda : button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,font='Helvetica 18 bold',command=lambda : button_click(5))
button_6=Button(root,text="6",padx=41,pady=20,font='Helvetica 18 bold',command=lambda : button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,font='Helvetica 18 bold',command=lambda : button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,font='Helvetica 18 bold',command=lambda : button_click(8))
button_9=Button(root,text="9",padx=41,pady=20,font='Helvetica 18 bold',command=lambda : button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,font='Helvetica 18 bold',command=lambda : button_click(0))
button_add=Button(root,text="+",padx=44.5,pady=20,command=button_add, fg="green",font='Helvetica 18 bold')
button_sub=Button(root,text="-",padx=48.49,pady=20,command=button_sub,fg="green",font='Helvetica 18 bold')
button_mun=Button(root,text="*",padx=43,pady=20,command=button_mun,fg="green",font='Helvetica 18 bold')
button_div=Button(root,text="/",padx=43,pady=20,command=button_div,fg="green",font='Helvetica 18 bold')
button_equal=Button(root,text="=",padx=45.4,pady=20,command=button_equal, bg="#009900",fg="white",font='Helvetica 18 bold')
button_clear=Button(root,text="Clear",padx=22.49,pady=20,command=button_clear, fg="red",font='Helvetica 18 bold')

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_clear.grid(row=1,column=3)
button_add.grid(row=2,column=3)
button_sub.grid(row=3,column=3)
button_mun.grid(row=4,column=2)
button_div.grid(row=4,column=1)
button_equal.grid(row=4,column=3,)

root.mainloop()