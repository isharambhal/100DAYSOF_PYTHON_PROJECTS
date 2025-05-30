#Tip Calculator
#After splitting the bill between the
# given number of people with tip percentage, also formatting to 2 decimal places

print("Welcome to the Tip Calculator!")
bill = float(input("What is the total bill?? $ \n"))
tip = int(input("What percentage tip would you like to give? \n"))
people = int(input("How many people to split the bill? \n"))
tip_as_percent = tip/100
total_tip_amt = bill * tip_as_percent
total_bill = bill + total_tip_amt
bill_per_person = total_bill / people
final_amt = round(bill_per_person, 2)
print(f"Each person should pay : $ {final_amt}")