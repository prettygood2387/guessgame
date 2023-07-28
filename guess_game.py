import random
num = random.randint(1,6)
guess = 0
while guess != num:
    guess = input('Guess a number between 1 and 10: ')
    guess = int(guess)

    if guess ==num:
        print('WOW!! \nYou Won.')
        break
    else:
        print('SORRY!! \nTry Again.')

