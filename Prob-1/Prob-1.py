# Module 7
#   Programming Assignment 10
#     Prob-1.py

# Robert Ballenger

# I - The numbers given by the user
# P - Keep a running sum of the numbers, break when negative number given
# O - The sum of the numbers.


def main():
    # Start with a variable called sum with the value of 0 that will be added to.
    sum = 0

    # Use the input command to get numbers from the user. Assign them as float so decimals wont mess things up.
    x = float(input("Enter a number (Or a negitive number to exit)\n"))

    # Using a while loop, we create a break point. X >= 0, so any negative number will stop the loop.
    while x >= 0:
        
        # Within the loop, we run a simple math accumulator that adds the value given by previous value, then asks the question again for a new x value.
        sum = sum + x
        x = float(input("Enter a number (Or a negitive number to exit)\n"))

    # Once the loop is broken, I create 2 print statements, one for looks and the other is a string with the finalized sum variable.
    print("-------------------------------------")
    print("The sum of your numbers is", sum)

main()