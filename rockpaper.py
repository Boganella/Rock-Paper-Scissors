import random

winCondition = {"rock":"paper",
                "paper":"scissors",
                "scissors":"rock"}

winQuote = "%s wins!\nYou chose %s.\nCPU chose %s!"



while True:
        
        cpuChoice = random.choice(list(winCondition.keys()))
        
        playerChoice = input("Rock paper scissors shoot!\n") # to-do : clean input 

        if playerChoice == cpuChoice:
                print("Draw")

        elif cpuChoice == winCondition[playerChoice]:
                print(winQuote % ( "CPU", playerChoice, cpuChoice))
        else: 
                print(winQuote % ("You", playerChoice, cpuChoice))


""" to-do list:
create gameplay loop  x
        Implement continue / exit functionality

add score keeping 

refactor game logic x
        move all game logic off main file

create front end for game

add dynamic winquotes

add error checking 

"""