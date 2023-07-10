# Write a Python program to calculate the sum of the digits in an integer.
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = int(input("enter the number"))
print(getSum(n))
