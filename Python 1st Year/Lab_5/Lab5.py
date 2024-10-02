#Lab5.py 
#Kelvin Osagie 122318693
#01/11/22




#Q1.



#number = int(input("Please enter a number from 1 to 10 "))


#for i in range(10):
    #traditional
    #print(number * (i+1),)
    #format print
    #print("{} * {} = {}".format(number, (i+1), number * (i+1)))
    #placeholders
    #print("%s * %s = %s" % (number, (i+1), number * (i+1)))
    #F strings 
    #print(f"%s * %s = %s" % (number, (i+1), number * (i+1)))
    

#Q2
'''counter = int(input("Please enter an integer "))
def blastOff(index):
        print(index)
        if index == 1:
            print("Blast Off")



for index in reversed(range(counter)) : 
    index += 1
    blastOff(index)

'''

#Q3.
def bottlesOfBeer(index):
    if index > 1:
        print("{} bottles of beer on the wall. {} bottles of beer. Take one down pass it around, {} bottles of beer on the wall".format(index, index, index-1))
    else:
        print("{} bottle of beer on the wall. {} bottle of beer. Take one down pass it around, {} bottles of beer on the wall".format(index, index, index-1))
    



number = int(input("Please enter a number "))

for index in reversed(range(number)) : 
    index += 1
    bottlesOfBeer(index)
    





    











    
