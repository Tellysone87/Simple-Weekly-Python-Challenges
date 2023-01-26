## Author:Shantel Williams
## Date: 1/23/2023
## FileName: rock paper scissors Challenge
##Create a program that simulates rock, paper, scissors!
####################################################################################################################################
import random
choices = ["Rock","Paper","Scissors"] #list of choices

## Steps:
## 1.greet player and ask for choice
def greetAndPrompt():
    print("Welcome to my Rock, Paper and Scissors Simulation!")

    playerHand = "" ## player hands after check is completed
    correctChoice = False #using to check if choice is correct
    playerInput = "" ## payer input

    while correctChoice == False: ## loops until the required correct choice is giving
        playerInput = input("Please enter a choice.") ## input
        for items in choices:
                if playerInput == items:
                    playerHand = playerInput
                    correctChoice = True
                    return playerHand  

## 2.Have computer generate random choice
def computerHand():
    computerRandomChoice = random.choice(choices)
    return computerRandomChoice

## 3.Compare hands
def CompareHands(playerAnswer,ComputerAnswer):
   
   if playerAnswer == ComputerAnswer: ## Draw game and conditionals
       return "Its a draw!"
   elif playerAnswer == "Rock" and ComputerAnswer == "Paper":
       return "You have lost!"
   elif playerAnswer == "Rock" and ComputerAnswer == "Scissors":
       return "You have Won!"
   elif playerAnswer == "Paper" and ComputerAnswer == "Scissors":
       return "You have lost!"
   elif playerAnswer == "Paper" and ComputerAnswer == "Rock":
       return "You have Won!"
   elif playerAnswer == "Scissors" and ComputerAnswer == "Paper":
       return "You have Won!"
   elif playerAnswer == "Scissors" and ComputerAnswer == "Rock":
       return "You have Won!"

#main function
def main():
    player1 = greetAndPrompt()
    computer = computerHand()
    Compared = CompareHands(player1,computer)
    print("Player Choice: " + player1)
    print("Computer Choice:" + computer)
    print("Results: " + Compared)

#run it 
main()