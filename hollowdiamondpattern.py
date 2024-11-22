n=4
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*",end="")
    if i!=0:
        print(" " * (2*i-1),end="")
        print("*",end="")
    print()
for i in range(n-1):
    print(" " * (i+1),end="")
    print("*",end="")
    if i!=n-2:
        print(" " * (2*(n-i)-5),end="")
        print("*",end="")
    print()
