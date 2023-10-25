# To check the version of your python interpreter
"""import os as o
o.system("python --version")"""

# Match Case Statement
# operator = input("Give The Arithmetic Operation")
# if operator != "+" or "-" or "*" or "/":
#     print("Wrong input")
# else:
#     num1 = int(input("Give the first number"))
#     num2 = int(input("Give the second number"))
#
#     match operator:
#         case "+":
#             print(num1 + num2)
#         case "-":
#             print(num1 - num2)
#         case "*":
#             print(num1 * num2)
#         case "/":
#             print(num1 / num2)




# operator = input("Give The Arithmetic Operation: ")
# if operator not in ("+", "-", "*", "/"):
#     print("Wrong input")
# else:
# num1 = int(input("Give the first number: "))
# num2 = int(input("Give the second number: "))
#
# match operator:
#     case "+":
#         print(num1 + num2)
#     case "-":
#         print(num1 - num2)
#     case "*":
#          print(num1 * num2)
#     case "/":
#         if num2 == 0:
#             print("Division by zero is not allowed")
#         else:
#             print(num1 / num2)
#     case _:
#         print("Invalid input")




# a = int(input("give the number"))
# match a:
#     # if a is 0
#     case 0:
#         print("THe number is 0")
#     #  case with if condition
#     case 4 if a% 2 ==0: #it checks whether the number 4 is even or not
#         print(" a%2 == 0 and case is 4")
# Empty case with if condition
# case _ if a<10:
#     # IT is basically just an else:
#     # default case will only be matched if the above cases are not matched
#     # It is not necessary to use default case or empty case as in languages such as C, C++ etc.
#     print("a is <10")
# case _:
#     print(a)

# code to calculate grade
"""def calculate_grade(score):
    match score:
        case _ if score >= 90:
            return "A"
        case _ if score >= 80:
            return "B"
        case _ if score >= 70:
            return "C"
        case _ if score >= 60:
            return "D"
        case _:
             return "F"


score = float(input("Enter the student's score: "))
grade = calculate_grade(score)
print(f"The student's grade is: {grade}")"""





"""def int_to_roman(n):
    match n:
        case 1:
            return "I"
        case 2:
            return "II"
        case 3:
            return "III"
        case 4:
            return "IV"
        case 5:
            return "V"
        case 6:
            return "VI"
        case 7:
            return "VII"
        case 8:
            return "VIII"
        case 9:
            return "IX"
        case 10:
            return "X"
        case 20:
            return "XX"
        case 30:
            return "XXX"
        case 40:
            return "XL"
        case 50:
            return "L"
        case 60:
            return "LX"
        case 70:
            return "LXX"
        case 80:
            return "LXXX"
        case 90:
            return "XC"
        case 100:
            return "C"
        case 200:
            return "CC"
        case 300:
            return "CCC"
        case 400:
            return "CD"
        case 500:
            return "D"
        case 600:
            return "DC"
        case 700:
            return "DCC"
        case 800:
            return "DCCC"
        case 900:
            return "CM"
        case 1000:
            return "M"
        case 2000:
            return "MM"
        case 3000:
            return "MMM"
        case _:
            return "Invalid input"

num = int(input("Enter an integer (1-3999): "))
if 1 <= num <= 3999:
    roman_numeral = int_to_roman(num)
    print(f"The Roman numeral for {num} is {roman_numeral}")
else:
    print("Please enter an integer within the specified range.")
"""



# def int_to_roman(n):
#     val = [
#         1000, 900, 500, 400,
#         100, 90, 50, 40,
#         10, 9, 5, 4,
#         1
#     ]
#     syms = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV",
#         "I"
#     ]
#     roman_numeral = ""
#     i = 0
#
#     while n > 0:
#         for _ in range(n // val[i]):
#             roman_numeral += syms[i]
#             n -= val[i]
#         i += 1
#
#     return roman_numeral
#
# num = int(input("Enter an integer (1-3999): "))
# if 1 <= num <= 3999:
#     roman_numeral = int_to_roman(num)
#     print(f"The Roman numeral for {num} is {roman_numeral}")
# else:
#     print("Please enter an integer within the specified range.")

# def int_to_roman(n):
#     val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#     roman_numeral = ""
#
#     for i in range(len(val)):
#         count = n // val[i]
#         roman_numeral += syms[i] * count
#         n -= val[i] * count
#
#     return roman_numeral
#
# num = int(input("Enter an integer (1-3999): "))
# if 1 <= num <= 3999:
#     roman_numeral = int_to_roman(num)
#     print(f"The Roman numeral for {num} is {roman_numeral}")
# else:
#     print("Please enter an integer within the specified range.")

# lis = [1, 2, 2, 3]
# print(range(len(lis)))


"""def roman_number(num):

    if num<=3999:
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        # num = int(input("Give the number"))
        roman = ""
        i = 0
        while num>0:
            div = num//numbers[i]
            num = num % numbers[i]
            while div>0:
                roman += syms[i]
                div -= 1
            i += 1
        return roman
    else:
        print("Please enter a number smalller than 3999")
print(roman_number(int(input("Give the number"))))"""


# spuare pattern
n = 5
for j in range(n): #outer loop determine the row
    for i in range(n):#inner loop detremine column
        print("*", end="  ")
    print()
print()

#  increasing triangle pattern

n = 5
for j in range(n):
    for i in range(j+1): #range of inner loop will be (j+1)
        print("*", end="  ")
    print()
print()
# decrteasing triangle pattern

n = 5
for j in range(n):
    for i in range(j, n): # range of inner loop will be (i, n)
        print("*", end="  ")
    print()
print()
# right side increasing triangle

n = 5
for j in range(n):
    for i in  range(j,n):
        print(" ", end=" ") # decreasing triangle with space
    for i in range(j+1):
        print("*", end=" ") # increasing triangle with star
    print()
print()

# right side decreasing triangle

n = 5
for j in range(n):
    for i in range(j):
        print(" ", end=" ")
    for i in range(j, n):
        print("*", end=" ")
    print()
print()

# HILL PATTERN

n = 5
for j in range(n):
    for i in range(j, n):
        print(" ", end=" ")
    for i in range(j+1):
        print("*", end=" ")
    for i in range(j):
        print("*", end=" ")
    print()
print()

# REVERSE HILL PATTERN

n = 5
for j in range(n):
    for i in range(j+1):
        print(" ", end=" ")
    for i in range(j, n-1):
        print("*", end=" ")
    for i in range(j, n):
        print("*", end=" ")
    print()
print()

# DIAMOND PATTERN
n = 5
for i in range(n-1):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()







