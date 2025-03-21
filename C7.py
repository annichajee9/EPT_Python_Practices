# Number of lines in the pattern
lines = 10

for i in range(lines):
    # Calculate the number of dashes for each line
    dashes = lines - i - 1
    # Create the ascending part of the sequence
    ascending = ''.join(str(x) for x in range(1, i + 2))
    # Create the descending part of the sequence
    descending = ''.join(str(x) for x in range(i, 0, -1))

    # Print the pattern
    print('-' * dashes + ascending + descending)
