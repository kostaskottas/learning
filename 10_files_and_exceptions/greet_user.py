import json
filename = '10_files_and_exceptions/username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
