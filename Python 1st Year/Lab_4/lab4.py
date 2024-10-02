'''
Lab-4
Kelvin Osagie 122318693 
27/10/22
''' 

#Q1a

'''
listOne = [3.14, "John", 45, True]
listTwo = [ ]

for index in (listOne) :
    listTwo.append(type(index))

print(listTwo)
'''

#Q1b
'''
listOne = [3.14, "John", 45, True]
listTwo = [ ]
'''
'''
for item in enumerate(listOne) :
    listTwo.append(item)
   
print(listTwo)

for item in range(4) :
    item = (listOne)
    listTwo.append(item)
    

print(listTwo)
'''
'''
#Q1c

from timeit import repeat
from unittest import skip


listOne = [114, 32, -8, -32, 9, -85, 110]
listTwo = [] 

for n in listOne :
    if n > 0:
        listTwo.append(n)
    else:
        print("Num outside range")

print(listTwo)
'''

#Q1d
'''
counties = ["Cork", "Dublin", "Kerry", "Waterford"]
population = [190384, 1228000, 148717, 49213] 

for item in range(len(counties)):
    for index in range(len(population)):
        if index == item:
            print(counties[item], population[index])
'''

#Q2a  

'''
star = '*'

for item in range(5):
    print(star)
'''

#Q2b

'''
star = '*'

for item in range(int(input("How many stars to print? "))):
    print(star)
'''

#Q2c

#Q2d

'''#Q2e
rows = int(input())

for i in range(rows):
    for j in range(i, rows):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i + 1):
        print("*", end="")
    print()
'''     

 


