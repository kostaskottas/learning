dogs = "10_files_and_excptions/dogs.txt"
cats = "10_files_and_exceptions/cats.txt"
petsnames = [dogs, cats]
try:
    for names in petsnames:
        with open(names) as pets:
            pets = pets.read()
            print(f"Your name list in the file {names} is:\n")
            print(pets)
except FileNotFoundError:
    pass
