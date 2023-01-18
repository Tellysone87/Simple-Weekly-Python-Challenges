## Author:Shantel Williams
## Date: 11/21/2022
## FileName: Week 21 Python Challenge
##
## Description: Write a function called number_compare. This function takes in two parameters (both numbers). 
## If the first is greater than the second, this function returns "First is greater".
## If the second number is greater than the first, the function returns "Second is greater" 
## Otherwise the function returns "Numbers are equal"
####################################################################################################################################

## import random to test function
import random
from winreg import SetValue

## Solution Function
def number_compare(numA,numB):
   if numA > numB:
       return numA
   elif numB > numA:
       return numB
   else:
       return str(numA) + " and " + str(numB) + " Numbers are equal"

##Declared  main.
def main():
    ## Using random values to test greater value.
    firstNum = random.randint(1,100)
    SecondNum = random.randint(1,100)
    results = number_compare(firstNum,SecondNum)
    print("Which number is larger " + str(firstNum) + " or " + str(SecondNum) + " ? " + str(results))

    ## A set value to test equal.
    setValues = number_compare(6,6)
    print(setValues)

## Run it!
main()