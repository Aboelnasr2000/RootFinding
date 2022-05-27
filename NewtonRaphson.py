import tkinter as tk
from tkinter import ttk
from sympy import var
from sympy import symbols
from numpy import linspace
from sympy import lambdify
from sympy import sympify
from sympy import diff
import math
import matplotlib.pyplot as mpl
import time


def NewtonRaphson(user_input, xi, iterations, epsilon, singlemod):
    x = var('x')
    e = var('e')
    expr = sympify(user_input)
    fxdiff = diff(expr, x)
    expr = expr.subs(e, math.e)
    fxdiff = fxdiff.subs(e, math.e)
    try:
        t = symbols('x')
        expr = sympify(expr)
        if singlemod == 1:
            lam_x = lambdify(t, expr, modules=['numpy'])
            x_vals = linspace(-10, 10, 10000)
            y_vals = lam_x(x_vals)
            axis = mpl.gca()
            axis.set_ylim([min(y_vals), max(y_vals)])
            mpl.plot(x_vals, y_vals)

        print(expr)
        expr = sympify(expr)
        fxi = expr.subs(x, xi)
        fxidiff = fxdiff.subs(x, xi)
        Alllist = []
        err = "INF"
        start_time = time.time()
        count = 0
        FP = 0
        for i in range(iterations):
            if not isinstance(err, str) and err < epsilon:
                break
            count = count + 1
            if fxdiff == 0:
                return "Change Xi value"
            xnext = xi - (fxi / fxidiff)
            if i > 0:
                err = abs(xnext - xi)
            templist = [xi, xnext, fxi, fxidiff, err]
            Alllist.append(templist)
            xi = xnext
            FP = xnext
            fxi = expr.subs(x, xi)
            fxidiff = fxdiff.subs(x, xi)

            if singlemod == 1:
                mpl.scatter(xi, fxi)
                mpl.pause(0.5)

        executionTime = time.time() - start_time
        show(Alllist, executionTime, count, FP)
        mpl.show()
        return ""
    except:
        return "Wrong function"


def show(templist, executionTime, count, FP):
    output = tk.Tk()

    label = tk.Label(output, text="Newton Raphson", font=("Arial", 30)).grid(row=0, columnspan=3)
    cols = ('Iterations', 'Xi', 'Xi+1', 'F(Xi)', 'F`(Xi)', 'Error')
    listBox = ttk.Treeview(output, columns=cols, show='headings', height=30)
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=2, column=0, columnspan=2)

    for i, (xi, xnext, fxi, fxidiff, err) in enumerate(templist, start=1):
        listBox.insert("", "end", values=(i, xi, xnext, fxi, fxidiff, err))

    ET = 'execution time  : ' + str(executionTime)
    ETl = tk.Label(output, text=ET, font=("Arial", 20)).grid(row=4, columnspan=4)
    NI = 'Number of iterations  = ' + str(count)
    NIL = tk.Label(output, text=NI, font=("Arial", 20)).grid(row=5, columnspan=4)
    FC = ' Midpoint = ' + str(FP)
    FCL = tk.Label(output, text=FC, font=("Arial", 20)).grid(row=6, columnspan=4)


def CallNewtonRaphson(func, xi, iterations, epsilon, singlemod):
    return NewtonRaphson(func, xi, iterations, epsilon, singlemod)
