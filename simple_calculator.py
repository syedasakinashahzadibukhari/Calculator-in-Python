value1 = int(input("Enter your value : "))

value2 = int(input("Enter your value :" ))
operator = str(input("Enter your operator ""addition","subtraction","Multiplication","Devision"))
if operator == "addition":
    print("addition",value1 + value2)
elif operator == "subtraction":
    print("subtraction",value1 - value2)
elif operator == "Multiplication":
    print("Multiplication",value1 ** value2)
elif operator == "Devsion":
    print("Devision",value1 // value2)
else:
    print("error")
""