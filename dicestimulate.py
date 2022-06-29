#import random module to randomly select a number between 0 & 7
import random

#Give title in the center
title = "Dice Simulation"
y = title.center(70)
# Change the title to uppercase
y = y.upper()
print(y)

x = "y"
# Let's loop through 1 to 6 to pick the number as rolling the dice for a number
while x == "y":
    Numb = random.randint(1,6)
    x = input("press y to continue ")
    x = x.lower()
    
    if x != "y":
        break
    

    if Numb == 1:
        print("--------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("--------")
        print("1")
    if Numb == 2:
        print("--------")
        print("|       |")
        print("|   00  |")
        print("|       |")
        print("--------")
        print("2")
    if Numb == 3:
        print("--------")
        print("|       |")
        print("|   00  |")
        print("|    0  |")
        print("|       |")
        print("--------")
        print("3")
    if Numb == 4:
        print("--------")
        print("|       |")
        print("|   00  |")
        print("|   00  |")
        print("|       |")
        print("--------")
        print("4")
    if Numb == 5:
        print("--------")
        print("|       |")
        print("|  000  |")
        print("|  00   |")
        print("|       |")
        print("--------")
        print("5")
    if Numb == 6:
        print("--------")
        print("|       |")
        print("|  000  |")
        print("|  000  |")
        print("|       |")
        print("--------")
        print("6")




