import tkinter as tk
from tkinter import messagebox

# from sympy.core.symbol import var
import NewtonRaphson as nr

mod = 0
read = 0


def changeval():
    global mod
    mod = mod ^ 1


def testing(FE, doneButton , readButton):
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


def readFile(E21, E31, E32):
    try:
        inputFile = open('inputfile.txt', 'r')
        line = inputFile.readline()
    except:
        messagebox.showerror("Error", "Can't read from file")
    try:
        fx = line
        xi = float(E21.get())
        iterations = int(E31.get())
        epsilon = float(E32.get())
        err = nr.CallNewtonRaphson(fx, xi, iterations, epsilon, mod)
        if err != "":
            messagebox.showerror("Error", err)
    except:
        messagebox.showerror("Error", "Wrong Data Type")


def donefunc(FE, XiE, MIE, EE):
    try:
        fx = FE.get()
        xi = float(XiE.get())
        iterations = int(MIE.get())
        epsilon = float(EE.get())
        err = nr.CallNewtonRaphson(fx, xi, iterations, epsilon, mod)
        if err != "":
            messagebox.showerror("Error", err)
    except:
        messagebox.showerror("Error", "Wrong Data Type")


def drawNewtonRaphson():
    top = tk.Tk()

    FL = tk.Label(top, text="F(x): ").grid(row=0, column=0)
    FE = tk.Entry(top, bd=5, width=30)
    FE.grid(row=0, column=1)

    Var2 = tk.IntVar()
    FR = tk.Checkbutton(top, text="File Read", variable=Var2, command=lambda: testing(FE, doneButton, readButton))
    FR.grid(row=0, column=2)

    XiL = tk.Label(top, text="Xi: ").grid(row=1, column=0)
    XiE = tk.Entry(top, bd=5, width=30)
    XiE.grid(row=1, column=1)

    MIL = tk.Label(top, text="MAX Iterations: ").grid(row=2, column=0)
    MIE = tk.Entry(top, bd=5, width=30)
    MIE.grid(row=2, column=1)
    MIE.insert(0, "50")

    EL = tk.Label(top, text="Epsilon: ").grid(row=2, column=2)
    EE = tk.Entry(top, bd=5, width=30)
    EE.grid(row=2, column=3)
    EE.insert(0, 0.00001)

    Var1 = tk.IntVar()
    SM = tk.Checkbutton(top, text="Single mode", variable=Var1, command=changeval)
    SM.grid(row=3, column=0)

    doneButton = tk.Button(top, text="Done", command=lambda: donefunc(FE, XiE, MIE, EE))
    doneButton.grid(row=3, column=3)
    readButton = tk.Button(top, text="Read Function From File", state='disabled', command=lambda: readFile(XiE, MIE, EE))
    readButton.grid(row=3, column=4)

    top.mainloop()
