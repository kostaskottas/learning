import json
def get_stored_username():
    """Get stored username if available."""
    filename = '10_files_and_exceptions/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = '10_files_and_exceptions/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        same_user = input(f"Is the {username} your's username? (y/n) ")
        if same_user == "y":
            print(f"Welcome back, {username}!")
        else:
            get_new_username()
            print(f"We'll remember you when you come back, {get_stored_username()}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()