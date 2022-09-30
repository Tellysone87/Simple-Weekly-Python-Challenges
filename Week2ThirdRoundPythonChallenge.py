## Title: Week 2 Third Round Challenge
## Author: Shantel Williams
## Date: 9/20/2022
##
## Challenge: Create a function that takes a list of strings as input.
## Join each string in the list to create and return one complete string.
## Each word should have a space between them.
##
########################################################################################################################################

## Import libraries
import string

##Solution function
def userStringList():

    inputList= [] #Creat blank list
    listLength = int(input("Enter number of words to be used. \n")) #Get the number of words from user
    print("Enter words: \n")
    for i in range(listLength): #take input until length is met
        data = input()
        inputList.append(data) #append to list

    ##joining each word in the list to one String and adding space between each entry.
    oneString = ' '.join(inputList) # used join() to concatenate list elements. 
    print(oneString)


## create main function
def main():
    userStringList()


## run code
main()
