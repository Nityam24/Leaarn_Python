#Write a program to map 2 lists into a dictionary.
Keys=['Alex','John','Divya']
Values=[23,22,24]
dic=dict(zip(Keys,Values))
print(dic)



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = list(zip(list1, list2))
print(result)