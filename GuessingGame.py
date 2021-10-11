import random

randomNumber = random.randint(1,9)

chances = 0 

while chances < 5:
    guess = int(input('Enter your guess'))
    if guess == randomNumber:
        print('Congrats !! You WIN !!')
        break

    elif guess < randomNumber:
        print('You guess was too small, guess a number higher than ', guess)
        
    else:
        print('You guess was too big, guess a number lower than ', guess)

    chances += 1

if chances > 5:
    print('You LOSE !! The number is ', randomNumber)