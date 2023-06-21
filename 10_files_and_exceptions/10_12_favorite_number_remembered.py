import json
file = "10_files_and_exceptions/favorite_number.json"
def store_favorite_number():
    favorite_number = input("What is your favorite number? ")
    
    with open(file, "w") as f:
        json.dump(favorite_number, f)

def print_favorite_number():            
    try:
        with open(file) as f:
            favorite_number = json.load(f)
            return favorite_number
    except FileNotFoundError:
        return None
    
def program():
    if print_favorite_number():
        print(f"Your favorite number is {print_favorite_number()}!")
    else:
        store_favorite_number()
        print(f"Now i know your favorite number {print_favorite_number()}")






program()