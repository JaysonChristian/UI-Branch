from tkinter import*
import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False


add_value = Calc()
root = Tk()
root.title("Project Casio")
root.resizable(width = False, height = False)
calc = Frame(root)
calc.grid()

# this represents the button/s in the calculator

txtDisplay = Entry(calc, font=("arial", 18, "bold"), bg="powder blue", bd=30, width = 28, justify = RIGHT)
txtDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0, "0")

# ------------------------------ /Row 1/ --------------------------------

btnAllClear = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "AC", bg="orange").grid(row = 1, column = 0)

btnDelete = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "DEL", bg="orange").grid(row = 1, column = 1)

btnSqroot = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "√").grid(row = 1, column = 2)

btnAdd = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "+").grid(row = 1, column = 3)

# ------------------------------- /Row 2/ --------------------------------

btn7 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "7", bg="powder blue").grid(row = 2, column = 0)

btn8 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "8", bg="powder blue").grid(row = 2, column = 1)

btn9 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "9", bg="powder blue").grid(row = 2, column = 2)

btnSubtract = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "-").grid(row = 2, column = 3)

# ------------------------------- /Row 3/ --------------------------------

btn4 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "4", bg="powder blue").grid(row = 3, column = 0)

btn5 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "5", bg="powder blue").grid(row = 3, column = 1)

btn6 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "6", bg="powder blue").grid(row = 3, column = 2)

btnMultiply = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "x").grid(row = 3, column = 3)

# ------------------------------- /Row 4/ --------------------------------

btn1 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "1", bg="powder blue").grid(row = 4, column = 0)

btn2 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "2", bg="powder blue").grid(row = 4, column = 1)

btn3 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "3", bg="powder blue").grid(row = 4, column = 2)

btnDivide = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "÷").grid(row = 4, column = 3)

# ------------------------------- /Row 5/ --------------------------------

btn0 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "0", bg="powder blue").grid(row = 5, column = 0)

btnDot = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = ".").grid(row = 5, column = 1)

btnPM = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "±").grid(row = 5, column = 2)

btnEquals = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "=").grid(row = 5, column = 3)


root.mainloop()