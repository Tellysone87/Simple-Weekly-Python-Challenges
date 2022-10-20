## Title: Week 16 Coding Challenge
## Author: Shantel Williams
## Date: 10/10/2022
##
## Challenge: Create a function that takes a single string as argument and
## returns an ordered list containing the indices of all capital letters in the string.
##
########################################################################################################################################

##Libraries
import string


##Solution function that takes a single string argument.
def index_of_caps(stringInput):
    indices = [] ## Blank list to collect capital letter positions.
    
    for letter in stringInput: ## looping through each letter in the giving string.
        if letter.isupper() == True: ## If the letter is uppercase,
            indices.append(stringInput.index(letter)) ## Add the position to the blank indices list.

    sortedIndicesList = sorted(indices) ## Created a list with the ordered values. 
    print(sortedIndicesList) 
    
##Declare main
def main():
    index_of_caps("eDaBiT")
    index_of_caps("eQuINoX")
    index_of_caps("determine")
    index_of_caps("STRIKE")
    index_of_caps("sUn")


##run code
main()
