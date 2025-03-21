for i in range(101):
    if (i == 2 or i == 3 or i == 5 or i == 7):
        print(i)
    elif i == 1:
        continue
    elif i == 9:
        continue
    elif (i % 2 == 0):
        continue
    elif i >= 10 and i % 3 == 0:
        continue
    elif i >= 10 and i % 5 == 0:
        continue
    elif i>=10 and i % 7 == 0:
        continue
    else:
        print(i)
    i += 1
