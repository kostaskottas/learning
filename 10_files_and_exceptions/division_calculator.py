print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divine by 0!")
    except ValueError:
        print("You can use only numbers!")
    else:
        print(answer)
        with open("10_files_and_exceptions/test.txt", "a") as file:
            file.write(f"{first_number} / {second_number} = {answer}\n")
