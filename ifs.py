#Let's check if students passed their exam or not.
#A grade less than 60 means a fail
#A grade above 60 means a pass
#A grade of 60 means probation

print("example 1 : assessing student grade:")
student1_grade = int(input("Enter student1's grade: "))
if student1_grade < 60:
    print("student1 failed the exam")
elif student1_grade == 60:
    print("student1 is on probation")
else:
    print("student1 passed the exam")

#If statements can be written as "short hand", consider example 2:
print("\nexample 2 : Comparing 2 numbers")
n1 = float(input("enter the first number: "))
n2 = float(input("enter the second number: "))
print("bigger number: ", n1) if n1>n2 else print("they are =") if n1==n2 else print("bigger number: ", n2)
#This example is similar to if elif else. 

#Example 3 on short hand statements:
print("\nexample 3 : comparing a number with thresholds")
min = 1
max = 5
myNumber = int(input("enter a number: "))
#if you just need an if statement
if myNumber > min and myNumber < max : print("You are within the limits")
#if you also need an else statement
print("you are within the limits") if myNumber > min and myNumber < max else print("you went outside the limits")

