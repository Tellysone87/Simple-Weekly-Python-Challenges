## Author:Shantel Williams
## Date: 12/5/2022
## FileName: Week 22 Python Challenge
##
## Description: Write a function called single_letter_count. This function takes in two parameters (two strings). 
## The first parameter should be a word and the second should be a letter. 
## The function returns the number of times that letter appears in the word. 
## The function should be case insensitive (does not matter if the input is lowercase or uppercase).
## If the letter is not found in the word, the function should return 0. 
####################################################################################################################################

## Solution function
def single_letter_count(word, letter):
    number = 0 # variable used to store the number of instances
    letterMatched = False # Setting matches to false

    for eachletter in word: # looping through each indidvidual letter of giving word.
        if letter == eachletter.lower() or letter == eachletter.upper(): # Checking for the letter provided
            number += 1
            letterMatched = True # We have found letter in word

    if letterMatched == True: # If the program found matches, it should return the number
        return number
    else: # If no matches were found, it return 0 
        return 0

## Defined main function
def main():
    numberOfMatches = single_letter_count("Lilly", "l")# Function call with arguments 
    numberOfMatches2 = single_letter_count("Titles", "T")
    numberOfMatches3 = single_letter_count("SUNNY", "n")
    numberOfMatches4 = single_letter_count("telephone", "Z")
    print(numberOfMatches)
    print(numberOfMatches2)
    print(numberOfMatches3)
    print(numberOfMatches4)

## Run it!
main()