# odd = [1, 3, 5]
# odd.append(7)
# print(odd)
# odd.extend([9, 11, 13])
# print(odd)
# odd.append([7,6])
# print(odd)


# # Concatenating and repeating lists
# odd = [1, 3, 5]
# print(odd + [9, 7, 5])
# print(["re"] * 3)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# thislist[2]="bit"
# print(mylist)
# print(thislist)

# a = "Hello, World!"
# print(a.replace("H", "J"))

# a = " Hello, World! "
# print(a.strip())

# a = "Hello, World!"
# print(a.split())
# print(a.split(","))

# txt = "apple#banana#cherry#orange"

# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 4)

# print(x)

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# print("C:\\Python32\\Lib")
# print("We are the so-called \"Vikings\" from the north.")

# txt = "Hello, welcome to my world."
# x = txt.find("e", 5, 10)
# print(x)

# txt = "Hello, welcome to my world."
# print(txt.find("q"))
# print(txt.index("q"))

# numTuple = ('1', '2', '3', '4')
# separator = ', '
# print(separator.join(numTuple))

# # .join() with lists
# numList = ['1', '2', '3', '4']
# separator = ', '
# print(separator.join(numList))

# s1 = 'abc'
# s2 = '123'
# print('s1.join(s2):', s1.join(s2))
# print('s2.join(s1):', s2.join(s1))



#SETS-----

# my_set = {1.0, "Hello", (1, 2, 3)}
# print(my_set)

# my_set = {1, 2, 3, 4, 3, 2}
# print(my_set)

# my_set = set([1, 2, 3, 2])
# print(my_set)

# my_set = {1, 2, [3, 4]}

# my_set = {}
# print(my_set)

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)
# print("banana" in thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# my_set = {1, 3}
# my_set.update([4, 5], {1, 6, 8})
# print(my_set)

# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)


#DICTONARY-----

# thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020,
# "electric": False, "colors": ["red", "white", "blue"] }
# print(thisdict)

# thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020 }
# print(len(thisdict))
# print(type(thisdict))

# car = { "brand": "Ford", "model": "Mustang", "year": 1964 }
# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x) #after the change

# car = { "brand": "Ford", "model": "Mustang", "year": 1964 }
# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change

# dict1 ={ "brand": "Ford", "model": "Mustang", "year": 1964}
# dict2 = dict1.copy()
# print(dict1)
# print(dict2)
# #Make changes in dict1
# print(dict1)
# print(dict2)

# myfamily = {
# "child1" : {
# "name" : "Emil",
# "year" : 2004
# },
# "child2" : {
# "name" : "Tobias",
# "year" : 2007
# },
# "child3" : {
# "name" : "Linus",
# "year" : 2011
# }
# }
# print(myfamily["child1"]["name"])

# # vowels keys
# keys = {'a', 'e', 'i', 'o', 'u' }

# vowels = dict.fromkeys(keys)
# print(vowels)

# value = 'vowel'
# vowels = dict.fromkeys(keys, value)
# print(vowels)

# # vowels keys
# keys = {'a', 'e', 'i', 'o', 'u' }
# value = [1]

# vowels = dict.fromkeys(keys, value)
# print(vowels)

# # updating the value
# value.append(2)
# print(vowels)

# #with List comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)


#FUNCTION-------

# def greet(name):

#     """

#     This function greets to
#     the person passed in as
#     a parameter
#     """

#     print("Hello, " + name + ". Good morning!")

# greet('Jitiksha')

# print(greet.__doc__)

# c = 1 # global variable
# def add():
#     c = c + 2 # increment c by 2
#     print(c)

# add()

# c = 0 # global variable
# def add():
#     global c
#     c = c + 2 # increment by 2
#     print("Inside add():", c)
# add()
# print("In main:", c)

# def foo():
#     y = "local"
# foo()
# print(y)
#-------------------------------------------
# def foo():
#     y = "local"
#     print(y)
# foo()


# x = "global "

# def foo():
#     global x
#     y = "local"
#     x = x * 2
#     print(x)
#     print(y)

# foo()

# x = 5
# def foo():
#     x = 10
#     print("local x:", x)
# foo()
# print("global x:", x)

# def outer():
#     x = "local"

#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)

#     inner()
#     print("outer:", x)

# outer()

class Teacher:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def disp(self):
        print(self.name)
        print(self.__salary)
teacher = Teacher('Suzan', 500000)
teacher.disp()
print(teacher.name)
print(teacher.__salary)# error-object has no
#attribute