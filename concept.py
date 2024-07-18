# print("Hello world")

# variable
# x = 10         # Integer
# y = 3.14       # Floating-point number
# name = "John"  # String
# is_active = True # Boolean

# datatype
# packed_tuple = 1, "hello", 3.14
# a, b, c = packed_tuple
# print(a)  # Output: 1
# print(b)  # Output: hello
# print(c)  # Output: 3.14
# ...

# conditional statement
# x = 3
# if x > 5:
#     print("x is greater than 5")
# elif x > 2:
#     print("x is greater than 2 but less than or equal to 5")
# else:
#     print("x is 2 or less")

# loopings
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# function
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero"
    return x / y

def calculator():
    while True:
        print("Welcome to my simple calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice == "5":
            print("Exiting the calculator. Bye!")
            break
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid value! Please enter a number")

            if choice == "1":
                print(f"The result is: {add(num1, num2)}")
            elif choice == "2":
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"The result is: {divide(num1, num2)}")

        else:
            print("Invalid choice! Please enter a number between 1 and 5")

calculator()