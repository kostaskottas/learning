print("If you want to stop at any time insert: stop")
while True:
    firstname = input("Please write your firstname: ")
    if firstname == "stop":
        break
    lastname = input("Please write your lastname: ")
    if lastname == "stop":
        break
    with open("10_files_and_exceptions/guest_book.txt", "a") as file:
        file.write(f"{firstname.title()} {lastname.title()}!\n")
        print(f"Hi {firstname} {lastname} you've been added to the guest book.")