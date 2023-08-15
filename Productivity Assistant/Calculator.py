
"""
Calculator GUI

This script implements a basic calculator graphical user interface (GUI) using the tkinter library in Python.
The calculator supports addition, subtraction, multiplication, and division operations on integers.

Usage:
    - Click the number buttons (0-9) to input digits into the calculator.
    - Click the "+" button to perform addition.
    - Click the "-" button to perform subtraction.
    - Click the "*" button to perform multiplication.
    - Click the "/" button to perform division.
    - Click the "=" button to display the result of the selected operation.
    - Click the "Clear" button to reset the calculator for a new calculation.

Functions:
    - button_click(number):
        Appends the clicked number to the current input in the entry widget.

    - button_clear():
        Clears the entry widget.

    - button_add():
        Prepares the calculator for addition by storing the first number, setting the operation,
        and clearing the entry widget.

    - button_subtract():
        Prepares the calculator for subtraction by storing the first number, setting the operation,
        and clearing the entry widget.

    - button_multiply():
        Prepares the calculator for multiplication by storing the first number, setting the operation,
        and clearing the entry widget.

    - button_divide():
        Prepares the calculator for division by storing the first number, setting the operation,
        and clearing the entry widget.

    - button_equals():
        Performs the selected arithmetic operation on the stored first number and the current
        number in the entry widget, then displays the result.

Please note:
    - The calculator only works with integer numbers.
    - The "Clear" button resets the calculator, but no undo functionality is provided.
    - Division by zero is not handled.

Author:
    [Millie J]

Date:
    [15.08.23]

Version:
    0.1
"""

import tkinter as tk # for UI

class Calculator:
    def __init__(self, root):
        self.root = root

        #UI
        self.e = tk.Entry(root, width=35, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Define number buttons
        self.button_1 = tk.Button(root, text="1", padx=40, pady=20, bg="gray", command=lambda: self.button_click(1)) # lambda to pass a parameter
        self.button_2 = tk.Button(root, text="2", padx=40, pady=20, bg="gray", command=lambda: self.button_click(2))
        self.button_3 = tk.Button(root, text="3", padx=40, pady=20, bg="gray", command=lambda: self.button_click(3))
        self.button_4 = tk.Button(root, text="4", padx=40, pady=20, bg="gray", command=lambda: self.button_click(4))
        self.button_5 = tk.Button(root, text="5", padx=40, pady=20, bg="gray", command=lambda: self.button_click(5))
        self.button_6 = tk.Button(root, text="6", padx=40, pady=20, bg="gray", command=lambda: self.button_click(6))
        self.button_7 = tk.Button(root, text="7", padx=40, pady=20, bg="gray", command=lambda: self.button_click(7))
        self.button_8 = tk.Button(root, text="8", padx=40, pady=20, bg="gray", command=lambda: self.button_click(8))
        self.button_9 = tk.Button(root, text="9", padx=40, pady=20, bg="gray", command=lambda: self.button_click(9))

        self.button_0 = tk.Button(root, text="0", padx=40, pady=20, bg="gray", command=lambda: self.button_click(0))

        # Define function buttons
        self.button_add = tk.Button(root, text="+", padx=39, pady=20, bg="light yellow", command=self.button_add)
        self.button_subtract = tk.Button(root, text="-", padx=41, pady=20, bg="light yellow", command=self.button_subtract)
        self.button_multiply = tk.Button(root, text="*", padx=41, pady=20, bg="light yellow", command=self.button_multiply)
        self.button_divide = tk.Button(root, text="/", padx=41, pady=20, bg="light yellow", command=self.button_divide)

        self.button_equals = tk.Button(root, text="=", padx=91, pady=20, bg="light blue", command=self.button_equals)

        self.button_clear = tk.Button(root, text="Clear", padx=79, pady=20, bg="light blue", command=self.button_clear) # Not passing a parameter so no lambda needed

        # Display buttons
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)

        self.button_0.grid(row=4, column=0)

        self.button_add.grid(row=5, column=0)
        self.button_subtract.grid(row=6, column=0)
        self.button_multiply.grid(row=6, column=1)
        self.button_divide.grid(row=6, column=2)

        self.button_equals.grid(row=5, column=1, columnspan=2)

        self.button_clear.grid(row=4, column=1, columnspan=2)



    def button_click(self, number) -> None:

        """
        Appends the clicked number to the current input in the entry widget.

        Parameters:
            number (int): The number clicked by the user.

        Returns:
            None
        """

        current = self.e.get()
        self.e.delete(0, tk.END)
        self.e.insert(0, str(current) + str(number)) # Stops it from add numbers together by making sure its a string

        return None

    def button_clear(self) -> None:

        """
        Clears the entry widget.

        Parameters:
            None

        Returns:
            None
        """

        self.e.delete(0, tk.END)

        return None

    def button_add(self) -> None:

        """
        Prepares the calculator for addition by storing the first number, setting the operation,
        and clearing the entry widget.

        Parameters:
            None

        Returns:
            None
        """

        first_number = self.e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        self.e.delete(0, tk.END)

        return None

    def button_subtract(self) -> None:

        """
        Prepares the calculator for subtraction by storing the first number, setting the operation,
        and clearing the entry widget.

        Parameters:
            None

        Returns:
            None
        """

        first_number = self.e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        self.e.delete(0, tk.END)

        return None

    def button_multiply(self) -> None:

        """
        Prepares the calculator for multiplication by storing the first number, setting the operation,
        and clearing the entry widget.

        Parameters:
            None

        Returns:
            None
        """

        first_number = self.e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        self.e.delete(0, tk.END)

        return None

    def button_divide(self) -> None:

        """
        Prepares the calculator for division by storing the first number, setting the operation,
        and clearing the entry widget.

        Parameters:
            None

        Returns:
            None
        """

        first_number = self.e.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        self.e.delete(0, tk.END)

        return None

    def button_equals(self) -> None:

        """
        Performs the selected arithmetic operation on the stored first number and the current
        number in the entry widget, then displays the result.

        Parameters:
            None

        Returns:
            None
        """

        second_number = self.e.get()
        self.e.delete(0, tk.END)

        if math == "addition":
            self.e.insert(0, f_num + int(second_number))
        if math == "subtraction":
            self.e.insert(0, f_num - int(second_number))
        if math == "multiplication":
            self.e.insert(0, f_num * int(second_number))
        if math == "division":
            self.e.insert(0, f_num / int(second_number))

        return None


## TO DO ##
# Remove global variables