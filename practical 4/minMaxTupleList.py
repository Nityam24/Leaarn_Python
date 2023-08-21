#f) Write a program to find minimum and maximum value in list of tuples.

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("initial list:",list)
list.sort(key=lambda x: x[1])
print("sorted list:",list)
print("minimum value:",list[0])
print("maximum value:",list[-1])