n = int(input())
total = 1
if n > 0:
    for i in range(n, 1, -1):
        total *= i
    print(total)
else:
    print(1)