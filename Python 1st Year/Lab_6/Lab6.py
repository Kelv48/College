#Discount.py Lab6
#08/11/22

#Q1
'''purchases = [4.95, 9.95, 14.95, 19.95, 24.95]
i = 0


while (i < len(purchases)):
    rounded = round(purchases[i], 2)
    print("Before discount " ,'€',rounded,' || ',"After 60% off discount " ,'€', round(rounded * 0.40, 2), sep="")
    i += 1'''

#Saving.py
#Q2
'''initial_balance = float(input("Please enter the initial balance "))
interest_rate = float(input("Please enter the apr for interest as a decimal "))
converted_interest = 1 + (interest_rate / 100)
desired_balance = float(input("Please enter the final desired value "))

i = initial_balance
x = 1

print("Year-", x,' €', i, sep="")

while i < desired_balance:
    i = round((i * converted_interest), 2)
    x+=1
    print("Year-",x ,' €', i, sep="")'''


#multiply.py
#Q3 
'''i = 0

while i < 10:
   x = i * 1
   print(x, end="")
   i +=1'''

print('While Loop')
print('', end='\t')  # print empty space at start

x = 1
while x <= 10:
     print(x ,end='\t') # prints the values 1 - 10 across the x axis
     x += 1

y = 1
while y <= 10:
     print('')
     print(y,end='\t') 
     z = 1  # reset to 1 to start loop again
     while z <= 10:
          print(y*z ,end='\t')  # inner loop multiplies each y value by z @ z = 1 - 10
          z += 1
     y += 1  # increments y after completing the loop
print()





    

    
   
    
   
    
    










    
    




    
    
