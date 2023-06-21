with open('10_files_and_exceptions/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)


filename = '10_files_and_exceptions/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
