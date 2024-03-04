# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

#1
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")

print("Hello,", name + " ", surname + " at age ", age + "!")

#2
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit-32) * 5/9

print("Temperature in Celsius:", celsius)

#3
score = float(input("Enter your score: "))

if score >= 90:
    grade = "5"
elif score >= 80:
    grade = "4"
elif score >= 70:
    grade = "3"
elif score >= 60:
    grade = "2"
else:
    grade = "1"

print("Your grade is:", grade)

#4
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 % number2 == 0:
    result = "Yes"
else:
    result = "No"

print("Can number 1 be devided by 2? ", result)

#5
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1+side2 > side3 and side2+side3 > side1 and side1+side3 > side2:
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    print("The triangle is:", triangle_type)

else:
    print("Cant be drown")

#6
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "/" and num2 == 0:
    print("cant divide by 0")

else:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "Invalid operation"

    print("Result:", result)