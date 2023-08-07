#Create a dictionary where keys are name of students and values are another dictionary
#containing semester, age and cpi of that student.
dicnis={"sem":4,"Age":20,"CPI":9}
dicnim={"sem":4,"Age":19,"CPI":7.5}
dicfinal={"nis":dicnis,"nim":dicnim}
#Print all the names of students.
print(dicfinal)
#Print only names of students
print(dicfinal.keys())
#Print the name of student having highest CPI
highest_cpi=max(dicfinal,key=lambda x: dicfinal[x]['CPI'])
print("Highest CPI:",highest_cpi)