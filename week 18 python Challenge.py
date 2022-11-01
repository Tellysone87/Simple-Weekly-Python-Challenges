## Author:Shantel Williams
## Date: 10/31/2022
## FileName: Week 18 Python Challenge
## Description: ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
## but exactly 4 digits or exactly 6 digits. Your task is to create a function that
## takes a string and returns True if the PIN is valid and False if it's not. 
####################################################################################################

####################################################################################################
## Create member class that takes pin numbers.
## This will allow us to reuse the code for each transaction.
## I chose this route because I plan on taking this challenge and adding more. 
####################################################################################################
class member():
    def __init__(self,pin,name):
        self.pin = pin
        self.name = name
        
#################################################################################################
## Solution Funtion that takes the pin that is converted to string
## and returns True of False. Cannot contain anything but exactly 4 digits or exactly 6 digits.
#################################################################################################
    def verifyPin(self): ## checks member for correct pin data length

        givingPin = self.pin

        if givingPin.isdigit(): ## Conditional. The pin should consist of digits. 
            stringMemberPin = str(givingPin) ## conversion to string. The function to accept strings.
            if len(stringMemberPin) != 4 and len(stringMemberPin) != 6: ## If both conditions are true
                return False ## Pin is not correct length
            else:
                return True
        else:
            return False
        
## Main
def main():
    name = input("Please enter your name:\n") ## Gets member name. 
    memberPin = input("Hello " + name + ". Please enter your pin:\n") ## Asks member for pin.

    accountAccess = member(memberPin,name) ##Created a member object
    Check = accountAccess.verifyPin() ## function called and assigned to variable
    print(Check) ## Prints boolean value
    
## Run it!    
main()
