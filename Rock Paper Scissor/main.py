# first import a module to select random no and assign a variable
import random
rand = random.randint(1, 3)
# create a function and assign the conditions to the function
def gameWin(com,you):
    if com==you:
        return None

    elif com=="rock":
        if you=="paper":
            return True
        elif you=="scissor":
            return False

    elif com=="paper":
        if you=="scissor":
            return True
        elif you=="rock":
            return False

    elif com=="scissor":
        if you=="rock":
            return True
        elif you=="paper":
            return False
# assign the name to the random choices.
if rand==1:
    com="rock"
elif rand==2:
    com = "paper"
elif rand==3:
    com = "scissor"
#take input and print!
you  = input("Enter your choice = ")
a= gameWin(com, you)
print(f"Computer choose = {com}")
           # print(f"You choose = {you}")
if a== None:
    print("The game is tie")
elif a:
    print("You win!")
else:
    print("You lose")