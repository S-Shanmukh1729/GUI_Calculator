from tkinter import *

calci=Tk()
calci.geometry("350x350")
calci.configure(bg='grey25')
calci.title("Calculator")
calci.resizable(0,0)


va=StringVar() # for showing on screen and computing
entry1=Entry(calci,textvar=va,width=50)
entry1.place(x=16,y=10,height=50)


def fun(v):
    if v == 'clr':
        va.set("")
    elif v == 'cl':
        va.set(va.get()[:-1])
    elif v == '=':
        try:
            va.set(eval(va.get()))
        except:
            va.set("INVALID SYNTAX")
    else:
        va.set(va.get() + v)

## Buttons

ac = Button(calci, text="AC", fg="black", bg="grey66", width=12, command=lambda : fun('clr')).place(x=25,y=80,height=30)
add = Button(calci, text="+", fg="black", bg="grey66", width=12, command=lambda : fun('+')).place(x=120,y=80,height=30)
sub = Button(calci, text="-", fg="black", bg="grey66", width=12, command=lambda : fun('-')).place(x=215,y=80,height=30)
mul = Button(calci, text="x", fg="black", bg="grey66", width=12, command=lambda : fun('*')).place(x=25,y=115,height=30)
div = Button(calci, text="/", fg="black", bg="grey66", width=12, command=lambda : fun('/')).place(x=120,y=115,height=30)


eq = Button(calci, text="=", fg="black", bg="grey66", width=12, command=lambda : fun('=')).place(x=215,y=115,height=30)


one = Button(calci, text="1", fg="black", bg="grey66", width=12, command=lambda : fun('1')).place(x=25,y=150,height=30)
two = Button(calci, text="2", fg="black", bg="grey66", width=12, command=lambda : fun('2')).place(x=120,y=150,height=30)
three = Button(calci, text="3", fg="black", bg="grey66", width=12, command=lambda : fun('3')).place(x=215,y=150,height=30)
four = Button(calci, text="4", fg="black", bg="grey66", width=12, command=lambda : fun('4')).place(x=25,y=185,height=30)
five = Button(calci, text="5", fg="black", bg="grey66", width=12, command=lambda : fun('5')).place(x=120,y=185,height=30)
six = Button(calci, text="6", fg="black", bg="grey66", width=12, command=lambda : fun('6')).place(x=215,y=185,height=30)
seven = Button(calci, text="7", fg="black", bg="grey66", width=12, command=lambda : fun('7')).place(x=25,y=220,height=30)
eight = Button(calci, text="8", fg="black", bg="grey66", width=12, command=lambda : fun('8')).place(x=120,y=220,height=30)
nine = Button(calci, text="9", fg="black", bg="grey66", width=12, command=lambda : fun('9')).place(x=215,y=220,height=30)
zero = Button(calci, text="0", fg="black", bg="grey66", width=12, command=lambda : fun('0')).place(x=25,y=255,height=30)
dzero = Button(calci, text="00", fg="black", bg="grey66", width=12, command=lambda : fun('00')).place(x=120,y=255,height=30)
dot = Button(calci, text=".", fg="black", bg="grey66", width=12, command=lambda : fun('.')).place(x=215,y=255,height=30)

clear = Button(calci, text="c", fg="black", bg="grey66", width=12, command=lambda : fun('cl')).place(x=25,y=290,height=30)

para1 = Button(calci, text="(", fg="black", bg="grey66", width=12, command=lambda : fun('(')).place(x=120,y=290,height=30)
para2 = Button(calci, text=")", fg="black", bg="grey66", width=12, command=lambda : fun(')')).place(x=215,y=290,height=30)


calci.mainloop()
