print("press q at any point to exit the programm")
while True:
    number1 = input("write your first number: ")
    if number1 == "q":
        break
    number2 = input("write your second number: ")
    if number2 == "q":
        break
    
    try:
        resolt = int(number1) + int(number2)
    except ValueError:
        print("please enter only number")
    else:
        print(resolt)
