'''18/10/22'''
from cmath import sqrt
import math

def calcWindChillIndex (tempA, speedA) :
    windChillIndex = 13.12 + (0.6215 * tempA) - (11.37 * (speedA ** 0.16)) + (0.3965 * tempA *(speedA ** 0.16))
    print("The temperature feels like " , round(windChillIndex) , chr(176),"C",sep='')

def seasons (number) :
    if int == 1 :
       print("winter")
    elif int == 2 :
        print("Spring")
    elif int == 3 :
        print("Summer") 
    elif int == 4 :
        print("Autumn")
    else:
        print("Error you have entered a number outside the parameters of this function, please try again")

def equal_numbers (num1, num2) :
    if num1 == num2 :
       print(sqrt(num1), "Numbers are equal")
    else:
       print(sqrt(num1), "Numbers aren't equal")           
            
