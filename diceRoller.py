import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []  
total = 0

while True: 
  try:
    num_of_dice = int(input("How many dices do you want to roll?: "))
    break 
  except ValueError:
    print("Oops! You need to input an integer.")

# generate random numbers

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# display the elements of the list

print("Result:", dice)

# check the number of dice along with the corresponding tuples

for die in range(num_of_dice):          
   for line in dice_art.get(dice[die]): 
       print(line)

# iterate and sum all the elemets within the list

for die in dice:
    total += die
print(f"Total: {total}")