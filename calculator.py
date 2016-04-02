#!/usr/bin/env python3
# SORRY FOR THIS MESSY CODE AND BAD VARIABLE NAMES AND ALL THAT. I'm just learning and having fun!
# I will refactor the code and clean up everything once I get comfortable. :]
# For educational purposes only. Created with the amazing PyCharm!
# I'll break you until you're mine.
# I'll admit I did 60% trial-and-error, and 40% reading the documentation / searching up questions.

from tkinter import * # Frame, Entry, DoubleVar
import tkinter as tk
from math import sqrt

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # self.pack()
        self.grid()
        self.createWidgets()

        # self.entrythingy = Entry()
        # self.entrythingy.pack()
        #
        # # here is the application variable
        # self.contents = StringVar()
        # # set it to some value
        # self.contents.set("this is a variable")
        # # tell the entry widget to watch this variable
        # self.entrythingy["textvariable"] = self.contents
        #
        # # and here we get a callback when the user hits return.
        # # we will have the program print out the value of the
        # # application variable when the user hits return
        # self.entrythingy.bind('<Key-Return>',
        #                       self.print_contents)

        # # Numbers
        # self.numberthingy = Entry()
        # self.numberthingy.pack()
        #
        # # here is the application variable
        # self.contents = DoubleVar()
        # # set it to some value
        # self.contents.set(0)
        # # tell the entry widget to watch this variable
        # self.numberthingy["textvariable"] = self.contents
        #
        # self.numberthingy.bind('<Key-Return>',
        #                        self.print_square)

    def createWidgets(self):
        # TWO TEXT FIELDS FOR MULTIPLYING
        self.firstNumberField = Entry()
        # self.firstNumberField.pack()
        self.firstNumberField.grid(row=0) # columnspan=80, sticky=W

        self.firstNumberFieldContents = DoubleVar()
        self.firstNumberFieldContents.set(0.0)
        self.firstNumberField["textvariable"] = self.firstNumberFieldContents

        self.secondNumberField = Entry()
        # self.secondNumberField.pack()
        self.secondNumberField.grid(row=1) # , columnspan=80, sticky=W

        self.secondNumberFieldContents = DoubleVar()
        self.secondNumberFieldContents.set(0.0)
        self.secondNumberField["textvariable"] = self.secondNumberFieldContents

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # # self.hi_there.pack(side="top")
        # self.hi_there.grid(row=5)

        self.buttonFrame = Frame(root)
        self.buttonFrame.grid(row=2, column=0, columnspan=5)

        self.additionButton = tk.Button(self.buttonFrame)
        self.additionButton.grid(row=2, column=0, sticky=W+E) # , sticky=W
        self.additionButton["text"] = "+"
        self.additionButton["command"] = self.add
        # self.additionButton.pack(side="left")

        self.minusButton = tk.Button(self.buttonFrame)
        self.minusButton.grid(row=2, column=1, sticky=W+E) # , sticky=W
        self.minusButton["text"] = "-"
        self.minusButton["command"] = self.minus
        #self.minusButton.pack(side="left")

        self.multiplyButton = tk.Button(self.buttonFrame)
        self.multiplyButton.grid(row=2, column=2, sticky=W) # , sticky=W
        self.multiplyButton["text"] = "*"
        self.multiplyButton["command"] = self.multiply
        # self.multiplyButton.pack(side="left")

        self.divideButton = tk.Button(self.buttonFrame)
        self.divideButton.grid(row=2, column=3, sticky=W) # , sticky=W
        self.divideButton["text"] = "/"
        self.divideButton["command"] = self.divide
        # self.divideButton.pack(side="left")

        self.clearButton = tk.Button(self.buttonFrame)
        self.clearButton.grid(row=2, column=4, sticky=W)  # , sticky=W
        self.clearButton["text"] = "CE"
        self.clearButton["command"] = self.clear

        self.squareButton = tk.Button(self.buttonFrame)
        self.squareButton.grid(row=3, sticky=W) # , sticky=W
        self.squareButton["text"] = "^2"
        self.squareButton["command"] = self.square
        # # self.squareButton.pack(side="left")

        self.squareRootButton = tk.Button(self.buttonFrame)
        self.squareRootButton.grid(row=3, column=1, sticky=W) # , sticky=E
        self.squareRootButton["text"] = "sqrt"
        self.squareRootButton["command"] = self.squareRoot

        self.output = Text(height=1)
        self.output.config(state=DISABLED)
        self.output.grid(row=4, column=0, sticky=N+E+S+W)

        #
        # self.backgroundColorToBlackButton = tk.Button(self)
        # self.backgroundColorToBlackButton["text"] = "Black"
        # self.backgroundColorToBlackButton.bind("<Enter>", self.changeBackgroundColorToBlack)
        # # self.backgroundColorToBlackButton.pack(side="bottom")
        # self.backgroundColorToBlackButton.grid(row=4)
        #
        # self.QUIT = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy)
        # self.quitButton = tk.Button(self, text="quit", command=root.destroy)
        # self.quitButton.pack(side="bottom")

    # def print_contents(self, event):
    #     print("hi. contents of entry is now ---->",
    #           self.contents.get())

    # def print_square(self, event):
    #     print(self.contents.get() * self.contents.get())

    # def say_hi(self):
    #     print("hi there, everyone!")

    def add(self):
        self.output.configure(state=NORMAL)
        self.output.delete(0.0, END)
        print(self.firstNumberFieldContents.get() + self.secondNumberFieldContents.get())
        self.output.insert(END, str(self.firstNumberFieldContents.get() + self.secondNumberFieldContents.get()))
        self.output.configure(state=DISABLED)

    def minus(self):
        self.output.configure(state=NORMAL)
        self.output.delete(0.0, END)
        print(self.firstNumberFieldContents.get() - self.secondNumberFieldContents.get())
        self.output.insert(END, str(self.firstNumberFieldContents.get() - self.secondNumberFieldContents.get()))
        self.output.configure(state=DISABLED)

    def multiply(self):
        self.output.configure(state=NORMAL)
        self.output.delete(0.0, END)
        print(self.firstNumberFieldContents.get() * self.secondNumberFieldContents.get())
        self.output.insert(END, str(self.firstNumberFieldContents.get() * self.secondNumberFieldContents.get()))
        self.output.configure(state=DISABLED)

    def divide(self):
        self.output.configure(state=NORMAL)
        self.output.delete(0.0, END)
        if self.secondNumberFieldContents.get() == 0:
            print('Cannot divide by 0!')
            self.output.insert(END, 'Cannot divide by 0!')
        else:
            print(self.firstNumberFieldContents.get() / self.secondNumberFieldContents.get())
            self.output.insert(END, str(self.firstNumberFieldContents.get() / self.secondNumberFieldContents.get()))
        self.output.configure(state=DISABLED)

    def clear(self):
        if self.firstNumberFieldContents.get() == 0 and self.secondNumberFieldContents.get() == 0:
            self.output.configure(state=NORMAL)
            self.output.delete(0.0, END)
            self.output.insert(END, 'Already cleared!')
            self.output.configure(state=DISABLED)
        else:
            self.firstNumberFieldContents.set(0.0)
            self.secondNumberFieldContents.set(0.0)

    def square(self):
        self.output.configure(state=NORMAL)
        self.output.delete(0.0, END)
        print(self.firstNumberFieldContents.get() * self.firstNumberFieldContents.get())
        self.output.insert(END, str(self.firstNumberFieldContents.get() * self.firstNumberFieldContents.get()))
        self.output.configure(state=DISABLED)

    def squareRoot(self):
        self.output.configure(state=NORMAL)
        self.output.delete(0.0, END)
        print(sqrt(self.firstNumberFieldContents.get()))
        self.output.insert(END, str(sqrt(self.firstNumberFieldContents.get())))
        self.output.configure(state=DISABLED)

    # def changeBackgroundColorToBlack(self, event):
    #     self.event.widget["activeforeground"] = "black"

root = Tk()
# root.grid_columnconfigure(0, weight=1)
app = App(root)
app.master.title("My Calculator")
# app.master.maxsize(480, 600)
app.master.resizable(width=False, height=False)
app.master.size()
app.master.minsize(200, 200)
app.mainloop()