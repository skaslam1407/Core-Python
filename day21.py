# Number Predict Game
import random

def number_predict(x):
    random_number = random.randint(1, x)
    #print(f'The random number is {random_number}')
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!')

number_predict(5)    