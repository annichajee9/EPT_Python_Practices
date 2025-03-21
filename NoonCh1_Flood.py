while True:
    x = list((input().split()))
    break
# print(x)
count = 0
for i in range(len(x)):
    if x[i] < '0':
        if i < len(x) - 1 and x[i + 1] < '0':
            continue
        count += 1
print(count)