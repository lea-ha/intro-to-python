#Tuple : A tuple is a collection which is ordered and unchangeable. It is used to group together related data.
#It can be useful for storing records.

#There are 2 ways to create a tuple:

LaraInfo = ("Lara", "Computer Engineering", 2021)

LeaInfo = tuple(("Lea", "Computer Engineering", 2021))

#Here we used tuples to store name, majors and date of enrollment of three students.

Abby = ("Abby","Computer Engineering",2021)
John = ("John","Mechatronics Engineering",2020)
Daisy= ("Daisy", "Computer Science", 2022)

#Some methods of tuples

print(Daisy.index(2022))
print(John.count("Mechatronics Engineering"))

#nb: a single valued tuple must be written in this way, or else it won't be considered a tuple:
myFirstName = ("Lea")
print("myFirstName's class: ", myFirstName.__class__)
myLastName = ("Haidamous",)
print("myLastName's class: ", myLastName.__class__)

