num = float(input("Enter a number: "))
try:
    if num >= 0:
       if num == 0:
           print("Zero")
       else:
           print("Positive number")
    else:
        print("Negative number")
finally:
    print("Code execution completed")