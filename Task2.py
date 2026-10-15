#  Hands-on Tasks


# Task 1 — Number Classification
#  Take a number and determine whether it is:

#  Positive
# Negative
#  Zero

# number=int(input("Enter Number:-"))
# print("Number:-",number)

# if number >0:
#     print("Positive")
# elif number <0:
#     print("Negative")
# else:
#     print("Zero")




# Task 2 — Even or Odd
# Take a number and determine whether it is even or odd. Use %.

# number=int(input("Enter Number:-"))
# print("Number:-",number)


# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")




# Task 3 — Sales Classification
# Sales	Category
# >= 100000	Excellent
# >= 75000	Good
# >= 50000	Average
# < 50000	Poor


# Sales=float(input("Enter Sales:-"))
# print(Sales)

# if Sales >= 100000:
#     Sales_Category="Excellent"
# elif Sales >= 75000:
#     Sales_Category="Good"
# elif Sales >= 50000:
#     Sales_Category="Average"
# else:
#     Sales_Category="Poor"

# print(Sales_Category)




# Task 4 — Profit or Loss
# Take sales and cost and determine profit or loss.

# Sales =float(input("Enter Sales:-"))
# print("Sales:-",Sales)

# Cost =float(input("Enter Cost:-"))
# print("Cost:-",Cost)

# Profit =Sales - Cost 
# print(Profit)

# if Profit >=0:
#     print("Profit")

# else:
#     print("Loss")




# Task 5 — Customer Segmentation
# Purchase	Customer Type
# >= 100000	Premium
# >= 50000	Gold
# >= 25000	Silver
# < 25000	Regular

# Sales =float(input("Enter Sales:-"))
# print("Sales:-",Sales)


# if Sales >= 100000:
#     Customer_Type="Premium"
# elif Sales >= 75000:
#    Customer_Type ="Gold"
# elif Sales >= 50000:
#    Customer_Type ="Silver"
# else:
#     Customer_Type="Regular"

# print(Customer_Type)



# Task 6 — Discount Calculator
# Amount	Discount
# >= 100000	20%
# >= 50000	10%
# >= 25000	5%
# < 25000	0%
# Calculate the final amount.

# amount=float(input("Enter AMount:-"))
# print(amount)

# if amount >= 100000:
#     Discount="20"
# elif amount >= 50000:
#    Discount ="10"
# elif amount >= 25000:
#    Discount ="5"
# else :
#     Discount="0"

# print(Discount,"%")



# Task 7 — Employee Bonus
# Take employee sales and profit.

# Sales >= 100000 AND Profit >= 20000
# → Bonus Eligible

# Otherwise
# → Not Eligible

# Sales =float(input("Enter Sales:-"))
# print("Sales:-",Sales)

# Profit =float(input("Enter profit:-"))
# print("profit:-",Profit)

# if Sales >= 100000 and Profit >= 20000:
#     Employee_Bonus="Eligibal"
# else:
#     Employee_Bonus="Not Eligibal"
# print(Employee_Bonus)



# Task 8 — Data Validation
# Take customer age.

# 18 to 100 → Valid
# Otherwise → Invalid

# Age=int(input("Enter Age:-"))
# print(Age)

# if Age>=18 and Age<=100:
#     Data_Validation="Valid"
# else:
#     Data_Validation="Invalid"

# print(Data_Validation)



# Task 9 — Student Result
# 90+ → A
# 75–89 → B
# 60–74 → C
# 35–59 → D
# Below 35 → Fail

# Marks=float(input("Enter Marks:-"))
# print(Marks)

# if Marks >=90:
#     Student_Result="A"
# elif Marks >=75:
#     Student_Result="B"
# elif Marks >=60:
#     Student_Result="C"
# elif Marks >=35:
#     Student_Result="D"
# else:
#     Student_Result="Fail"
# print(Student_Result)



# Task 10 — Order Validation
# Take quantity and unit price.

# Both must be greater than 0.

# Display Valid Order or Invalid Order.

# quantity=int(input("Enter Quantity:-"))
# print(quantity)

# unit_price=int(input("Enter Unit_Price:-"))
# print(unit_price)

# if quantity >=0 and unit_price >=0:
#     Order_Validation="Valid"
# else:
#     Order_Validation="Invalid"
# print(Order_Validation)



# 20. Challenge Task — Customer Classification
# Take:

# Customer Name
# Purchase Amount
# Number of Orders
# Rules
# Premium:
# Purchase >= 100000 AND Orders >= 10

# Gold:
# Purchase >= 50000 AND Orders >= 5

# Silver:
# Purchase >= 25000

# Regular:
# Everything else
# Display:

# Customer Name
# Purchase Amount
# Number of Orders
# Customer Segment


Customer_Name=input("Enter Customer Name:-")
print(Customer_Name)

Purchase_Amount=float(input("Enter Purchase Amount:-"))
print(Purchase_Amount)

Number_Of_Orders=int(input("Enter NO Of Orders:-"))
print(Number_Of_Orders)

if Purchase_Amount >= 100000 and Number_Of_Orders >= 10:
    Customer_Segment="Premium"
elif Purchase_Amount >= 50000 and Number_Of_Orders >= 5:
    Customer_Segment="Gold"
elif Purchase_Amount >= 25000:
    Customer_Segment="Silver"
else:
    Customer_Segment="Regular"
print(Customer_Segment)