from math import sqrt, log, log10, pi, e
import re
import operator
from tkinter import *
import tkinter as tk


class Calculator(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_fields()
        self.create_button_frame()

    def create_fields(self):
        self.number_field = Entry()
        self.number_field.grid(row=0, sticky=W)
        self.contents_of_number_field = StringVar()
        self.number_field["textvariable"] = self.contents_of_number_field
        self.number_field.focus_set()
        self.number_field.icursor(END)
        self.number_field.bind('<Key-Return>', self.enter)

        self.error_field = Text(height=1)
        self.error_field.config(state=DISABLED)
        self.error_field.grid(row=1, sticky=N+E+S+W)

    def create_button_frame(self):
        self.button_frame = Frame(root)
        self.button_frame.grid(row=3, columnspan=5, sticky=W)

        self.create_basic_operands_buttons()
        self.create_other_math_buttons()
        self.create_clear_and_enter_buttons()

    def create_basic_operands_buttons(self):
        self.addition_button = tk.Button(self.button_frame, text="+", command=lambda: self.append_basic_operand(0))
        self.addition_button.grid(row=3)

        self.minus_button = tk.Button(self.button_frame, text="-", command=lambda: self.append_basic_operand(1))
        self.minus_button.grid(row=3, column=1, sticky=W + E)

        self.multiply_button = tk.Button(self.button_frame, text="*", command=lambda: self.append_basic_operand(2))
        self.multiply_button.grid(row=3, column=2)

        self.divide_button = tk.Button(self.button_frame, text="/", command=lambda: self.append_basic_operand(3))
        self.divide_button.grid(row=3, column=3, sticky=W + E)

    def create_other_math_buttons(self):
        self.square_button = tk.Button(self.button_frame, text="²", command=self.square)
        self.square_button.grid(row=4)

        self.cube_button = tk.Button(self.button_frame, text="³", command=self.cube)
        self.cube_button.grid(row=4, column=1)

        self.sqrt_button = tk.Button(self.button_frame, text="√", font="Arial 9", command=self.square_root)
        self.sqrt_button.grid(row=4, column=2, sticky=W + E)

        self.pi_button = tk.Button(self.button_frame, text="π", command=self.insert_pi)
        self.pi_button.grid(row=4, column=3)

        self.e_button = tk.Button(self.button_frame, text="e", font="Arial 9", command=self.insert_e)
        self.e_button.grid(row=5)

        self.ln_button = tk.Button(self.button_frame, text="ln", font="Arial 9", command=self.ln)
        self.ln_button.grid(row=5, column=1)

        self.log_base_two_button = tk.Button(self.button_frame, text="lg₂ ", font="Arial 9", command=self.log_base_two)
        self.log_base_two_button.grid(row=5, column=2)

        self.log_base_ten_button = tk.Button(self.button_frame, text="lg₁₀", font="Arial 9", command=self.log_base_ten)
        self.log_base_ten_button.grid(row=5, column=3)

    def create_clear_and_enter_buttons(self):
        self.clear_button = tk.Button(self.button_frame, text="C", command=self.clear)
        self.clear_button.grid(row=3, column=4, sticky=E)

        self.enter_button = tk.Button(self.button_frame, text="=", command=self.enter)
        self.enter_button.grid(row=5, column=4, sticky=E)

    def append_basic_operand(self, index):
        self.reset_error_output()
        switch = {
            0: " + ",
            1: " - ",
            2: " * ",
            3: " / ",
        }
        self.contents_of_number_field.set(self.contents_of_number_field.get() + switch.get(index))
        self.number_field.icursor(END)

    def square(self):
        self.reset_error_output()
        self.contents_of_number_field.set(str(pow(float(self.contents_of_number_field.get()), 2)) + ' ')
        self.number_field.icursor(END)

    def cube(self):
        self.reset_error_output()
        self.contents_of_number_field.set(str(pow(float(self.contents_of_number_field.get()), 3)) + ' ')
        self.number_field.icursor(END)

    def square_root(self):
        self.reset_error_output()
        self.contents_of_number_field.set(str(sqrt(float(self.contents_of_number_field.get()))) + ' ')
        self.number_field.icursor(END)

    def insert_pi(self):
        self.reset_error_output()
        if len(self.contents_of_number_field.get()) == 0:
            self.contents_of_number_field.set(str(pi))
        else:
            self.contents_of_number_field.set(self.contents_of_number_field.get() + ' ' + str(pi))
        self.number_field.icursor(END)

    def insert_e(self):
        self.reset_error_output()
        if len(self.contents_of_number_field.get()) == 0:
            self.contents_of_number_field.set(str(e))
        else:
            self.contents_of_number_field.set(self.contents_of_number_field.get() + ' ' + str(e))
        self.number_field.icursor(END)

    def ln(self):
        self.reset_error_output()
        self.contents_of_number_field.set(str(log(float(self.contents_of_number_field.get()))) + ' ')
        self.number_field.icursor(END)

    def log_base_two(self):
        self.reset_error_output()
        self.contents_of_number_field.set(str(log(float(self.contents_of_number_field.get()), 2)) + ' ')
        self.number_field.icursor(END)

    def log_base_ten(self):
        self.reset_error_output()
        self.contents_of_number_field.set(str(log10(float(self.contents_of_number_field.get()))) + ' ')
        self.number_field.icursor(END)

    def clear(self):
        self.error_field.configure(state=NORMAL)
        self.error_field.delete(0.0, END)
        if len(self.contents_of_number_field.get()) == 0:
            self.error_field.insert(END, 'ERROR: Already cleared!')
        else:
            self.contents_of_number_field.set('')
        self.error_field.configure(state=DISABLED)

    def enter(self, event=None):
        self.reset_error_output()
        self.eval_expr()
        # string = str(self.eval_binary_expr(*(self.contents_of_number_field.get().split())))
        # self.parse_str_and_add_space(string)
        field_contents = str(self.eval_expr())
        self.parse_str_and_add_space(field_contents)

    def parse_str_and_add_space(self, field_contents):
        self.contents_of_number_field.set(field_contents + ' ')
        self.number_field.icursor(END)

    def get_op(self, op):
        return {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
        }[op]

    # can probably delete this, but I want to keep it
    def eval_binary_expr(self, left_operand, op, right_operand):
        left_operand, right_operand = float(left_operand), float(right_operand)
        if operator == '/' and right_operand == 0:
            self.contents_of_number_field.set('')
            self.error_field.configure(state=NORMAL)
            self.error_field.delete(0.0, END)
            self.error_field.insert(END, 'ERROR: Cannot divide by 0!')
            self.error_field.configure(state=DISABLED)
            return 0
        else:
            return self.get_op(op)(left_operand, right_operand)

    def eval_expr(self):
        try:
            field_contents = self.contents_of_number_field.get()
            field_contents = re.sub('\s+', '', field_contents)
            field_contents = re.split('(-|\+)', field_contents)

            # src: https://gist.github.com/cammckinnon/3971894
            def solve_term(string):
                string = re.split('(/|\*)', string)
                ret = float(string[0])
                for op, num in zip(string[1::2], string[2::2]):
                    num = float(num)
                    if op == '*':
                        ret *= num
                    else:
                        if num != 0:
                            ret /= num
                        else:
                            self.error_field.configure(state=NORMAL)
                            self.error_field.delete(0.0, END)
                            self.error_field.insert(END, 'ERROR: Cannot divide by 0!')
                            self.error_field.configure(state=DISABLED)
                            return 0
                return ret

            result = solve_term(field_contents[0])

            for op, num in zip(field_contents[1::2], field_contents[2::2]):
                result += solve_term(num) * (1 if op == '+' else -1)

            return result
        except ValueError:
            self.error_field.configure(state=NORMAL)
            self.error_field.delete(0.0, END)
            self.error_field.insert(END, 'ERROR: Invalid expression!')
            self.error_field.configure(state=DISABLED)
            self.contents_of_number_field.set('')
            return 0

    def reset_error_output(self):
        self.error_field.configure(state=NORMAL)
        self.error_field.delete(0.0, END)
        self.error_field.configure(state=DISABLED)

root = Tk()
app = Calculator(root)
app.master.title("simple calculator")
app.master.resizable(width=False, height=False)
root.geometry('{}x{}'.format(192, 150))
app.mainloop()