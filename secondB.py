print("Hello World")
a=float(input("Enter the 1st number"))
b=float(input("Enter the 2nd number"))
c=float(input("Enter the 3rd number"))
if a>=b and a>=c:
    largest = a
elif b>=a and b>=c:
    largest = b
else:
    largest = c
print("largest among three is " ,largest)
