def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

count = 0
number = 2
while count < 100:
    if is_prime(number):
        print(number, end="\n")
        count += 1
    number += 1
