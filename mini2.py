# Guess the number game - MATKA
import random as r

number = r.randint(1, 10)
print(number)

for i in range(0, 3):
    guess = int(input('Guess the number: '))
    if guess == number:
        print('You won')
        break
    else:
        print('Wrong guess.')
        if i == 2:
            print('You lost. Play again')
            print('The number was ', number)
