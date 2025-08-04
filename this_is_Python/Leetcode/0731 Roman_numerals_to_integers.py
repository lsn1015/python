#Roman numerals to integers

def Roman_to_Int(s: str) -> int:
    d = {'I': 1, 'V': 5, 'x': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    initial = 0
    for c in reversed(s):
        current_value = d[c]
        if current_value < initial:
            total -= current_value
        else:
            total += current_value
        initial = current_value
    return total

R1 = Roman_to_Int('IV')
print(R1)