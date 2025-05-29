#Basic Calculator in python

print("Simple Calculator")
print("Choose operation:")
print("1. Add = + ")
print("2. Subtract = - ")
print("3. Multiply = * ")
print("4. Divide = / ")

Operator_choice = input("Enter your operator(+,-,*,/): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if Operator_choice == "+":
    result = num1 + num2
    print(f"Addition of two number is : {result}")
elif Operator_choice == "-":
    result = num1 - num2
    print(f"Subtraction of two number is : {result}")
elif Operator_choice == "*":
    result = num1 * num2
    print(f"Multiplication of two number is : {result}")
elif Operator_choice == "/":
    result = num1 / num2
    if num1 == 0:
        print("Error ! : Cannot divide by zero")
    else :
        print(f"Division of two number is : {result}")
else:
    print("Choose Appropriate operator")

