## Title: Week 4 Third Round Challenge
## Author: Shantel Williams
## Date: 9/26/2022
##
## Challenge: Create a function that takes a number as its only argument
## and returns True if it's less than or equal to zero, otherwise return False.
##
########################################################################################################################################

# Import libraries
import string

##Solution function
def numberCalculation(providedList): ##declaring function that takes an integer argument.
    if type(providedList) != int: ## return error if interger isn't given. 
        return "Invalid entry."
    elif providedList <= 0: ## 2 conditions for True or False. 
        return True
    elif providedList > 0:
        return False


## Creat main function
def main():
    result = numberCalculation("89")## Variable for results
    print(result) ## results


## Run code 
main()
