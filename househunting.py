total_cost = float(input("What is the total cost of your home?"))
portion_down_payment = total_cost * 0.25
print("Your downpayment will be", portion_down_payment)
current_savings = 0
r = float(input("What is the expected annual rate of return on your savings?")) 
annual_salary = float(input("What is your annual salary?"))
salary_percentage = float(input("What percent of your annual salary will you save towards downpayment?"))
portion_saved =  annual_salary * salary_percentage
print("Your annual salary savings is", portion_saved)
monthly_savings = portion_saved / 12
print ("Your monthly savings is", monthly_savings) 
number_of_months = 0
while current_savings <= portion_down_payment:
    number_of_months += 1
    current_savings = current_savings + monthly_savings + (current_savings * r/12)

print("The number of months is", number_of_months)






