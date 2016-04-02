#!/usr/bin/env python3

from tkinter import *
import tkinter as tk

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
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

         # Numbers
        self.numberthingy = Entry()
        self.numberthingy.pack()

        # here is the application variable
        self.contents = DoubleVar()
        # set it to some value
        self.contents.set(0)
        # tell the entry widget to watch this variable
        self.numberthingy["textvariable"] = self.contents

        self.numberthingy.bind('<Key-Return>',
                               self.print_square)

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.QUIT.pack(side="bottom")

    def print_contents(self, event):
        print("hi. contents of entry is now ---->",
              self.contents.get())

    def print_square(self, event):
        print(self.contents.get() * self.contents.get())

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
my_app = App(master=root)
my_app.master.title("Generic App")
my_app.master.maxsize(800, 600)

my_app.mainloop()