import tkinter as tk
from tkinter import ttk
from sympy import var
from sympy import symbols
from numpy import linspace
from sympy import lambdify
from sympy import sympify
import matplotlib.pyplot as mpl
import time
import math


def Secant(user_input, xold, xi, Iterations, epsilon, singlemod):
    x = var('x')
    e = var('e')
    expr = sympify(user_input)
    expr = expr.subs(e, math.e)
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

        expr = sympify(expr)

        fxi = expr.subs(x, xi)
        fxold = expr.subs(x, xold)
        Alllist = []
        err = "INF"
        start_time = time.time()
        count = 0
        FP = 0
        for i in range(Iterations):
            if not isinstance(err, str) and err < epsilon:
                break
            count = count + 1
            xnext = xi - fxi * (xold - xi) / (fxold - fxi)
            FP = xnext
            if i > 0:
                err = abs(xnext - xi)

            templist = [xold, xi, xnext, fxi, fxold, err]
            Alllist.append(templist)
            xold = xi
            xi = xnext
            fxi = expr.subs(x, xi)
            fxold = expr.subs(x, xold)
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
    label = tk.Label(output, text="Secant", font=("Arial", 30)).grid(row=0, columnspan=3)

    cols = ('Iterations', 'Xold', 'Xi', 'Xi+1', 'F(Xi)', 'F(Xold)', 'Error')
    listBox = ttk.Treeview(output, columns=cols, show='headings', height=30)
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=2, column=0, columnspan=2)

    for i, (xold, xi, xnext, fxi, fxold, err) in enumerate(templist, start=1):
        listBox.insert("", "end", values=(i, xold, xi, xnext, fxi, fxold, err))

    ET = 'execution time  : ' + str(executionTime)
    ETl = tk.Label(output, text=ET, font=("Arial", 20)).grid(row=4, columnspan=4)
    NI = 'Number of iterations  = ' + str(count)
    NIL = tk.Label(output, text=NI, font=("Arial", 20)).grid(row=5, columnspan=4)
    FC = ' Midpoint = ' + str(FP)
    FCL = tk.Label(output, text=FC, font=("Arial", 20)).grid(row=6, columnspan=4)


def CallSecant(func, xold, xi, iterations, epsilon, singlemod):
    return Secant(func, xold, xi, iterations, epsilon, singlemod)
