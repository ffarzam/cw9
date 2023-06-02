from operations.addition import add
from operations.subtraction import subtraction
from operations.division import division
from operations.multiplication import multi

while True:
    while True:
        op=input("Enter the chosen operator (+ - * /) or e to Exit: ")

        if op not in ["+","-","*","/","e"]:
            print("Enter a valid option")
        else:
            break
    if op == "e":
        break

    x = float(input("Enter your first number: "))
    y = float(input("Enter your first number: "))

    if op == "+":
        print(add(x,y))
    elif op == "-":
        print(subtraction(x, y))
    elif op == "*":
        print(multi(x, y))
    elif op == "/":
        print(division(x, y))



