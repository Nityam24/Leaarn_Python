# b) Declare a class Person having name as member. Derive two classes
# a. Businessman - having income and number of people involved in his
# business as members.
# b. Employee - having income as a member.
# c. Create objects of both the classes and compare the income and print the name of
# one having greater income.


class person:
    def __init__(self, name):
        self.name = name


class Businessman(person):
    def __init__(self, name, income, ppl):
        super().__init__(name)
        self.income = income
        self.people = ppl


class Employee(person):
    def __init__(self, name, income):
        super().__init__(name)
        self.income = income


bm1 = Businessman("Dhirubhai", 70000000, 5000)
ep1 = Employee("Sundar", 80000000)

if bm1.income > ep1.income:
    print("{} is havin Greater income".format(bm1.name))
elif ep1.income > bm1.income:
    print("{} is havin Greater income".format(ep1.name))
else:
    print("Both are having same income")
