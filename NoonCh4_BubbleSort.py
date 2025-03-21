n = int(input())
ls = []
for i in range(n):
    string = input()
    ls.append(string)

count = 0
for i in range(len(ls)): #n = 4 then range(4) = 0, 1, 2, 3
    for j in range(len(ls) - i - 1): 
    # n = 4 - 0 - 1 = 3 then range(3) = 0, 1, 2
    # n = 4 - 1 - 1 = 2 then range(2) = 0, 1
    # n = 4 - 2 - 1 = 1 then range(1) = 0
        if len(ls[j]) > len(ls[j + 1]) or (len(ls[j]) == len(ls[j + 1]) and ls[j] > ls[j + 1]):
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
            count += 1

for item in ls:
    print(item)
print(count)
