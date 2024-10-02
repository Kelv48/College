'''MetEireann.py
Kelvin Osagie 122318693
18/10/22'''
import math

'''#1a

#gets input from the user for the temp and speed values
airTemp = float(input("Please enter the air temperature "))
airSpeed = float(input("Please enter the air speed "))

#Calculates the WCI and prints it to the screen
windChillIndex = 13.12 + (0.6215 * airTemp) - (11.37 * (airSpeed ** 0.16)) + (0.3965 * airTemp *(airSpeed ** 0.16))
print(round(windChillIndex, 0))'''

#1b

#Define the function
def calcWindChillIndex (tempA, speedA) :
    windChillIndex = 13.12 + (0.6215 * airTemp) - (11.37 * (airSpeed ** 0.16)) + (0.3965 * airTemp *(airSpeed ** 0.16))
    return windChillIndex

#Input the variables and invoke the function
airTemp = float(input("Please enter the air temperature "))
airSpeed = float(input("Please enter the air speed "))
WCI = calcWindChillIndex(airTemp, airSpeed)

#Print the results
print("The temperature feels like " , round(WCI) , chr(176),sep='')



'''#1c
#Define the function
def calcWindChillIndex (tempA, speedA) :
    windChillIndex = 13.12 + (0.6215 * airTemp) - (11.37 * (airSpeed ** 0.16)) + (0.3965 * airTemp *(airSpeed ** 0.16))
    print("The temperature feels like " , round(windChillIndex) , chr(176),sep='')

#Input the variables and invoke the function
airTemp = float(input("Please enter the air temperature "))
airSpeed = float(input("Please enter the air speed "))

calcWindChillIndex(airTemp, airSpeed)'''

'''#1d

#Import the function from another folder
from Lab3functions import calcWindChillIndex

#Input the variables and invoke the function
airTemp = float(input("Please enter the air temperature "))
airSpeed = float(input("Please enter the air speed "))

#Invoke the Function
calcWindChillIndex(airTemp, airSpeed)'''


'''baker.py'''

'''#2

sconeprice = 1.49 * float(input("How many scones were bought at full price "))
sconediscountedPrice = (1.49 * 0.60) * float(input("How many scones were bought two days old at a discount "))

totalPrice = sconeprice + sconediscountedPrice
print('€',totalPrice, sep="")'''

'''#2a

def scones (fpscone, dpscone) :
    fprice = 1.49 * fpscone
    dprice = (1.49 * 0.60) * dpscone
    totalprice = fprice + dprice
    round(totalprice, )
    return totalprice 

sconeprice = float(input("How many scones were bought at full price? "))
dsconeprice = float(input("How many scones were bought two days old at a discount? "))

totalprice = scones(sconeprice, dsconeprice)
print('€',totalprice, sep="")'''

'''#2b
def scones (fpscone, dpscone) :
    fprice = float(1.49 * fpscone)
    dprice = float((1.49 * 0.60) * dpscone)
    totalprice = fprice + dprice
    return totalprice 

sconeprice = float(input("How many scones were bought at full price? "))
dsconeprice = float(input("How many scones were bought two days old at a discount? "))

totalprice = scones(sconeprice, dsconeprice)
print("The bakery sold {}{} worth of scones.".format('€', totalprice))'''

'''#2c

def scones (fpscone, dpscone) :
    fprice = float(1.49 * fpscone)
    dprice = float((1.49 * 0.60) * dpscone)
    totalprice = fprice + dprice
    return totalprice 

sconeprice = float(input("How many scones were bought at full price? "))
dsconeprice = float(input("How many scones were bought two days old at a discount? "))

totalprice = scones(sconeprice, dsconeprice)
print("The bakery sold {}{} worth of scones.".format('€', totalprice))'''

'''#3

def seasons(number) :
    if number == 1 :
       print("winter")
    elif number == 2 :
        print("Spring")
    elif number == 3 :
        print("Summer") 
    elif number == 4 :
        print("Autumn")
    else:
        print("Error you have entered a number outside the parameters of this function, please try again")


num = int(input("Please enter a number between one and four as an integer "))
seasons(num)'''

'''#4

from Lab3functions import equal_numbers

number1 = int(input("Please enter the 1st number "))
number2 = int(input("Please enter the 2nd number "))

equal_numbers(number1, number2)'''





















