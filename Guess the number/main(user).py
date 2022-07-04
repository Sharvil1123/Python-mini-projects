import random



def guess_by_user(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!=random_number:
        guess = int(input(f"Enter the guess between 1 and {x}  => "))
        if guess<random_number:
            print("Select a bigger number")
        elif guess> random_number:
            print("Select a smaller number")
    print("Congrats you gueessed it correctly")




guess_by_user(10)

