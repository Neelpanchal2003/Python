# Q1
# Create variables for:

# name
# age
# percentage
# is_pass
# Print their data types.

name="Neel"
age=20
percentage=80.78
is_pass=True

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_pass))

# Q2
# Create a list of 5 cities and replace one city.

City=["Ahmedabad","Surat","Mumbai"]

City[1]="Rajasthan"
print(City)

# Q3
# Create dictionary of student information.

Student={"Name":"Neel",
         "Age":20,
         "Percentage":79.89,
         "City":"Jaipur",
         }
print(Student)


# Q4
# Convert:

# "100" → int
# 50 → string
# 10 → float


Text="100"
New_Text=int(Text)
print(New_Text)


num = 50
Text=int(num)
print(Text)


x=20
print(float(x))





#Homwork#

'''Create a student database using dictionary'''

students = {
    1: {
        "name": "Rahul",
        "age": 20,
        "city": "Ahmedabad",
        "marks": 85
    },
    2: {
        "name": "Priya",
        "age": 21,
        "city": "Surat",
        "marks": 90
    },
    3: {
        "name": "Amit",
        "age": 19,
        "city": "Vadodara",
        "marks": 78
    }
}

print("Student Database")

for student_id, details in students.items():
    print("\nStudent ID:", student_id)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("City:", details["city"])
    print("Marks:", details["marks"])


'''Create a shopping cart using list'''

shopping_cart = []

shopping_cart.append("Laptop")
shopping_cart.append("Mouse")
shopping_cart.append("Keyboard")
shopping_cart.append("Headphones")

print("Shopping Cart:", shopping_cart)

# Remove an item
shopping_cart.remove("Mouse")

print("Updated Shopping Cart:", shopping_cart)

# Display total number of items
print("Total Items:", len(shopping_cart))


'''Explain mutable vs immutable with examples'''
#mutable
list=[10,20,30]
list[0]=100
print(list)

#immutable
name="Neel"
name=name + " Panchal"
print(name)

'''Create a program using all data types together'''
# 1. Integer
age = 21

# 2. Float
percentage = 75.45

# 3. String
name = "Neel"

# 4. Boolean
is_Employee = True

# 5. List
City = ["Ahmedabad", "Surat", "Maheshana"]

# 6. Tuple
marks = (85, 90, 88)


# 7. Set
skills = {"Communication", "Writing", "Reading"}

# 8. Dictionary
student = {
    "name": "Neel",
    "age": 21,
    "city": "Ahmedabad"
}

print(age, type(age))
print(percentage, type(percentage))
print(name, type(name))
print(is_Employee, type(is_Employee))
print(City, type(City))
print(marks, type(marks))
print(skills, type(skills))
print(student, type(student))
