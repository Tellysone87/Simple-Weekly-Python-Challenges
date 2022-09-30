## Title: Week 3 Third Round Challenge
## Author: Shantel Williams
## Date: 9/23/2022
##
## Challenge: Create a function that takes a list of non-negative integers
## and strings. The function will then return a new list without the strings.
##
########################################################################################################################################

## Import libraries
import string

##Solution function
def filterList(providedList):

    ## Needed variables and list
    newList = [] # Create a new list for results
    correctData = True # I used this variable to let the program know when it can proceed with filtering.

    #####################################################################
    ## Check to ensure elements are of string and non-negative integers.#
    #####################################################################

    for item in providedList: ## Loop to check elements and display error messages if needed.

        if type(item) != str and type(item) != int:
            correctData = False
            print("Incorrect datatypes. please use lists containing strings or integers. ")
            break
        
        elif type(item) == int and item < 0:
            correctData = False
            print("Your list contains the number: " + str(item))
            print("The list cannot contain non-negative numbers. Please review data.")
            break
            
    ####################################################
    ## Moving on to solution if correctData is True.   #
    ####################################################
        
    if correctData == True:
        for item in providedList: # Checking each value in list
            if type(item) == int: # Compares item to see if it is type integer.
                newList.append(item) # If This returns True, append this element to newList.
            else:
                continue
        print(newList) #Display list

##Main function to call function
def main():
    filterList([12,45,67,"The","our","Light"])


## Run code
main()
