number = input()

list_of_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ls = []
for num in number:
    ls.append(int(num))

for i in ls:
    if i in list_of_nums:
        list_of_nums.remove(i)
if len(list_of_nums) == 0:
    print("No missing digits")
else:
    print(" ".join(map(str, list_of_nums)))