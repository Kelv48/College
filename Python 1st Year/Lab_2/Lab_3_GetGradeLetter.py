'''GetGradeLetter.py 
11-10-22'''

'''Ask the user to input the numerical grade
Save this as a variable called gradePercentage
Depending on the user input print the corresponding letter grade
if number is outside of range 0 - 100 print X'''

gradePercentage = int((input("What is your grade?")))


if gradePercentage >= 85 : print("A")
elif gradePercentage >= 70 : print("B")
elif gradePercentage >= 55 : print("C")
elif gradePercentage >= 40 : print("D")
elif gradePercentage >= 25: print("E")
elif gradePercentage >= 0 : print("F")

