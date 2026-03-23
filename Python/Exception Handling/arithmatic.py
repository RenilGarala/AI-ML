num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
    result = int(num1) / int(num2)
except TypeError as te:
    print("Type error: ", te)
    result = None
except ZeroDivisionError as zde:
    print("Cannot divide by zero: ", zde)
    result = None
except ValueError as ve:
    print("Value error: ", ve)
    result = None
except Exception as e:
    print("An error occurred: ", e)
    result = None
print("The result is: ", result)