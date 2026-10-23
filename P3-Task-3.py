'''' Print all numbers from 1 to 50.'''

for i in range(1,101):
    print(i)

'''Print all even numbers between 1 and 100.'''

for numbers in range(2,101,2):
    print(numbers)

'''Calculate the sum of numbers from 1 to 100.'''

total=0
for number in range(1,101):
    total+=number
print("sum:",total)

'''Calculate the total and average of a list of 10 sales values.'''

sales=[40000,50000,10000,30000,60000,
       20000,70000,90000,80000,35000]

total=0
for i in sales:
    total+=i

    avg=total/len(sales)
print("Total Sales:",total)
print("Average:",avg)

'''Count how many sales values exceed ₹50,000.'''

sales=[40000,50000,10000,30000,60000,
       20000,70000,90000,80000,35000]

count=0
for i in sales:
    if i > 50000:
        count+=1
print("Total Sales Value:",count)


'''Find the highest sales value without using max().'''

sales=[40000,50000,10000,30000,60000,
       20000,70000,90000,80000,35000]

highest=sales[0]
for i in sales:
    if i > highest:
        highest=i
print("Highest value:",highest)

'''Find the lowest sales value without using min().'''

sales=[40000,50000,10000,30000,60000,
       20000,70000,90000,80000,35000]

lowest=sales[0]
for i in sales:
    if i < lowest:
        lowest=i
print("Lowest value:",lowest)


'''Count the number of negative values in a list of transactions.'''

sales=[40000,50000,-280,30000,60000,
       20000,-450,90000,80000,-884]

count=0
for i in sales:
    if i < 0:
        count+=1
print("Negative Value:",count)


'''Calculate profit for each product using separate sales and cost lists.'''

sales=[40000,50000,30000,60000]
cost=[20000,35000,10000,25000]

for i in range(len(sales)):
    profit=sales[i]-cost[i]
    print("Product:",i+1,"Profit:",profit)


'''Count how many students passed, given a list of marks and a passing score of 35.'''
marks=[57,35,68,56,79,50]
passed=0
for i in marks:
    if i >35:
        passed+=1
print("Pass MArks:",passed)


'''Print customer names from a list, skipping empty strings.'''
name =["Rahul","","Mohan","","Hiten"]

for i in name:
    if name!="":
        print(i)

  
'''Use a while loop to display numbers from 10 down to 1.'''
i=10
while i >=1:
    print(i)
    i=i-1

'''Stop processing a list when the first value greater than ₹1,00,000 is found.'''
sales=[40000,50000,30000,60000,59000,80000,100000,150000]
for value in sales:
    if value>100000:
        print("First Value:",value)
        break
    print("Processing:",value)


'''Calculate total revenue for a list of product quantities and prices.'''

price=[300,200,450,350,500]
quantity=[10,3,5,7,15]
total_revenue=0
for i in range(len(quantity)):
    total_revenue=quantity[i]*price[i]
    total_revenue+=1
print("Total Revenue:",total_revenue)


'''Build a sales report showing total sales, average sales, highest sales, and number of high-sales days.'''
sales=[20000,30000,45000,57000,80000,38000,68000]
total_sales=0
highest_sales=sales[0]
highest_sales_days=0
for i in sales:
    total_sales+=i
    if i>highest_sales:
       highest_sales=i
    if i>50000:
        highest_sales_days+=1

average_sales=total_sales/len(sales)
print("Total Sales:",total_sales)
print("Highest Sale:",highest_sales)
print("Highest Sales Days:",highest_sales_days)
print("Average Sales:",average_sales)



#homework

sales = [25000, 60000, 45000, 80000, 15000,
         95000, 50000, 70000, 18000, 40000]

total = 0
count_above_50000 = 0
count_below_20000 = 0
highest = sales[0]
lowest = sales[0]
count = 0

print("Daily Sales Report")
for i in sales:
    print(i)
    total+=i
    count+=1
    if i > highest:
        highest=i

    if i < lowest:
        lowest =i 

    if i >50000:
        count_above_50000+=1

    if i <20000:
        count_below_20000+=1

avg=total/len(sales)
percentage = (count_above_50000 / count) * 100 

print("\n----- Sales Summary -----")
print("Total Sales:", total)
print("Average Sales:", avg)
print("Highest Sales:", highest)
print("Lowest Sales:", lowest)
print("Days above 50000:", count_above_50000)
print("Days below 20000:", count_below_20000)
print("Percentage above 50000:", percentage, "%")

