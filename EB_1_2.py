n = int(input())
if n == 0:
    avg = 0
    print(0)
    print("-")
    print("-")
else:
    ls = []
    ls.append(n)
    for i in range(n):
        add_n = int(input())
        ls.append(add_n)
    #print(ls)


    sum = 0
    calculated_avg = ls[1:]
    for j in calculated_avg:
        sum += j
    avg = sum/len(calculated_avg)
    print("%.3f" %avg)
    print(int(min(ls)))
    print(int(max(ls)))