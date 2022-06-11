import random

Options = { "R":"rock", "P":"paper", "S":"scissors"}
Player = input("Please Enter an Option: ")
for i in Options:
    if Player not in Options:
        print("This is not a valid choice. Enter again!")
        Player = input("Please Enter an Option: ")
        
Computer = random.choice(list(Options))
print(Player, ":", Computer)

if Player == "R" and Computer =="S":
    print("You win!")
elif Player =="S" and Computer == "R":
    print("Computer wins!")

if Player == "P" and Computer =="R":
    print("You win!")
elif Player == "R" and Computer == "P":
    print("Computer wins!")

if Player == "S" and Computer =="P":
    print("You win!")
elif Player == "P" and Computer == "S":
    print("Computer wins!")

if Player == Computer:
    print("It is a tie!")


