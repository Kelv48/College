'''FizzBuzz.py 
11-10-22'''

'''If num int divided by 3 = 0 num is a multiple of 3
Print Fizz in this case
If num int divided by 5 = 0 it is a multiple of 5
For nums which are divisible by both  3 and 5 print FizzBuzz'''

number = int(input("Please Enter a number"))

if number % 3 == 0 and number % 5 ==0 : str(print("FizzBuzz"))

elif  number % 3 == 0 : str(print("Fizz"))
   
elif number % 5 == 0 : str(print("Buzz"))



else: print(number)
