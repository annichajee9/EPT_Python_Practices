n = int(input())
ls = []
for i in range(n):
    x = input().strip()
    ls.append(x)

roman_to_int_table = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

def roman_to_int(roman):
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_to_int_table[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

int_to_roman_table = [
    ['M', 1000], ['CM', 900], ['D', 500], ['CD', 400],
    ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
    ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]
]

def int_to_roman(num):
    roman = ""
    for symbol, value in int_to_roman_table:
        while num >= value:
            roman += symbol
            num -= value
    return roman

sorted_ls = sorted(ls, key=roman_to_int)
for item in sorted_ls:
    print(item)