# Dice roll stimulator
import random as r

while True:
    print('1. Roll the dice\n2. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print('Rolling the dice...')
        print(r.randint(1, 6))
    else:
        break
