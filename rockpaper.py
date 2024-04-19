# Script that plays rock paper scissors with me

from random import *

options = ['rock' , 'paper' , 'scissors']

def openingSequence():
    print("Welcome to Rock Paper Scissors!\n")
    print("I will be your opponent today!\n")
    print("When you're ready, just input Rock, Paper, or Scissors\n")
    print("Oh, and don't worry about me cheating! I won't I promise, cross my fingers :)\n")

def playerAI():
    return void
    

def gameRules():
    return void

def get_prompt():
    answerRequest = True
    while answerRequest:  
        response = input("Rock paper scissors shoot~! ")
        if response not in options:
            print("try again sillypuss")
        else:
            answerRequest = False
            break
    return(response)
    
       
def mainLoop():
    openingSequence()
    get_prompt()
    


mainLoop()
