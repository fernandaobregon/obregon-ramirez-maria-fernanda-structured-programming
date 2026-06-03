
# Variable declaration
condition="yes" 

def generate_email(name, lastname):
    email = f"{name.lower()}.{lastname.lower()}@utd.edu.mx"
    return email

while condition.lower() == "yes":
    name = input("Introduce your name here: ")
    lastname = input("Introduce your last name here: ")
    
    # Main program 
    email = generate_email(name, lastname)
    print(f"Your institutional email is: {email}")
    
    condition = input("Do you want to generate an institutional email? (yes/no): ")

""" What is Income Tax (ISR)?
Steps
Enter the salary, lower limit, fixed fee, and excess percentage.
Calculate the difference between the salary and the lower limit.
Multiply the difference by the excess percentage.
Add the fixed fee to the tax on the excess.
Display the total ISR in Mexican currency format.

ISR (Impuesto Sobre la Renta) is the Mexican equivalent of Income Tax."""

import locale
from decimal import Decimal
locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')

def format_currency(amount):
    return f"${amount:,.4f}"

def calculate_isr(salary, lower_limit, fixed_fee, excess_percentage):
    isr = ((salary - lower_limit) * excess_percentage) + fixed_fee
    print(f"Your ISR is: {format_currency(isr)}")

salary= Decimal(input("Enter your salary: "))
lower_limit = Decimal(input("Enter the lower limit: "))
fixed_fee= Decimal(input("Enter the fixed fee: "))
excess= Decimal(input("Enter the excess percentage: ")) / 100

calculate_isr(salary, lower_limit, fixed_fee, excess)

