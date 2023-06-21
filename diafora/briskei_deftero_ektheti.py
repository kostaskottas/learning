def solve_for_exp(a, b):
    count = 1
    while b != a:
        b = b / a
        count += 1
    
    return count

print(solve_for_exp(2,1024))

