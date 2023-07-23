#Write a program to sort given list.

list = [3,5,7,2,6,9,1]
print("initial List:",list)
temp=0
for i in range(0,len(list)):    
    for j in range(i+1, len(list)):    
        if(list[i] > list[j]):    
            temp = list[i];    
            list[i] = list[j];    
            list[j] = temp;
print("sorted list:",list)
