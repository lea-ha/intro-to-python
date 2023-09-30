
fruitsList = ("apple", "banana", "cherry", "watermelon")

#2 ways to iterate over an iterable
for x in fruitsList: #Creating using an iterable
    print(x)


for x in range(len(fruitsList)): #Creating using the range function
    print(fruitsList[x])

#Illustrating overloaded method range and the else in for loops
for x in range(2,4):
    print(fruitsList[x])
else:
    print("The for loop finished!\n")

