'''Payslip.py  
Kelvin Osagie 122318693
11-10-22'''

#SudoCode
'''How many hours the employee worked store this as a variable
Make variable for standard week =40 hours @ €12 per hour
Overtime is all hours over 40 and is payed at €20 per hour

Print hours worked
Print Basic Pay
Print Overtime Pay
Print Total Pay'''

#Hours Worked
Hours_worked = int(input("how many hours did you work")) 
Standard_week = 40
Overtime_week = int((Hours_worked - Standard_week))

#Rates of Pay
Standard_pay = 12
Overtime_pay = 20

#Amount of Money Payed
Basic_pay = int((Standard_week * Standard_pay))
Overtime_payslip = int((Overtime_week * Overtime_pay))
Total_pay = int((Overtime_payslip + Basic_pay))

#Print Results
print ("Hours Worked:" , Hours_worked)
print ("Basic Pay:" ,Basic_pay)
print ("Overtime Pay:" ,Overtime_payslip)
print ("Total Pay:" ,Total_pay)
