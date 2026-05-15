def Calculator():
    limit = 99
    count = 0
    while count<limit:
        operation = input()
        if len(operation)>99:
            print("Too long")
        elif operation[-1]=="=":
            answer = eval(operation)
            print(answer)
        else:
            print("error")

''' This evak function make'''