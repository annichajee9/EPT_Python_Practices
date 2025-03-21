n = 100
ls = []
for i in range(1,n+1):
    if n % i == 0:
        ls.append(i)
    i += 1
print(ls)