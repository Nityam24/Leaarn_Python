'''Write a program which takes a sentence from user and calculates number of digits, letters,
uppercase letters, lowercase letter and spaces in sentence.'''

def countChar(str):
     upper, lower, number, special = 0, 0, 0, 0
     for i in range(len(str)):
         if str[i] >= 'A' and str[i] <= 'Z':
             upper += 1
         elif str[i] >= 'a' and str[i] <= 'z':
             lower += 1
         elif str[i] >= '0' and str[i] <= '9':
             number += 1
         else:
             special += 1
     print('Upper case letters:', upper)
     print('Lower case letters:', lower)
     print('Number:', number)
     print('Special characters:', special)
 
str = input("enter the string")
countChar(str)


