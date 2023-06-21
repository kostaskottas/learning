firstname = input("Please insert you first name: ")
lastname = input("Please insert you last name: ")
fullname = f"{firstname} {lastname}!\n"
file = "10_files_and_exceptions/namefile.txt"

with open(file, "a") as names:
    names.write(fullname.title())