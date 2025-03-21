ls = []
for i in range(10):
    i = int(input())
    ls.append(i)

even = False
for j in ls:
    if j % 2 == 0:
        even = True

if even:
    print("have")
else:
    print("don't have")