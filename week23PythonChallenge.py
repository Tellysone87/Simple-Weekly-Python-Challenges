## Author:Shantel Williams
## Date: 12/12/2022
## FileName: Week 23 Python Challenge
## Define a function contains_blue() that accepts any number of arguments. 
## It should return True if any of the arguments are "blue" (all lowercase). 
## Otherwise, it should return False .
####################################################################################################################################

## Solution function
def contains_blue(*args):  # args is used to pass a number of arguments to the function
    for item in args:  # Checking each individual argument for "blue"
        if item == "blue":
            return True
    return False # Default False unless "blue" is found

## Def main Function
def main():
    # To speed up my process, I Created a list to run each example function call. 
    exampleList = [
    contains_blue(25, "blue") ,
    contains_blue("green", False, 37, "purple", "hello world"),
    contains_blue("blue") ,
    contains_blue("a", 99, "blah blah blah", 1, True, False, "blue"),
    contains_blue(1,2,3)]  

    for example in exampleList:
        print(example)
## Run it! 
main()