list=[]
binary_number=input("enter the binary number:")
for i in binary_number.split("."):
    binary_number=int(i)
    binary_number=int(binary_number)
    decimal_number=int(i,2)
    list.append(decimal_number)
print("the decimal number is:",end="")
print(*list,sep=".")