n = int(input())
answer = 0
for i in range(1,n+1):
    answer += 1/(i**2)
    i += 1
print("%.3f" %answer)