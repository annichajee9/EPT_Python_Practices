# Number of lines in the pattern
lines = 10

for i in range(lines):
    # Calculate the number of dashes and X's for each line
    dashes = lines - i - 1
    xs = 2 * (i) + 1

    # Print the pattern
    print('-' * dashes + 'x' * xs)
