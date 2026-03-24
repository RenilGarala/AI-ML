class MyException(Exception):
    pass

try:
    a = 10
    if(a > 5):
        raise MyException("Value is greater than 5")
    else:
        print("Value is less than or equal to 5")
except MyException as e:
    print("Caught MyException: ", e)