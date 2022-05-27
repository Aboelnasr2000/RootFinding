import tkinter as tk
from tkinter import messagebox

from sympy.core.symbol import var
import FixedPoint as fp

read = 0


def testing(GE, doneButton, readButton):
    global read
    if read == 0:
        GE.config(state='disabled')
        doneButton.config(state='disabled')
        readButton.config(state='normal')
        read = 1
    else:
        GE.config(state='normal')
        readButton.config(state='disabled')
        doneButton.config(state='normal')
        read = 0


def readFile(XRE, MIE, EE):
    try:
        inputFile = open('inputfile.txt', 'r')
        line = inputFile.readline()
    except:
        messagebox.showerror("Error", "Can't read from file")
    try:
        gx = line
        xr = float(XRE.get())
        iterations = int(MIE.get())
        epsilon = float(EE.get())
        err = fp.CallFixedPoint(gx, xr, iterations, epsilon)
        if err != "":
            messagebox.showerror("Error", err)
    except:
        messagebox.showerror("Error", "Wrong Data Type")


def donefunc(GE, XRE, MIE, EE):
    try:
        gx = GE.get()
        xr = float(XRE.get())
        iterations = int(MIE.get())
        epsilon = float(EE.get())
        err = fp.CallFixedPoint(gx, xr, iterations, epsilon)
        if err != "":
            messagebox.showerror("Error", err)
    except:
        messagebox.showerror("Error", "Wrong Data Type")


def drawFixedPoint():
    top = tk.Tk()

    GL = tk.Label(top, text="G(x): ").grid(row=0, column=0)
    GE = tk.Entry(top, bd=5, width=30)
    GE.grid(row=0, column=1)

    Var2 = tk.IntVar()
    FR = tk.Checkbutton(top, text="File Read", variable=Var2, command=lambda: testing(GE, doneButton, readButton))
    FR.grid(row=0, column=2)

    XRL = tk.Label(top, text="Xr: ").grid(row=1, column=0)
    XRE = tk.Entry(top, bd=5, width=30)
    XRE.grid(row=1, column=1)

    MIL = tk.Label(top, text="MAX Iterations: ").grid(row=2, column=0)
    MIE = tk.Entry(top, bd=5, width=30)
    MIE.grid(row=2, column=1)
    MIE.insert(0, "50")

    EL = tk.Label(top, text="Epsilon: ").grid(row=2, column=2)
    EE = tk.Entry(top, bd=5, width=30)
    EE.grid(row=2, column=3)
    EE.insert(0, 0.00001)

    doneButton = tk.Button(top, text="Done", command=lambda: donefunc(GE, XRE, MIE, EE))
    doneButton.grid(row=3, column=3)
    readButton = tk.Button(top, text="Done(function from file)", state='disabled',
                           command=lambda: readFile(XRE, MIE, EE))
    readButton.grid(row=3, column=4)

    top.mainloop()
