
fruitsList = ("apple", "banana", "cherry", "watermelon", "pear", "avocado")

#2 ways to iterate over an iterable
for x in fruitsList: #Creating using an iterable
    print("using iterable: ", x)


for x in range(len(fruitsList)): #Creating using the range function
    print("using[]: ", fruitsList[x])

#Illustrating overloaded method range and the else in for loops
for x in range(2,4):
    print(fruitsList[x])
else:
    print("The for loop finished!\n\n\n")

#Showing the break and continue statement
#I want to buy only apple and cherry from the list:
for x in fruitsList:
    #I dont want bananas
    if(x == "banana"): 
        continue
    #everything from watermelon and beyond I dont need.
    if(x == "watermelon"):
        break
    print(x)


