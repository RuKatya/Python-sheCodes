# if statement = a block of code that will execute if it's condition is true

# age = int(input("How old are you?: "))

# if age == 100:
#     print('Too old!')
# elif age >= 18:
#     print("Adult!")
# elif age < 0:
#     print('It\'s not exist!')
# else:
#     print('Child')

# PRACTICE
# !----- 1 -----!
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

# ---- answer ----
# service = int(input("Enter your year service: "))
# salary = int(input("Enter your salary: "))

# if service > 5:
#     print(salary + salary*0.05)
# else:
#     print(salary)

# !----- 2 -----!
# Take values of length and breadth of a rectangle from user and check if it is square or not.

# ---- answer ----
# lenght = int(input("Enter lenght: "))
# breadth = int(input("Enter breadth: "))

# if lenght*breadth == lenght**2:  # if length == breadth:
#     print("Square")
# else:
#     print("Note")

# !----- 3 -----!
# Take two int values from user and print greatest among them.

# ---- answer ----
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# if num1 > num2:
#     print("The bigger is :" + str(num1))
# elif num2 > num1:
#     print("The bigger is :" + str(num2))
# else:
#     print("Equel")

# !----- 4 -----!
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

# ---- answer ----
# quantity = int(input("Enter quantity: "))
# total_cost = quantity*100
# total_discount = total_cost*0.1

# if total_cost > 1000:
#     print("The discount will be: " + str(total_discount))
# else:
#     print("The discount will be: 0")

# !----- 5 -----!
# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# ---- answer ----
# grade = int(input("Enter grade: "))

# if grade > 80:
#     print("A")
# elif grade > 60:
#     print("B")
# elif grade > 50:
#     print("C")
# elif grade > 45:
#     print("D")
# elif grade > 25:  # elif marks>=25 and marks<45:
#     print("E")
# elif grade < 25:
#     print("F")

# !----- 6 -----!
# Take input of age of 3 people by user and determine oldest and youngest among them.

# ---- answer ----
# first = int(input("Enter first age: "))
# second = int(input("Enter second age: "))
# third = int(input("Enter third age: "))

# if first >= second and first >= third:
#     print("Oldest is" + str(first))
# elif second >= first and second >= third:
#     print("Oldest is" + str(second))
# elif third >= first and third >= second:
#     print("Oldest is" + str(third))
# else:
#     print("All are equal")

# !----- 7 -----!
# Write a program to print absolute value of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

# ---- answer ----
# value = int(input("Enter value: "))

# print(str(abs(value)))

# !----- 8 -----!
# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# ---- answer ----
# noh = int(input("Number of classes held: "))
# noa = int(input("Number of classes attended: "))
# atten = (noa/float(noh))*100

# print("Attendence is" + str(atten))

# if atten >= 75:
#     print("You are allowed to sit in exam")
# else:
#     print("Sorry, you are not allowed. Attend more classes from next time.")

# !----- 9 -----!
# Modify the above question to allow student to sit if he/she has medical cause.
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

# ---- answer ----
# Hint only
# Do it yourself
# if medical_cause == 'Y':
#   print "You are allowed"
# else:
#   if atten>=75:
#     print "Allowed"
#   else:
#     print "Not allowed"
