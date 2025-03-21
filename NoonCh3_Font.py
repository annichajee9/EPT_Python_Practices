lower_letter = "abcdefghijklmnopqrstuvwxyz"
upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

full_alphabet = list(lower_letter + upper_letter)

string_1 = input()
string_2 = input()

ls = []
for i in string_1:
    if i in string_2:
        ls.append(i)

updated_ls = sorted(set(ls), key=lambda x: full_alphabet.index(x))

output = []
for item in updated_ls:
    alphabet_index = full_alphabet.index(item)
    output.append(full_alphabet[alphabet_index])

if output:
    print(" ".join(output))
else:
    print("NONE")
