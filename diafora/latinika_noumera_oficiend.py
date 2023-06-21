def roman_to_int(roman):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    
    for symbol in reversed(roman):
        value = roman_map[symbol]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


# Example usage:
roman_numeral = 'MMMCMLXXVIII'
numeric_value = roman_to_int(roman_numeral)
print(numeric_value)