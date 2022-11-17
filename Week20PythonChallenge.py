## Author:Shantel Williams
## Date: 11/14/2022
## FileName: Week 20 Python Challenge
## Description: 1. Create a function that takes a number num and returns its length. I decided to play around with forms. 
##
####################################################################################################################################

## Libraries
from ast import Lambda
from distutils.log import warn
import sys
from distutils.cmd import Command
from tkinter import *
from tkinter.tix import COLUMN
from tkinter import messagebox

root = Tk() ##Tkinter objct
root.title('Number Counter')
root.geometry("500x300") ## Set Size

##################################################### solution Function ################################################3
def getNumLength(numProvided):
   Nlength = Label(root,text=len(numProvided)) ## Label to display answer on form. I used the len() function to resolve this challenge. 
   Nlength.grid(row = 2,column= 3,sticky = "w") ##Placement on grid

def getNum():
    num = number_entry.get()
    if num.isdigit():
       getNumLength(num)
    else:
        messagebox.showinfo("Information","Please enter a Valid number.") ## Reminds user to enter numbers only
        number_entry.delete("0", END)


## Function to clear user text field ##
def deleteText():
    number_entry.delete("0", END)

## Label for heading text
Label(root, text = "Number Length Counter", 
      font="ar 15 bold").grid(row = 0, column=2,pady= 10, sticky = "w")

## Labels for info fields
userNum = Label(root,text = "Enter a Number: ")
lengthOfNum = Label(root,text = "Length:")

## Setting grid locations to display the labels
userNum.grid(row=1,column=1,pady= 5)
lengthOfNum.grid(row=1,column=3,pady= 5,sticky = "w")

##Setting variables to collect data enter in fields
UserNumber = IntVar

## Creating entry fields for user
number_entry = Entry(root, textvariable= UserNumber)

##Setting entry field loctions
number_entry.grid(row=1,column=2, pady= 5)

## Submit button
Button(text = "Submit",height = 1,
       width = 10,command=getNum).grid(row = 4, column=2, pady= 5)
Button(text = "Clear",height = 1,
       width = 10,command=deleteText).grid(row = 5, column=2, pady= 5)

root.mainloop()

##### Solution Function ####
#def numberLength(num):
#    return len(num)

### prompts user for input and returns the number if it passes conditions. 
#def userInput():
#    running = 0
#    stopMessage = "Enter STOP to end the program."

#    while running != 1:
#        print(stopMessage)
#        givingNum = input("Please enter a number: ")

#        if(givingNum != "STOP"):
#            if (givingNum.isdigit()):
#                return givingNum
#            else:
#                print("Please enter numbers only or enter STOP to exit.")

#        elif(givingNum == "STOP"):
#            running = 1
#            sys.exit(0)

### Main Function
#def main():
#    InputNum = userInput()
#    nlength = numberLength(InputNum)
#    print(nlength)
   
### Run it !
#main()