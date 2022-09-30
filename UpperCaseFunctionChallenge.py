## Title: Week 1 Third Round Challenge
## Author: Shantel Williams
## Date: 9/19/2022
##
## Challenge: Create a function that takes a string as a input and capitalizes it. 
## 
##
## 
## Solution: To complete this funtion. I used the rsults of a input function an then
## called this function to be capitalized. 
##
########################################################################################################################################

## Import libraries
import string



## function to get sting from user
def promptUser():
    print("Hello There!")
    UserInput = input("Please enter a word.\n ")
    boldWord = UserInput
    print("You entered: " + boldWord)
    return UserInput

## function to capitalize string
def UpperCase(userWord):
    capitalized = userWord.capitalize()
    print("The user word capitalized is: " + capitalized)
    
    
## Main function
def main():
    Word = promptUser()
    UpperCase(Word)

## run code    
main()
