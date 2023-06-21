textfile = '10_files_and_exceptions/learning_python.txt'

with open(textfile) as file:
    lines = file.readlines()
    
    
for line in lines:
    line = line.replace("Python", "C")
    print(line)
    