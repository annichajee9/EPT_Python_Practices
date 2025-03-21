count = 0  # Initialize a counter to keep track of elements per line

for i in range(1, 111):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("CozaLozaWoza", end="")
    elif i % 3 == 0 and i % 5 == 0:
        print("CozaLoza", end="")
    elif i % 5 == 0 and i % 7 == 0:
        print("LozaWoza", end="")
    elif i % 3 == 0 and i % 7 == 0:
        print("CozaWoza", end="")
    elif i % 3 == 0:
        print("Coza", end="")
    elif i % 5 == 0:
        print("Loza", end="")
    elif i % 7 == 0:
        print("Woza", end="")
    else:
        print(i, end="")

    count += 1  # Increment the counter

    if count == 11:  # Check if 11 elements have been printed
        print()  # Print a newline
        count = 0  # Reset the counter
