value1 = int(input("Enter your first value: "))
value2 = int(input("Enter your second value: "))

operator = input(
    "Enter your operator (addition, subtraction, multiplication, division): "
)

if operator == "addition":
    print("Addition =", value1 + value2)

elif operator == "subtraction":
    print("Subtraction =", value1 - value2)

elif operator == "multiplication":
    print("Multiplication =", value1 * value2)

elif operator == "division":
    print("Division =", value1 / value2)

else:
    print("Error: Invalid operator")...