# Task 1 — Personal Information
# Create variables for:

# Name
# Age
# City
# Qualification
# Experience
# Display all information.

name="Neel"
age=21
city="Ahmedabad"
Qualification="BCA"
Experience="Fresher"

print(name)
print(age)
print(city)
print(Qualification)
print(Experience)


# Task 2 — Employee Salary
# Create:

# basic_salary = 30000
# allowance = 5000
# bonus = 3000
# Calculate:

# Total Salary = Basic Salary + Allowance + Bonus

basic_salary = 30000
allowance = 5000
bonus = 3000

Total_Salary = basic_salary + allowance + bonus

print(Total_Salary)


# Task 3 — Sales Calculation
# Create:

# quantity = 10
# unit_price = 2500
# Calculate total sales.

quantity = 10
unit_price = 2500
total_sales= quantity * unit_price

print(total_sales)


# Task 4 — Profit Calculation
# Create:

# sales = 100000
# cost = 75000
# Calculate:

# Profit
# Profit Percentage
# Formula:

# Profit = Sales - Cost
# Profit % = (Profit / Sales) × 100

sales = 100000
cost = 75000

profit = sales - cost 
Profit_percentage= (profit/sales)*100

print(profit)
print(Profit_percentage)


# Task 5 — Average Marks
# Create marks for five subjects:

# Python
# SQL
# Excel
# Power BI
# Statistics
# Calculate:

# Total marks
# Average marks

Python=50
SQL=44
Excel=78
Power_BI=80
Statistics=72

Total_Marks= Python + SQL + Excel + Power_BI + Statistics
Average_Marks= Python + SQL + Excel + Power_BI + Statistics / 5

print(Total_Marks)
print(Average_Marks)


# Task 6 — Customer Bill
# Take the following from the user:

# Product name
# Quantity
# Unit price
# Calculate and display:

# Product
# Quantity
# Unit Price
# Total Amount

Product_name=input("Enter Product Name:-")
Quantity=int(input("Enter Quantity:-"))
Unit_price=float(input("Enter Unit Price:-"))

Total_Amount = Quantity * Unit_price

print(Product_name)
print(Quantity)
print(Unit_price)
print(Total_Amount)


# Task 7 — Discount Calculation
# Given:

# price = 50000
# discount = 10
# Calculate:

# Discount Amount
# Final Price
# Formula:

# Discount Amount = Price × Discount / 100
# Final Price = Price - Discount Amount

price = 50000
discount = 10

Discount_Amount = price * discount/100
print(Discount_Amount)

Final_Price = price - Discount_Amount
print(Final_Price)


# Task 8 — Data Analyst Salary
# Take the following inputs:

# Employee Name
# Monthly Salary
# Calculate:

# Annual Salary
# Formula:

# Annual Salary = Monthly Salary × 12

Employee_Name =input("Enter Employee Name:-")
print(Employee_Name
      )
Monthly_Salary =float(input("Enter Monthly Salary"))
print(Monthly_Salary)

Annual_Salary = Monthly_Salary * 12
print(Annual_Salary)



#Lecture Activity — Real Business Problem

Quantity = 150
Selling_Price = 45000
Cost_Price = 38000

Total_Revenue = Quantity * Selling_Price
print(Total_Revenue)

Total_Cost =  Quantity * Cost_Price
print(Total_Cost)

Total_Profit = Total_Revenue - Total_Cost
print(Total_Profit)


#Homework

# Problem 1
# Create a program that accepts:

# Employee name
# Monthly salary
# Bonus
# Calculate annual income.

Employee_name = "Neel"
Monthly_salary = 30000
Bonus = 10000

Annual_income = (Monthly_salary * 12 )+ Bonus
print(Annual_income)


# Problem 2
# Create a program that accepts:

# Product name
# Quantity
# Price
# Discount %
# Calculate the final bill amount.

Product_name =input("Enter Product Name:-")
Quantity = int(input("Enter Quantity:-"))
Price = float(input("Enter Price:-"))
Discount_percentage =float(input("Enter Discount Percentage:-"))

Total_Amount = Quantity * Price
print(Total_Amount)

Discount_Amount = (Total_Amount * Discount_percentage) /100
print(Discount_Amount)

Final_Bill = Total_Amount - Discount_Amount
print(Final_Bill)


# Problem 3
# A company has:

# January Sales = ₹50,000
# February Sales = ₹65,000
# March Sales = ₹75,000
# Calculate:

# Total Sales
# Average Sales
# Highest Sales
# Lowest Sales

January_Sales = 50000
February_Sales = 65000
March_Sales = 75000

Total_Sales = January_Sales + February_Sales + March_Sales
print(Total_Sales)

Average_Sales = Total_Sales / 3
print(Average_Sales)

Highest_Sales = max(January_Sales , February_Sales , March_Sales)
print(Highest_Sales)

Lowest_Sales = min(January_Sales , February_Sales , March_Sales)
print(Lowest_Sales)

