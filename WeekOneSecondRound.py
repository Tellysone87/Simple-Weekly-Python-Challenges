## Title: Week 1 Second Round Challenge
## Author: Shantel Williams
## Date: 8/3/2022
##
## Challenge: Create a function that returns True when num1 is equal to num2;
## otherwise return False.
##
## Examples: 
## is_same_num(4, 8) ➞ False
##
## is_same_num(2, 2) ➞  True
##
## Solution: To complete this funtion. I decided to use 3 functions.
## I used two to collect the users numbers and one to actually answer the challenge.
##
########################################################################################################################################

## Import libraries
import string

## Create welcome message
def promptnumber1():
    welcome = "Welcome to the Number checker!"
    CenteredWelcome = welcome.center(20)
    print(CenteredWelcome)

## function to get number 1 from user 
    Num1 = input("Enter your first number: ")
    print("You entered " + Num1)
    print(Num1)
    return Num1

## function to get number 2 from user 
def promptnumber2():
    Num2 = input("Enter your second number: ")
    print("You entered " + Num2)
    print(Num2)
    return Num2

## Check for answer. This is the challenge funtion. Function takes two numbers and returns boolean value.
## I will get the numbers from each prompt user funtion. Then return the true or false response.

def is_same_num(NumA, NumB):
    return NumA == NumB

    
## Main function to call functions. I made variables to store each functions value.
##Then print the funtion with the answer.

def main():
    val1 = promptnumber1()
    val2 = promptnumber2()
    print(is_same_num(val1,val2))
   

## Lastly Run program
main()
