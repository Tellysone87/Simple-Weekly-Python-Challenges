## Author:Shantel Williams
## Date: 1/23/2023
## FileName: Week 26 Python Challenge
## Write a function named only_ints that takes two parameters. 
## Your function should return True if both parameters are integers, and False otherwise.
## For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False. 
####################################################################################################################################

# Solution Function
def only_ints(entry1,entry2):
  if type(entry1)  == int and type(entry2) == int:
      return True
  else:
      return False

# main function
def main():
    results = only_ints(1,2)
    results2 = only_ints(1,"No")
    results3 = only_ints("short","bee")
    print(results)
    print(results2)
    print(results3)

#run it 
main()