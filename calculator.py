from math import sqrt, log, log10, pi, e
import re
# import operator
from tkinter import *
import tkinter as tk
from error_messages import *


class Calculator(Frame):

    def __init__(self, master=None):
        """Initializes the GUI."""
        Frame.__init__(self, master)
        self.grid()
        self.create_fields()
        self.create_button_frame()

    def create_fields(self):
        """Creates the number field and the error field."""
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
        """Creates the button frame, and then calls three functions to create the buttons themselves."""
        self.button_frame = Frame(root)
        self.button_frame.grid(row=3, columnspan=5, sticky=W)

        self.create_basic_operands_buttons()
        self.create_other_math_buttons()
        self.create_clear_and_enter_buttons()

    def create_basic_operands_buttons(self):
        """Creates the five basic operand buttons: + - / * %"""
        self.addition_button = tk.Button(self.button_frame, text="+", command=lambda: self.append_basic_operand(0))
        self.addition_button.grid(row=3)

        self.minus_button = tk.Button(self.button_frame, text="-", command=lambda: self.append_basic_operand(1))
        self.minus_button.grid(row=3, column=1, sticky=W + E)

        self.multiply_button = tk.Button(self.button_frame, text="*", command=lambda: self.append_basic_operand(2))
        self.multiply_button.grid(row=3, column=2)

        self.divide_button = tk.Button(self.button_frame, text="/", command=lambda: self.append_basic_operand(3))
        self.divide_button.grid(row=3, column=3, sticky=W + E)

        self.modulus_button = tk.Button(self.button_frame, text="%", command=lambda: self.append_basic_operand(4))
        self.modulus_button.grid(row=4, column=4)

    def create_other_math_buttons(self):
        """Creates the rest of the math buttons."""
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
        """Creates the CLEAR and ENTER buttons."""
        self.clear_button = tk.Button(self.button_frame, text="C", command=self.clear)
        self.clear_button.grid(row=3, column=4, sticky=E)

        self.enter_button = tk.Button(self.button_frame, text="=", command=self.enter)
        self.enter_button.grid(row=5, column=4, sticky=E)

    def append_basic_operand(self, index):
        """Appends +, -, *, /, or % to the contents of the number field."""
        self.reset_error_output()
        switch = {
            0: " + ",
            1: " - ",
            2: " * ",
            3: " / ",
            4: " % ",
        }
        self.contents_of_number_field.set(self.contents_of_number_field.get() + switch.get(index))
        self.number_field.icursor(END)

    def square(self):
        """Directly squares the number in the contents of the number field."""
        self.reset_error_output()
        try:
            self.contents_of_number_field.set(str(pow(float(self.contents_of_number_field.get()), 2)) + ' ')
        except ValueError:
            self.print_error_message(1)
        self.number_field.icursor(END)

    def cube(self):
        """Directly cubes the number in the contents of the number field."""
        self.reset_error_output()
        try:
            self.contents_of_number_field.set(str(pow(float(self.contents_of_number_field.get()), 3)) + ' ')
        except ValueError:
            self.print_error_message(1)
        self.number_field.icursor(END)

    def square_root(self):
        """Directly takes the square root of the number in the contents of the number field."""
        self.reset_error_output()
        try:
            self.contents_of_number_field.set(str(sqrt(float(self.contents_of_number_field.get()))) + ' ')
        except ValueError:
            self.print_error_message(1)
        self.number_field.icursor(END)

    def insert_pi(self):
        """Appends a pi to the end of the contents of the number field."""
        self.reset_error_output()
        if len(self.contents_of_number_field.get()) == 0:
            self.contents_of_number_field.set(str(pi))
        else:
            self.contents_of_number_field.set(self.contents_of_number_field.get() + ' ' + str(pi))
        self.number_field.icursor(END)

    def insert_e(self):
        """Appends an e to the end of the contents of the number field."""
        self.reset_error_output()
        if len(self.contents_of_number_field.get()) == 0:
            self.contents_of_number_field.set(str(e))
        else:
            self.contents_of_number_field.set(self.contents_of_number_field.get() + ' ' + str(e))
        self.number_field.icursor(END)

    def ln(self):
        """Calculates the natural logarithm of the number in the contents of the number field."""
        self.reset_error_output()
        try:
            self.contents_of_number_field.set(str(log(float(self.contents_of_number_field.get()))) + ' ')
        except ValueError:
            self.print_error_message(1)
        self.number_field.icursor(END)

    def log_base_two(self):
        """Calculates log base two of the number in the contents of the number field."""
        self.reset_error_output()
        try:
            self.contents_of_number_field.set(str(log(float(self.contents_of_number_field.get()), 2)) + ' ')
        except ValueError:
            self.print_error_message(1)
        self.number_field.icursor(END)

    def log_base_ten(self):
        """Calculates log base ten of hte number in the contents of the number field."""
        self.reset_error_output()
        try:
            self.contents_of_number_field.set(str(log10(float(self.contents_of_number_field.get()))) + ' ')
        except ValueError:
            self.print_error_message(1)
        self.number_field.icursor(END)

    def clear(self):
        """Clears the contents of the number field as well as the error field."""
        self.error_field.configure(state=NORMAL)
        self.error_field.delete(0.0, END)
        if len(self.contents_of_number_field.get()) == 0:
            self.print_error_message(3)
        else:
            self.contents_of_number_field.set('')
        self.error_field.configure(state=DISABLED)

    def enter(self, event=None):
        """Calls the eval_expr() function and changes the contents of the number field to the return value."""
        self.reset_error_output()
        self.eval_expr()
        # string = str(self.eval_binary_expr(*(self.contents_of_number_field.get().split())))
        # self.parse_str_and_add_space(string)
        field_contents = str(self.eval_expr())
        if field_contents != "error":
            self.add_space_to_contents(field_contents)
        else:
            self.contents_of_number_field.set('')

    def add_space_to_contents(self, field_contents):
        """Appends a space to the field contents and moves the cursor to the end."""
        self.contents_of_number_field.set(field_contents + ' ')
        self.number_field.icursor(END)

    # def get_op(self, op):
    #     return {
    #         '+' : operator.add,
    #         '-' : operator.sub,
    #         '*' : operator.mul,
    #         '/' : operator.truediv,
    #         '%' : operator.mod,
    #     }[op]
    #
    # # can probably delete this, but I want to keep it
    # def eval_binary_expr(self, left_operand, op, right_operand):
    #     left_operand, right_operand = float(left_operand), float(right_operand)
    #     if operator == '/' and right_operand == 0:
    #         self.contents_of_number_field.set('')
    #         self.print_error_message(2)
    #         return 0
    #     else:
    #         return self.get_op(op)(left_operand, right_operand)

    def eval_expr(self):
        """Parses the string in the number field and calculates the expression from left to right."""
        try:
            field_contents = self.contents_of_number_field.get()
            field_contents = re.sub('\s+', '', field_contents)
            field_contents = re.split('(-|\+)', field_contents)

            # src: https://gist.github.com/cammckinnon/3971894
            def solve_term(string):
                string = re.split('(/|\*|%)', string)
                ret = float(string[0])
                for op, num in zip(string[1::2], string[2::2]):
                    num = float(num)
                    if op == '*':
                        ret *= num
                    elif op == '/':
                        if num != 0:
                            ret /= num
                        else:
                            self.print_error_message(2)
                            return "error"
                    else:
                        if num != 0:
                            ret %= num
                        else:
                            self.print_error_message(2)
                            return "error"

                return ret

            result = solve_term(field_contents[0])

            for op, num in zip(field_contents[1::2], field_contents[2::2]):
                result += solve_term(num) * (1 if op == '+' else -1)

            return result
        except ValueError:
            self.print_error_message(0)
            return "error"

    def print_error_message(self, index):
        """Resets the error output and inserts an error message corresponding to the index given."""
        self.error_field.configure(state=NORMAL)
        self.error_field.delete(0.0, END)
        self.error_field.insert(END, return_error_message(self, index))
        self.error_field.configure(state=DISABLED)

    def reset_error_output(self):
        """Resets the error output and disables it."""
        self.error_field.configure(state=NORMAL)
        self.error_field.delete(0.0, END)
        self.error_field.configure(state=DISABLED)

root = Tk()
app = Calculator(root)
app.master.title("simple calculator")
app.master.resizable(width=False, height=False)
root.geometry('{}x{}'.format(195, 150))
app.mainloop()