#!/usr/bin/env python3
# SORRY FOR THIS MESSY CODE AND BAD VARIABLE NAMES AND ALL THAT. I'm just learning and having fun!
# I will refactor the code and clean up everything once I get comfortable. :]
# For educational purposes only. Created with PyCharm.
# I'll break you until you're mine.
# I'll admit I did 60% trial-and-error, and 40% reading the documentation / searching up questions.

from tkinter import *
import tkinter as tk
import operator
from math import sqrt

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.firstNumberField = Entry()
        self.firstNumberField.grid(row=0, sticky=W)

        self.firstNumberFieldContents = StringVar()
        self.firstNumberFieldContents.set('0 ')
        self.firstNumberField["textvariable"] = self.firstNumberFieldContents

        self.firstNumberField.bind('<Key-Return>', self.enter)

        self.buttonFrame = Frame(root)
        self.buttonFrame.grid(row=3, column=0, columnspan=5, sticky=W)

        self.additionButton = tk.Button(self.buttonFrame)
        self.additionButton.grid(row=3, column=0, sticky=W+E)
        self.additionButton["text"] = "+"
        self.additionButton["command"] = self.add

        self.minusButton = tk.Button(self.buttonFrame)
        self.minusButton.grid(row=3, column=1, sticky=W+E)
        self.minusButton["text"] = "-"
        self.minusButton["command"] = self.minus

        self.multiplyButton = tk.Button(self.buttonFrame)
        self.multiplyButton.grid(row=3, column=2, sticky=W+E)
        self.multiplyButton["text"] = "*"
        self.multiplyButton["command"] = self.multiply

        self.divideButton = tk.Button(self.buttonFrame)
        self.divideButton.grid(row=3, column=3, sticky=W+E)
        self.divideButton["text"] = "/"
        self.divideButton["command"] = self.divide

        self.clearButton = tk.Button(self.buttonFrame)
        self.clearButton.grid(row=3, column=4, sticky=W+E)
        self.clearButton["text"] = "CE"
        self.clearButton["command"] = self.clear

        self.squareButton = tk.Button(self.buttonFrame)
        self.squareButton.grid(row=4, sticky=W+E)
        self.squareButton["text"] = "²"
        self.squareButton["command"] = self.square

        self.squareRootButton = tk.Button(self.buttonFrame)
        self.squareRootButton.grid(row=4, column=1, sticky=W+E)
        self.squareRootButton["text"] = "√"
        self.squareRootButton["command"] = self.squareRoot

        # self.oppositeButton = tk.Button(self.buttonFrame)
        # self.oppositeButton.grid(row=4, column=4, sticky=E)
        # self.oppositeButton["text"] = "+/-"
        # self.oppositeButton["command"] = self.opposite
        # An opposite button/function would not work with the way
        # I designed this calculator.
        # The user can simply type - in front of a number and it'll be parsed as a negative number.
        # ex: -3 - 2 = -5.0
        # ex: 1 - 3.0 = -2.0

        self.enterButton = tk.Button(self.buttonFrame)
        self.enterButton.grid(row=5, column=4, sticky=E)
        self.enterButton["text"] = '='
        self.enterButton["command"] = self.enter

        self.errorOutput = Text(height=1)
        self.errorOutput.config(state=DISABLED)
        self.errorOutput.grid(row=1, column=0, sticky=N+E+S+W)

    def add(self):
        self.errorOutput.configure(state=NORMAL)
        self.errorOutput.delete(0.0, END)
        self.errorOutput.configure(state=DISABLED)

        self.firstNumberFieldContents.set(self.firstNumberFieldContents.get() + " + ")
        self.firstNumberField.icursor(END)

    def minus(self):
        self.errorOutput.configure(state=NORMAL)
        self.errorOutput.delete(0.0, END)
        self.errorOutput.configure(state=DISABLED)

        self.firstNumberFieldContents.set(self.firstNumberFieldContents.get() + " - ")
        self.firstNumberField.icursor(END)

    def multiply(self):
        self.errorOutput.configure(state=NORMAL)
        self.errorOutput.delete(0.0, END)
        self.errorOutput.configure(state=DISABLED)

        self.firstNumberFieldContents.set(self.firstNumberFieldContents.get() + " * ")
        self.firstNumberField.icursor(END)

    def divide(self):
        self.firstNumberFieldContents.set(self.firstNumberFieldContents.get() + " / ")
        self.firstNumberField.icursor(END)

    def clear(self):
        self.errorOutput.configure(state=NORMAL)
        self.errorOutput.delete(0.0, END)
        self.errorOutput.configure(state=DISABLED)

        if self.firstNumberFieldContents.get() == '0':
            self.errorOutput.configure(state=NORMAL)
            self.errorOutput.delete(0.0, END)
            self.errorOutput.insert(END, 'ERROR: Already cleared!')
            self.errorOutput.configure(state=DISABLED)
        else:
            self.firstNumberFieldContents.set('0')

    def square(self):
        self.errorOutput.configure(state=NORMAL)
        self.errorOutput.delete(0.0, END)
        self.errorOutput.configure(state=DISABLED)

        self.firstNumberFieldContents.set(str(float(self.firstNumberFieldContents.get()) * float(self.firstNumberFieldContents.get())) + ' ')
        self.firstNumberField.icursor(END)

    def squareRoot(self):
        self.errorOutput.configure(state=NORMAL)
        self.errorOutput.delete(0.0, END)
        self.errorOutput.configure(state=DISABLED)

        self.firstNumberFieldContents.set(str(sqrt(float(self.firstNumberFieldContents.get()))) + ' ')
        self.firstNumberField.icursor(END)

    def enter(self, event=None):
        self.errorOutput.configure(state=NORMAL)
        self.errorOutput.delete(0.0, END)
        self.errorOutput.configure(state=DISABLED)
        self.parseString(str(self.eval_binary_expr(*(self.firstNumberFieldContents.get().split()))))

    def parseString(self, string):
        self.firstNumberFieldContents.set(string + ' ')
        self.firstNumberField.icursor(END)

    # START: Code I found on StackedOverflow, and modified for this program
    # I'm really bad at parsing strings.
    # http://stackoverflow.com/questions/1740726/python-turn-string-into-operator
    def get_operator_fn(self, op):
        return {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
        }[op]

    def eval_binary_expr(self, op1, operator, op2):
        op1, op2 = float(op1), float(op2)
        if operator == '/' and op2 == 0:
            self.firstNumberFieldContents.set('0')
            self.errorOutput.configure(state=NORMAL)
            self.errorOutput.delete(0.0, END)
            self.errorOutput.insert(END, 'ERROR: Cannot divide by 0!')
            self.errorOutput.configure(state=DISABLED)
            return 0
        else:
            return self.get_operator_fn(operator)(op1, op2)
    # END

root = Tk()
app = App(root)
app.master.title("My Calculator")
app.master.resizable(width=False, height=False)
root.geometry('{}x{}'.format(192, 150))
app.master.minsize(192, 150)
app.mainloop()