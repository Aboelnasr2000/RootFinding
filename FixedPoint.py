import tkinter as tk
from tkinter import ttk
from sympy import var
from sympy import sympify
from sympy import symbols
from sympy import diff
import time
import math


def FixedPoint(user_input, xr, iterations, epsilon):
    x = var('x')
    e = var('e')
    expr = sympify(user_input)
    expr = expr.subs(e, math.e)
    try:
        t = symbols('x')
        expr = sympify(expr)
        gxdiff = diff(expr, x)
        if gxdiff.subs(x, xr) > 1:
            return "No Convergence"
        Alllist = []
        templist = [xr, "-"]
        Alllist.append(templist)
        print(expr)
        xr = expr.subs(x, xr)
        xrold = 0
        err = "-"
        start_time = time.time()
        FP = 0
        count = 0

        for i in range(iterations):
            if not isinstance(err, str) and err < epsilon:
                break
            count = count + 1
            xr = expr.subs(x, xr)
            if i > 0:
                err = abs(xr - xrold)
            templist = [xr, err]
            Alllist.append(templist)
            xrold = xr
            FP = xr

        execution = time.time() - start_time
        show(Alllist, execution, count, FP)
        return ""
    except:
        return "Wrong function (Invalid Input)"


def show(templist, execution, count, FP):
    output = tk.Tk()
    label = tk.Label(output, text="Fixed Point", font=("Arial", 30)).grid(row=0, columnspan=3)

    cols = ('Iterations', 'Xr', 'Error')
    listBox = ttk.Treeview(output, columns=cols, show='headings', height=30)
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=2, column=0, columnspan=2)

    for i, (xr, err) in enumerate(templist, start=1):
        listBox.insert("", "end", values=(i, xr, err))

    ET = 'execution time  : ' + str(execution)
    ETl = tk.Label(output, text=ET, font=("Arial", 20)).grid(row=4, columnspan=4)
    NI = 'Number of iterations  = ' + str(count)
    NIL = tk.Label(output, text=NI, font=("Arial", 20)).grid(row=5, columnspan=4)
    FC = ' Midpoint = ' + str(FP)
    FCL = tk.Label(output, text=FC, font=("Arial", 20)).grid(row=6, columnspan=4)


def CallFixedPoint(func, xi, iterations, epsilon):
    return FixedPoint(func, xi, iterations, epsilon)
