#d) Write a program to convert Decimal to hex, octal and binary.

def dec_to_bin(x):
    return int(bin(x)[2:])

def dec_to_oct(x):
    return int(oct(x)[2:])

def dec_to_hex(x):
    return hex(x)[2:]

x = int(input("enter the number"))
print("decimal to binary: ",dec_to_bin(x))
print("decimal to octal: ",dec_to_oct(x))
print("decimal to hex: ",dec_to_hex(x))