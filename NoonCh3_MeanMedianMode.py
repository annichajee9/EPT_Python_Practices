n = int(input())
total = 0
ls = []
max = float("-inf")
for i in range(n):
    number = int(input())
    ls.append(number)
    total += number
avg = total / n
print(avg)
ls.sort()

if n % 2 == 0:
    median = n // 2
    final_med = (ls[median] + ls[median - 1]) / 2
    print(final_med)
else:
    median = n // 2 + 1
    print(ls[median - 1])

for item in ls:
    mode = ls.count(item)
    if mode > max:
        max = mode
        final_mode = item
print(final_mode)