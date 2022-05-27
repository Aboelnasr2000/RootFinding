import tkinter as tk
from tkinter import messagebox
from sympy.core.symbol import var
import FalsePosition as fr

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


def readFile(XlL, XuE, MIE, EE, mod):
    try:
        inputFile = open('inputfile.txt', 'r')
        line = inputFile.readline()
        print(line)
    except:
        messagebox.showerror("Error", "Can't read from file")
    try:
        fx = line
        xl = float(XlL.get())
        xu = float(XuE.get())
        iterations = int(MIE.get())
        epsilon = float(EE.get())
        err = fr.CallFalseReguli(fx, xl, xu, iterations, epsilon, mod)
        if err != "":
            messagebox.showerror("Error", err)
    except:
        messagebox.showerror("Error", "Wrong Data Type")
def donefunc(FE, XlE, XuE, MIE, EE, mod):
    try:
        fx = FE.get()
        xl = float(XlE.get())
        xu = float(XuE.get())
        iterations = int(MIE.get())
        epsilon = float(EE.get())
        err = fr.CallFalseReguli(fx, xl, xu, iterations, epsilon, mod)
        if err != "":
            messagebox.showerror("Error", err)
    except:
        messagebox.showerror("Error", "Wrong Data Type")


def drawFalseReguli():
    top = tk.Tk()

    FL = tk.Label(top, text="F(x): ").grid(row=0, column=0)
    FE = tk.Entry(top, bd=5, width=30)
    FE.grid(row=0, column=1)

    Var2 = tk.IntVar()
    FR = tk.Checkbutton(top, text="File Read", variable=Var2, command=lambda: testing(FE, doneButton, readButton))
    FR.grid(row=0, column=3)

    XlL = tk.Label(top, text="Xl: ").grid(row=1, column=0)
    XlE = tk.Entry(top, bd=5, width=30)
    XlE.grid(row=1, column=1)

    XuL = tk.Label(top, text="Xu: ").grid(row=2, column=0)
    XuE = tk.Entry(top, bd=5, width=30)
    XuE.grid(row=2, column=1)

    MIL = tk.Label(top, text="MAX Iterations: ").grid(row=1, column=2)
    MIE = tk.Entry(top, bd=5, width=30)
    MIE.grid(row=1, column=3)
    MIE.insert(0, "50")

    EL = tk.Label(top, text="Epsilon: ").grid(row=2, column=2)
    EE = tk.Entry(top, bd=5, width=30)
    EE.grid(row=2, column=3)
    EE.insert(0, 0.00001)

    var1 = tk.IntVar()
    CH = tk.Checkbutton(top, text="Single mode", variable=var1, command=changeval)
    CH.grid(row=3, column=0)

    doneButton = tk.Button(top, text="Done", command=lambda: donefunc(FE, XlE, XuE, MIE, EE, mod))
    doneButton.grid(row=3, column=3)
    readButton = tk.Button(top, text="Read Function From File", state='disabled',
                           command=lambda: readFile(XlE, XuE, MIE, EE, mod))
    readButton.grid(row=3, column=4)
    top.mainloop()
