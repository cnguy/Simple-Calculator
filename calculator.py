from math import sqrt, log, log10, pi, e
import operator
from tkinter import *
import tkinter as tk


class Calculator(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.entry = Entry()
        self.entry.grid(row=0, sticky=W)
        self.contents = StringVar()
        self.entry["textvariable"] = self.contents
        self.entry.focus_set()
        self.entry.icursor(END)
        self.entry.bind('<Key-Return>', self.enter)

        self.error_output = Text(height=1)
        self.error_output.config(state=DISABLED)
        self.error_output.grid(row=1, sticky=N + E + S + W)

        self.button_frame = Frame(root)
        self.button_frame.grid(row=3, columnspan=5, sticky=W)

        self.additionButton = tk.Button(self.button_frame, text="+", command=lambda: self.append_basic_operand(0))
        self.additionButton.grid(row=3)
        self.minusButton = tk.Button(self.button_frame, text="-", command=lambda: self.append_basic_operand(1))
        self.minusButton.grid(row=3, column=1, sticky=W+E)
        self.multiplyButton = tk.Button(self.button_frame, text="*", command=lambda: self.append_basic_operand(2))
        self.multiplyButton.grid(row=3, column=2)
        self.divideButton = tk.Button(self.button_frame, text="/", command=lambda: self.append_basic_operand(3))
        self.divideButton.grid(row=3, column=3, sticky=W+E)

        self.clearButton = tk.Button(self.button_frame, text="C", command=self.clear)
        self.clearButton.grid(row=3, column=4, sticky=E)

        self.squareButton = tk.Button(self.button_frame, text="²", command=self.square)
        self.squareButton.grid(row=4)

        self.cubeButton = tk.Button(self.button_frame, text="³", command=self.cube)
        self.cubeButton.grid(row=4, column=1)

        self.squareRootButton = tk.Button(self.button_frame, text="√", font="Arial 9", command=self.squareRoot)
        self.squareRootButton.grid(row=4, column=2, sticky=W+E)

        self.piButton = tk.Button(self.button_frame, text="π", command=self.pi)
        self.piButton.grid(row=4, column=3)

        self.eButton = tk.Button(self.button_frame, text="e", font="Arial 9", command=self.e)
        self.eButton.grid(row=5)

        self.lnButton = tk.Button(self.button_frame, text="ln", font="Arial 9", command=self.ln)
        self.lnButton.grid(row=5, column=1)

        self.logTwoButton = tk.Button(self.button_frame, text="lg₂ ", font="Arial 9", command=self.logTwo)
        self.logTwoButton.grid(row=5, column=2)

        self.logTenButton = tk.Button(self.button_frame, text="lg₁₀", font="Arial 9", command=self.logTen)
        self.logTenButton.grid(row=5, column=3)

        self.enterButton = tk.Button(self.button_frame, text="=", command=self.enter)
        self.enterButton.grid(row=5, column=4, sticky=E)

    def append_basic_operand(self, index):
        self.reset_error_output()
        switch = {
            0: " + ",
            1: " - ",
            2: " * ",
            3: " / ",
        }
        self.contents.set(self.contents.get() + switch.get(index))
        self.entry.icursor(END)

    def clear(self):
        self.error_output.configure(state=NORMAL)
        self.error_output.delete(0.0, END)
        if len(self.contents.get()) == 0:
            self.error_output.insert(END, 'ERROR: Already cleared!')
        else:
            self.contents.set('')
        self.error_output.configure(state=DISABLED)

    def square(self):
        self.reset_error_output()
        self.contents.set(str(pow(float(self.contents.get()), 2)) + ' ')
        self.entry.icursor(END)

    def cube(self):
        self.reset_error_output()
        self.contents.set(str(pow(float(self.contents.get()), 3)) + ' ')
        self.entry.icursor(END)

    def squareRoot(self):
        self.reset_error_output()
        self.contents.set(str(sqrt(float(self.contents.get()))) + ' ')
        self.entry.icursor(END)

    def pi(self):
        self.reset_error_output()
        if len(self.contents.get()) == 0:
            self.contents.set(str(pi))
        else:
            self.contents.set(self.contents.get() + ' ' + str(pi))
        self.entry.icursor(END)

    def e(self):
        self.reset_error_output()
        if len(self.contents.get()) == 0:
            self.contents.set(str(e))
        else:
            self.contents.set(self.contents.get() + ' ' + str(e))
        self.entry.icursor(END)

    def ln(self):
        self.reset_error_output()
        self.contents.set(str(log(float(self.contents.get()))) + ' ')
        self.entry.icursor(END)

    def logTwo(self):
        self.reset_error_output()
        self.contents.set(str(log(float(self.contents.get()), 2)) + ' ')
        self.entry.icursor(END)

    def logTen(self):
        self.reset_error_output()
        self.contents.set(str(log10(float(self.contents.get()))) + ' ')
        self.entry.icursor(END)

    def enter(self, event=None):
        self.reset_error_output()
        self.parse_str(str(self.eval_binary_expr(*(self.contents.get().split()))))

    def parse_str(self, string):
        self.contents.set(string + ' ')
        self.entry.icursor(END)

    def get_op(self, op):
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
            self.error_output.configure(state=NORMAL)
            self.error_output.delete(0.0, END)
            self.error_output.insert(END, 'ERROR: Cannot divide by 0!')
            self.error_output.configure(state=DISABLED)
            return 0
        else:
            return self.get_op(operator)(op1, op2)

    def reset_error_output(self):
        self.error_output.configure(state=NORMAL)
        self.error_output.delete(0.0, END)
        self.error_output.configure(state=DISABLED)

root = Tk()
app = Calculator(root)
app.master.title("simple calculator")
app.master.resizable(width=False, height=False)
root.geometry('{}x{}'.format(192, 150))
app.mainloop()