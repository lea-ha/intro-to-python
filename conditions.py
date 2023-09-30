#Let's take a look at all the logical operators in python:
number1 = 10
number2 = 10
number3 = 30

if number1 > number2 : print("1)", number1, ">", number2)
if number1 >= number2 : print("2)", number1, ">=", number2)
if number1 < number2 : print("3)", number1, "<", number2)
if number1 <= number2 : print("4)", number1, "<=", number2)
if number1 >= number2 and number3>number2 : print("5)", number3,">",number2,">=",number1)
if number1 >= number2 or number3 >= number2 : print("6)", number3, " or ", number1, ">=", number2)
if not number1 > number3 : print("7)",number3,">",number1)
