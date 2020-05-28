# Module 7
#   Programming Assignment 10
#     Prob-3.py

# Robert Ballenger

def main():
    sum = 0
    
    '''
    x = float(input("Enter a number (Or a negitive number to exit)\n"))
    while x >= 0:
        sum = sum + x
        x = float(input("Enter a number (Or a negitive number to exit)\n"))
    print("-------------------------------------")
    print("The sum of your numbers is", sum)
    '''

    # Since true is always true, this while loop will loop until the break point occurs so...
    while True:
        
        # Starting again creating x for the number given variable. Same as above.
        x = float(input("Enter a number (Or a negitive number to exit) "))

        # Now we run an if statment to check if the number given is postive or negative.
        if x >= 0:
            # If postive it adds the number to the sum to create a new sum.
            sum = sum + x
            # Then the loop restarts since True is still True and no break has been hit.
        else:
            # If a negative number is given, it prints out the sum again but also breaks the loop.
            print("-------------------------------------")
            print("The sum of your numbers is", sum)
            break
main()    