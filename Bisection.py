import tkinter as tk
from tkinter import ttk
from sympy import var
from sympy import sympify
from sympy import symbols
from numpy import linspace
from sympy import lambdify
from sympy import sympify
import math
import matplotlib.pyplot as mpl
import time


def Bisection(user_input, a, b, Iterations, Epsilon, singlemod):
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
        fa = expr.subs(x, a)
        fb = expr.subs(x, b)
        Allist = []
        err = "INF"
        oldmid = 0
        start_time = time.time()
        count = 0
        FinalP = 0
        if fa * fb > 0:
            return "No zero in that interval"
        for i in range(Iterations):
            if not isinstance(err, str) and err < Epsilon:
                break
            count = count + 1
            mid = a + (b - a) / 2
            if i > 0:
                err = abs(mid - oldmid)
            fa = expr.subs(x, a)
            fb = expr.subs(x, b)
            fmid = expr.subs(x, mid)
            FinalP = mid
            templist = [a, b, fa, fb, mid, fmid, err]
            Allist.append(templist)
            oldmid = mid
            if fa * fmid > 0:
                a = mid
            else:
                b = mid

            if singlemod == 1:
                mpl.scatter(mid, fmid)
                mpl.pause(1)

        executionTime = time.time() - start_time
        show(Allist, executionTime, count, FinalP)
        mpl.show()
        return ""
    except:
        return "Wrong function"


def show(tempList, executionTime, count, FinalP):
    output = tk.Tk()
    label = tk.Label(output, text="Bisection", font=("Arial", 30)).grid(row=0, columnspan=3)

    cols = ('Iteration', 'A', 'B', 'F(A)', 'F(B)', 'C', 'F(C)', 'Error')
    listBox = ttk.Treeview(output, columns=cols, show='headings', height=30)

    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=3, column=0, columnspan=2)

    for i, (a, b, fa, fb, mid, fmid, err) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, a, b, fa, fb, mid, fmid, err))

    ET = 'execution time  : ' + str(executionTime)
    ETl = tk.Label(output, text=ET, font=("Arial", 20)).grid(row=4, columnspan=4)
    NI = 'Number of iterations  = ' + str(count)
    NIL = tk.Label(output, text=NI, font=("Arial", 20)).grid(row=5, columnspan=4)
    FC = ' Midpoint = ' + str(FinalP)
    FCL = tk.Label(output, text=FC, font=("Arial", 20)).grid(row=6, columnspan=4)


def CallBisection(func, a, b, Iterations, Epsilon, singlemod):
    return Bisection(func, a, b, Iterations, Epsilon, singlemod)
