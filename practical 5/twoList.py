#Write a program to map 2 lists into a dictionary.
Keys=['Alex','John','Divya']
Values=[23,22,24]
dic=dict(zip(Keys,Values))
print(dic)



#Write a program to generate dictionary of frequency of alphabets of given string.
str1="ALEXWILLIAMBARNES"
str2=set(str1)
dict1={}
for s in str2:
    dict1[s]=str1.count(s)
print(dict1)