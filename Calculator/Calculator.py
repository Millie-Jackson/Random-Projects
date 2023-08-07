
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
    [07.08.23]

Version:
    1.0
"""

from tkinter import *

root = Tk()
root.title("Calculator") # Title

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number) -> None:

    """
    Appends the clicked number to the current input in the entry widget.

    Parameters:
        number (int): The number clicked by the user.

    Returns:
        None
    """

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) # Stops it from add numbers together by making sure its a string

    return None

def button_clear() -> None:

    """
    Clears the entry widget.

    Parameters:
        None

    Returns:
        None
    """

    e.delete(0, END)

    return None

def button_add() -> None:

    """
    Prepares the calculator for addition by storing the first number, setting the operation,
    and clearing the entry widget.

    Parameters:
        None

    Returns:
        None
    """

    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

    return None

def button_subtract() -> None:

    """
    Prepares the calculator for subtraction by storing the first number, setting the operation,
    and clearing the entry widget.

    Parameters:
        None

    Returns:
        None
    """

    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

    return None

def button_multiply() -> None:

    """
    Prepares the calculator for multiplication by storing the first number, setting the operation,
    and clearing the entry widget.

    Parameters:
        None

    Returns:
        None
    """

    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

    return None

def button_divide() -> None:

    """
    Prepares the calculator for division by storing the first number, setting the operation,
    and clearing the entry widget.

    Parameters:
        None

    Returns:
        None
    """

    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

    return None

def button_equals() -> None:

    """
    Performs the selected arithmetic operation on the stored first number and the current
    number in the entry widget, then displays the result.

    Parameters:
        None

    Returns:
        None
    """

    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

    return None

# Define number buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg="gray", command=lambda:button_click(1)) # lambda to pass a parameter
button_2 = Button(root, text="2", padx=40, pady=20, bg="gray", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="gray", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="gray", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="gray", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="gray", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="gray", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="gray", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="gray", command=lambda: button_click(9))

button_0 = Button(root, text="0", padx=40, pady=20, bg="gray", command=lambda: button_click(0))

# Define function buttons
button_add = Button(root, text="+", padx=39, pady=20, bg="light yellow", command=button_add)
button_subtract = Button(root, text="-", padx=41, pady=20, bg="light yellow", command=button_subtract)
button_multiply = Button(root, text="*", padx=41, pady=20, bg="light yellow", command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, bg="light yellow", command=button_divide)

button_equals = Button(root, text="=", padx=91, pady=20, bg="light blue", command=button_equals)

button_clear = Button(root, text="Clear", padx=79, pady=20, bg="light blue", command=button_clear) # Not passing a parameter so no lambda needed



# Display buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_equals.grid(row=5, column=1, columnspan=2)

button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()

## TO DO ##
# Remove global variables