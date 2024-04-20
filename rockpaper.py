# Script that plays rock paper scissors with me

import random

options = ('rock' , 'paper' , 'scissors')
computerAction = random.choice(options)
playerAction = input("Rock paper scissors shoot~! ")


if playerAction == computerAction:
    print(f"Golly we both picked {playerAction} no way!!")
elif playerAction == 'rock':
    if computerAction == 'scissors':
            print("Holy smokes you SMASHED me!")
    else:
            print("Guess I got ya covered~! I win :)")
elif playerAction == 'paper':
    if computerAction == 'rock':
            print("Paper beat's rock, you're really good at this~!")
    else:
            print("Talk about cutting the competition down to size, I win this one~!")
elif playerAction == 'scissors':
    if computerAction == 'paper':
            print("Goodness take no prisoners, it's a cutthroat business. You win~!")
    else:
            print("I totally rocked your world admit it. I win~!")



       

