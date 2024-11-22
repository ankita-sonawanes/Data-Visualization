n = 4
for i in range(n):
    # Print leading spaces
    print(" " * (n - i - 1), end="")

    # Print increasing part
    for j in range(1, i + 2):
        print(j, end="")

    # Print decreasing part
    for j in range(i, 0, -1):
        print(j, end="")

    print()  # Newline after each row
