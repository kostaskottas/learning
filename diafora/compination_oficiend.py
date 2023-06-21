import itertools

list_of_num = [71, 22, 51, 6, 53, 49, 69, 70, 48, 98, 20, 75, 0, 25, 19, 81, 99, 46, 31, 29, 7, 73, 55, 18, 64, 37, 33, 14, 11, 84, 21]

found = False

for combination in itertools.combinations(list_of_num, 6):
    if sum(combination) == 500:
        print(*combination)
        found = True
        break

if not found:
    print("No combination found.")