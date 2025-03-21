message = input()

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

full = number + upper_letter + lower_letter
counts = [0] * len(full)

for item in message:
    if item in full:
        index = full.index(item)
        counts[index] += 1
print(" ".join(map(str, counts)))
