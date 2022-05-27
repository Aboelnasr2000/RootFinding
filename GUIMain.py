from tkinter import *
import tkinter as tk
import NewtonRaphsonGUI as nr
import BisectionGUI as bs
import FalsePositionGUI as fr
import SecantGUI as sg
import FixedPointGUI as fp

root = tk.Tk()
root.geometry("300x300")


def method():
    if chosen.get() == "Bisection":
        bs.drawBisection()
    if chosen.get() == "False-Position":
        fr.drawFalseReguli()
    if chosen.get() == "Fixed-Point":
        fp.drawFixedPoint()
    if chosen.get() == "Newton-Raphson":
        nr.drawNewtonRaphson()
    if chosen.get() == "Secant":
        sg.drawSecant()


options = [
    "Bisection",
    "False-Position",
    "Fixed-Point",
    "Newton-Raphson",
    "Secant"
]

chosen = StringVar()

chosen.set("Choose Method")

methodLabel = Label(root, text="Method : ").grid(row=0, column=0)
drop = OptionMenu(root, chosen, *options)
drop.grid(row= 0, column=1)

button = Button(root, text="Choose", command=method).grid(row=1, column=2)

root.mainloop()
