operator = input("Give The Arithmetic Operation: ")
if operator not in ("+", "-", "*", "/"):
    print("Wrong input")
else:
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
         print(num1 * num2)
    case "/":
        if num2 == 0:
            print("Division by zero is not allowed")
        else:
            print(num1 / num2)
    case _:
        print("Invalid input")