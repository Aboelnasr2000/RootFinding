import tkinter as tk
from tkinter import messagebox

from sympy.core.symbol import var
import Secant as sec

mod = 0
read = 0


def testing(FE, doneButton, readButton):
    global read
    if read == 0:
        FE.config(state='disabled')
        doneButton.config(state='disabled')
        readButton.config(state='normal')
        read = 1
    else:
        FE.config(state='normal')
        readButton.config(state='disabled')
        doneButton.config(state='normal')
        read = 0


def changeval():
    global mod
    mod = mod ^ 1


def readFile( XOE, XIE, MIE, EE):
    try:
        inputFile = open('inputfile.txt', 'r')
        line = inputFile.readline()
    except:
        messagebox.showerror("Error", "Can't read from file")
    try:
        fx = line
        xold = float(XOE.get())
        xi = float(XIE.get())
        iterations = int(MIE.get())
        epsilon = float(EE.get())
        err = sec.CallSecant(line, xold, xi, iterations, epsilon, mod)
        if err != "":
            messagebox.showerror("Error", err)
    except:
        messagebox.showerror("Error", "Wrong Data Type")


def donefunc(FE, XOE, XIE, MIE, EE):
    try:
        fx = FE.get()
        xold = float(XOE.get())
        xi = float(XIE.get())
        iterations = int(MIE.get())
        epsilon = float(EE.get())
        err = sec.CallSecant(fx, xold, xi, iterations, epsilon, mod)
        if err != "":
            messagebox.showerror("Error", err)
    except:
        messagebox.showerror("Error", "Wrong Data Type")


def drawSecant():
    top = tk.Tk()

    FL = tk.Label(top, text="F(x): ").grid(row=0, column=0)
    FE = tk.Entry(top, bd=5, width=30)
    FE.grid(row=0, column=1)

    Var2 = tk.IntVar()
    FR = tk.Checkbutton(top, text="File Read", variable=Var2, command=lambda: testing(FE, doneButton, readButton))
    FR.grid(row=0, column=2)

    XOL = tk.Label(top, text="Xold: ").grid(row=1, column=0)
    XOE = tk.Entry(top, bd=5, width=30)
    XOE.grid(row=1, column=1)

    XIL = tk.Label(top, text="Xi: ").grid(row=2, column=0)
    XIE = tk.Entry(top, bd=5, width=30)
    XIE.grid(row=2, column=1)

    MIL = tk.Label(top, text="MAX Iterations: ").grid(row=1, column=2)
    MIE = tk.Entry(top, bd=5, width=30)
    MIE.grid(row=1, column=3)
    MIE.insert(0, "50")

    EL = tk.Label(top, text="Epsilon: ").grid(row=2, column=2)
    EE = tk.Entry(top, bd=5, width=30)
    EE.grid(row=2, column=3)
    EE.insert(0, 0.00001)

    var1 = tk.IntVar()
    CH = tk.Checkbutton(top, text="Single mode", variable=var1, command=changeval).grid(row=3, column=0)

    doneButton = tk.Button(top, text="Done", command=lambda: donefunc(FE, XOE, XIE, MIE, EE))
    doneButton.grid(row=3, column=3)
    readButton = tk.Button(top, text="Done(function from file)", command=lambda: readFile(XOE, XIE, MIE, EE))
    readButton.grid(row=3, column=4)
    top.mainloop()
