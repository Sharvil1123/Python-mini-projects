import random

def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        
        feedback = input(f"is {guess} too high(h), or too low(l) or correct(c)").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low  = guess + 1
    print("congratulations comp guessed your number correctly")


guess(55)
        