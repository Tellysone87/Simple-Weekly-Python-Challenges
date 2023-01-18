## Author:Shantel Williams
## Date: 1/17/2023
## FileName: Week 25 Python Challenge
## Create a function, yell, 
## which accepts a single string argument.
## It should return(not print) an uppercased version of the string with an exclamation point added at the end. 
####################################################################################################################################

## Solution function
def yell(strValue): #accepts a single string argument
    return strValue.upper() + "!" #return uppercased version of the string with an exclamation point added at the end.

# define a main
def main():
    test = "leave me alone"
    results = yell(test)
    print(results) 

# Run it!
main()



