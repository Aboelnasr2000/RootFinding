import tkinter as tk
from tkinter import ttk
from sympy import var
from sympy import sympify
from sympy import symbols
from numpy import linspace
from sympy import lambdify
from sympy import sympify
import matplotlib.pyplot as mpl
import math
import time


def FalseReguli(user_input, xl, xu, Iterations, Epsilon, singlemod):
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
        fxl = expr.subs(x, xl)
        fxu = expr.subs(x, xu)
        Allist = []
        err = "INF"
        oldmid = 0
        start_time = time.time()
        count = 0
        Fp = 0

        if fxl * fxu > 0:
            return "No zero in that interval"
        for i in range(Iterations):
            if not isinstance(err, str) and err < Epsilon:
                break

            xr = ((xl * fxu) - (xu * fxl) ) / (fxu - fxl) * 1.0
            if i > 0:
                err = abs(xr - oldmid)
            fxl = expr.subs(x, xl)
            fxu = expr.subs(x, xu)
            fxr = expr.subs(x, xr)
            templist = [xl, xu, fxl, fxu, xr, fxr, err]
            Allist.append(templist)
            oldmid = xr
            Fp = xr
            count = count + 1
            if fxl * fxr > 0:
                xl = xr
            else:
                xu = xr
            if singlemod == 1:
                mpl.scatter(xr, fxr)
                mpl.pause(1)

        executiontime = time.time() - start_time
        show(Allist, executiontime, count, Fp)
        mpl.show()

        return ""
    except:
        return "Wrong function ( Invalid Input )"


def show(tempList, executiontime, count, Fp):
    scores = tk.Tk()
    label = tk.Label(scores, text="False Position", font=("Arial", 30)).grid(row=0, columnspan=3)

    cols = ('Iterations', 'Xl', 'Xu', 'F(Xl)', 'F(Xu)', 'Xr', 'F(Xr)', 'Error')

    listBox = ttk.Treeview(scores, columns=cols, show='headings', height=30)

    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=2, column=0, columnspan=2)

    closeButton = tk.Button(scores, text="End", width=15, command=exit).grid(row=10, column=1)

    for i, (xl, xu, fxl, fxu, xr, fxr, err) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, xl, xu, fxl, fxu, xr, fxr, err))

    ET = 'execution time: ' + str(executiontime)
    ETL = tk.Label(scores, text=ET, font=("Arial", 20)).grid(row=4, columnspan=4)
    NI = 'Number of iterations  = ' + str(count)
    NIL = tk.Label(scores, text=NI, font=("Arial", 20)).grid(row=5, columnspan=4)
    FC = ' Midpoint = ' + str(Fp)
    FCL = tk.Label(scores, text=FC, font=("Arial", 20)).grid(row=6, columnspan=4)


def CallFalseReguli(func, xl, xu, Iterations, Epsilon, singlemod):
    return FalseReguli(func, xl, xu, Iterations, Epsilon, singlemod)
