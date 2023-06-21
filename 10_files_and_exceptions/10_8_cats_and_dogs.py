dogs = "10_files_and_exceptions/dogs.txt"
cats = "10_files_and_exceptions/cats.txt"
petsnames = [dogs, cats]
try:
    for names in petsnames:
        print(f"Your name list in the file {names} is:\n")
        with open(names) as pets:
            pets = pets.read()
            print(pets)
except FileNotFoundError:
    print("there are missing files")
