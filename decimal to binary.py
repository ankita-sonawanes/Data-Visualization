list=[]
decimal_number=input("enter the decimal number:")
for i in decimal_number.split("."):
    decimal_number=int(i)
    decimal_number=bin(decimal_number)
    binary_number=decimal_number[2:]
    list.append(binary_number)
print("enter the binaru number:",end="")
print(*list,sep=".")