# manually call exception
age = 10

try:
    if age < 18:
        raise Exception("You are not eligible to vote.")
    else:
        print("You are eligible to vote.")
except Exception as e:
    print("An error occurred: ", e)
