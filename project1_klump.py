#Conor Klump
#IT 211
#Project 1: Monthly Loan Payment Calculator

loan_amount_str= input("Enter your loan amount in USD: ")
loan_amount_str= loan_amount_str.replace(",","").replace("$","")
loan_amount= float(loan_amount_str)

interest_rate_str= input("Enter annual interest rate: ")
interest_rate_str = interest_rate_str.replace("%","")
interest_rate= float(interest_rate_str)

loan_duration_str=(input("Enter duration of loan in number of months: "))
loan_duration_str= loan_duration_str.replace("months","")
loan_duration= float(loan_duration_str)

monthly_interest= (interest_rate/100)/12

monthly_payment = (monthly_interest*loan_amount)/(1-(1+monthly_interest)**(-loan_duration))

print("      ")
print("Your monthly mortgage payment is $%.2f." % monthly_payment)  

#end of program
