## Arthor : Shantel Williams
## Date : 3/29/2023
## Summary : Create a function that creates a box based on dimension n.
##
#######################################################################################################3

def make_box(n):
    side = []
    down = []
    i = 0
    j = 0
    
    # Sets the length of box
    for i in range(n):
        side.append('#')
    #sets the row height
    for j in range(n):
        down.append(side)

    for row in down:
        print(row)         

def main():
    make_box(6)

main()