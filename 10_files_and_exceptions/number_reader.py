import json
filename = '10_files_and_exceptions/number.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)