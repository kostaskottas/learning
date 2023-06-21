def calculator(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    if operator == "-":
        result = num1 - num2
    if operator == "*":
        result = num1 * num2
    if operator == "/":
        if num2 == 0:
            result = "Can't divine by 0!"
        else:
            result = num1 / num2

    return result

print(calculator(2314234, "*", 234242))