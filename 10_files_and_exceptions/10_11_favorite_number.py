import json
file = "10_files_and_exceptions/favorite_number.json"
def store_favorite_number():
    favorite_number = input("What is your favorite number? ")
    
    with open(file, "w") as f:
        json.dump(favorite_number, f)

def print_favorite_number():            
    with open(file) as f:
        favorite_number = json.load(f)
        print(f"Your favorite number is {favorite_number}!")

store_favorite_number()
print_favorite_number()