#2 ways to create a set
set1 = {"Ali Assi", "Lara Ayass", "Lea Haidamous", "Daisy Doe", "John Doe"}

set2 = set(("Ali Assi", "Lara Ayass", "Lea Haidamous", "Lea Haidamous"))

print(set1,"\n")
print(set2,"\n")

#True and 1 represent the same value
myset = {1, True, 2}
print(myset)

#some methods of sets:
set1.add("John Doe")
print(set1.intersection(set2)) 
set1.pop() #pops the last element as it counts in the hashset, not in the way you wrote it
print(set1)
set1.remove("Daisy Doe")
print(set1)