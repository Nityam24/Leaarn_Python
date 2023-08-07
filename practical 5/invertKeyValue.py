#Write a program to invert keys and values of dictionary.
dict1={'Apple':14,'Samsung':23,'Google':7}
dict2=dict((value,key) for key,value in dict1.items())
print(dict1)
print(dict2)