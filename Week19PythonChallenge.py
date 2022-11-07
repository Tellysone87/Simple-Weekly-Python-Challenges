## Author:Shantel Williams
## Date: 11/7/2022
## FileName: Week 19 Python Challenge
## Description: Given a list of client emails,
## create a function that takes in the list as an argument
## and returns a new list with only the domain of each email.
####################################################################################################

## Library regEx - As suggested in Challenge
import re


## Solution Function takes a list for the argument
def get_domains(clientList):

    ## Splitting the emails of the giving list. They are split at the @ symbol.
    ## Thus creating a multidimensional list
    splitEmailList = [re.split("@",email) for email in clientList]

    ##List to grab the last element of nested list.
    newList =[splitItems[1]for splitItems in splitEmailList] 
    return newList
    
## Main function
def main():
    clients = ['brucewayne@gotham.com', 'homer_simpson@springfieldnuclear.com',
               'hank_hill@arlenpropane.com', 'petergriffin@pawtucketbrewery.com'] ## Provided list

    domainList = get_domains(clients) ## Variable calling function
    print(domainList)

## Run it!
main()
