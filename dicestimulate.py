import random

title = "Dice Simulation"
y = title.center(70)
y = y.upper()
print(y)

x = "y"
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




