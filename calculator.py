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
        self.entry = Entry()
        self.entry.grid(row=0, sticky=W)
        self.contents = StringVar()
        self.contents.set('0 ')
        self.entry["textvariable"] = self.contents
        self.entry.focus_set()
        self.entry.icursor(END)
        self.entry.bind('<Key-Return>', self.enter)

        self.errorOutput = Text(height=1)
        self.errorOutput.config(state=DISABLED)
        self.errorOutput.grid(row=1, sticky=N+E+S+W)

        ### BUTTON FRAME AND BUTTONS BELOW ###

        self.buttonFrame = Frame(root)
        self.buttonFrame.grid(row=3, columnspan=5, sticky=W)

        self.additionButton = tk.Button(self.buttonFrame, text="+", command=lambda: self.appendBasicOperand(0))
        self.additionButton.grid(row=3, sticky=W+E)

        self.minusButton = tk.Button(self.buttonFrame, text="-", command=lambda: self.appendBasicOperand(1))
        self.minusButton.grid(row=3, column=1, sticky=W+E)

        self.multiplyButton = tk.Button(self.buttonFrame, text="*", command=lambda: self.appendBasicOperand(2))
        self.multiplyButton.grid(row=3, column=2, sticky=W+E)

        self.divideButton = tk.Button(self.buttonFrame, text="/", command=lambda: self.appendBasicOperand(3))
        self.divideButton.grid(row=3, column=3, sticky=W+E)

        self.clearButton = tk.Button(self.buttonFrame, text="CE", command=self.clear)
        self.clearButton.grid(row=3, column=4, sticky=W+E)

        self.squareButton = tk.Button(self.buttonFrame, text="²", command=self.square)
        self.squareButton.grid(row=4, sticky=W+E)

        self.squareRootButton = tk.Button(self.buttonFrame, text="√", command=self.squareRoot)
        self.squareRootButton.grid(row=4, column=1, sticky=W+E)

        self.enterButton = tk.Button(self.buttonFrame, text="=", command=self.enter)
        self.enterButton.grid(row=5, column=4, sticky=E)

        ### END BUTTONS ###

    ### FUNCTIONALITY ###

    def appendBasicOperand(self, index):
        self.resetErrorOutput()
        switch = {
            0: " + ",
            1: " - ",
            2: " * ",
            3: " / ",
        }
        self.contents.set(self.contents.get() + switch.get(index))
        self.entry.icursor(END)

    def clear(self):
        self.errorOutput.configure(state=NORMAL)
        self.errorOutput.delete(0.0, END)
        if self.contents.get() == '0 ' or self.contents.get() == '0':
            self.errorOutput.insert(END, 'ERROR: Already cleared!')
        else:
            self.contents.set('0 ')
        self.errorOutput.configure(state=DISABLED)

    def square(self):
        self.resetErrorOutput()
        self.contents.set(str(float(self.contents.get()) * float(self.contents.get())) + ' ')
        self.entry.icursor(END)

    def squareRoot(self):
        self.resetErrorOutput()
        self.contents.set(str(sqrt(float(self.contents.get()))) + ' ')
        self.entry.icursor(END)

    def enter(self, event=None):
        self.resetErrorOutput()
        self.parseString(str(self.eval_binary_expr(*(self.contents.get().split()))))

    def parseString(self, string):
        self.contents.set(string + ' ')
        self.entry.icursor(END)

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
            self.contents.set('0')
            self.errorOutput.configure(state=NORMAL)
            self.errorOutput.delete(0.0, END)
            self.errorOutput.insert(END, 'ERROR: Cannot divide by 0!')
            self.errorOutput.configure(state=DISABLED)
            return 0
        else:
            return self.get_operator_fn(operator)(op1, op2)
    # END

    def resetErrorOutput(self):
        self.errorOutput.configure(state=NORMAL)
        self.errorOutput.delete(0.0, END)
        self.errorOutput.configure(state=DISABLED)

    ### END FUNCTIONALITY ###

root = Tk()
app = App(root)
app.master.title("calculator")
app.master.resizable(width=False, height=False)
root.geometry('{}x{}'.format(192, 150))
app.mainloop()