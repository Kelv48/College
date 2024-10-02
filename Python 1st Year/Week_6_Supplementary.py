#Kelvin Osagie 122318693
#Supplementary.py

#Q1.
'''Speed_of_Light = 186_000    #Miles per second
Distance_between = 34_000_000  #Miles


def howLongToTransmit ():
    global time_taken
    time_taken = Distance_between // Speed_of_Light

howLongToTransmit()
mins = time_taken // 60
print(time_taken, "seconds or aproximately", mins, "minutes")'''

#Q2.

#insurance = 80% the amount 

'''def calculateInsurance (cost):   # returns the minimum amount of insurance needed 
    global insurance             # makes insurance a global variable so that it doesn't need to be defined outside of the function
    insurance = cost * 0.8
    round(insurance, 2)

cost_of_replacement = float(input("Please enter the cost to replace the structure "))   # Gets the cost from the user
calculateInsurance(cost_of_replacement)       # Enters the users input into the function

print("€",insurance, sep="")'''

#Q3.
#property tax = 60% actual value @ 64 cent per €100
#@ 60_000 property tax is 384

'''def calculate_property_Tax (price):           # Function for calculating the property tax
    global valuation
    valuation = price * 0.6
    global prop_tax                             
    prop_tax = (valuation // 100) * 0.64
    round(prop_tax, 2)

prop_value = float(input("Please enter in the value of the property "))     # Get input from the user
calculate_property_Tax(prop_value)

print("€", prop_tax, sep="")'''

#Q4.
'''ClassA = 100
ClassB = 80
ClassC = 60 

def revenue_generated (numOfClassA, numOfClassB, numOfClassC):
    PriceA = numOfClassA * ClassA
    PriceB = numOfClassB * ClassB
    PriceC = numOfClassC * ClassC
    global total
    total = PriceA + PriceB + PriceC

numberOfClassA = int(input("Please enter the values of Class A ticket sales "))
numberOfClassB = int(input("Please enter the values of Class B ticket sales "))
numberOfClassC = int(input("Please enter the values of Class C ticket sales "))


revenue_generated(numberOfClassA, numberOfClassB, numberOfClassC)
print("€", total, sep="")'''

#Conditionals
#Q1.

'''luggageWeight = int(input("Please enter the weight of your bag in Kgs "))

def checkLuggageWeight (weight):
    if weight > 20:
        print("There is a €20 surcharge as your bag is overweight ")
    elif weight < 20:
        print("Have a safe flight!")
    else:
        print("Phew! you just made it")

checkLuggageWeight(luggageWeight)'''

#Q2.

'''Any year that is divisible by 400 is a leap year. 
Of the remaining years, any year that is divisible by 100 is not a leap year. 
Of the remaining years, any year that is divisible by 4 is a leap year. 
All other years are not leap years. '''

'''def checkLeapYear (year):
    if year // 400 == 0:
        print("It is a leap year")
    elif year // 100 == 0:
        print("Is not a leap year")         #doesn't work consistently
    elif year // 4 == 0:
        print("It is a leap year")
    else:
        print("It is not a leap year")

what_year = int(input("What year is it "))
checkLeapYear(what_year)'''

#Q3.
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


def romanNumeral (num):
    if num > 0 and num <= 10:
        list_position = num - 1
        roman_char = r_numerals[list_position]
        print(roman_char)
    else:
        print("Error you have entered a number outside of 1 - 10")


number = int(input("enter num "))
romanNumeral(number)'''


