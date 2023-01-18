## Author:Shantel Williams
## Date: 1/9/2023
## FileName: Week 24 Python Challenge
## 
## Description: Create a dictionary called answer , that makes each first item in each list a key 
## and the second item a corresponding value. 
####################################################################################################################################

##Resolution Funtion
def newDictionary(providedList): ## takes the provided multidimenional list as argument. 
    newdict = {}  ## empty dictionary
    for list in providedList: ## loops through each list and grabs both items
        newdict.update({list[0]: list[1]})  ## update() adds the key and value if it doesn't already exist 
    return newdict

## Main
def main():
    person = [["name", "Bruce"], ["job", "Batman"], ["city", "Gotham"]]
    answer = newDictionary(person) ## using function to create answer dictionary.
    print(answer)

## Run it! 
main()