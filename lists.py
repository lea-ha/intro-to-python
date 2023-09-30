#2 ways to create a list:

countries_list = ["Lebanon", "USA", "France", "Italy", "Japan"]


languages_list = list(("Arabic", "English", "French", "Italian", "Japanese"))



#Illustrating list methods through a groceries list example:
groceries_list = ["milk", "bread", "eggs", "lettuce"]
print("Initial list", groceries_list)

#I found eggs, I can now remove eggs from my list, to do so:
groceries_list.remove("eggs")
print("After removing eggs", groceries_list)

#I forgot that I need butter, I can add that element to the list:
groceries_list.append("butter")
print("After adding butter", groceries_list)

#I ran out of water, I should add it as the first element of the list to remember buying it:
groceries_list.insert(0,"water")
print("After adding water", groceries_list)

#How many items do I need to buy now?
print("list length",len(groceries_list))

#What is the last element that I need?
print("Last element I need", groceries_list[len(groceries_list)-1])

