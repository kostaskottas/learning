filetxt = '10_files_and_exceptions/learning_python.txt'
with open(filetxt) as file:
    text = file.read()
print(text)

with open(filetxt) as file:    
    for line in file:
        print(line.strip())

text = ''
with open(filetxt) as file:
    for line in file:
        text += line
print(text)

with open(filetxt) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())