# recursively 
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  

num = int(input("Enter a number: "))  

if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))  

# iteratively
def get_factorial_while_loop(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

inp = input("Enter a number: ")
inp = int(inp)

print(f"The result is: {get_factorial_while_loop(inp)}")
