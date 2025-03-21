i = 1
print("*|", end="\t")
while i <= 9:
    if i != 9:
        print(str(i), end="\t")
    else:
        print(str(i))
    i = i + 1
print("-" * 77)


for i in range (1,10):
    print(str(i) + "|", end="\t")
    for j in range(1,10):
        if j != 9:
            j = i * j
            print(j, end="\t")
        else:
            j = i * j
            print(j)
    i += 1