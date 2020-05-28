# Module 7
#   Programming Assignment 10
#     Prob-2.py

# Robert Ballenger

# I - A file with a list of numbers
# P - Takes the numbers from the file and puts them all on their own line then adds them up
# O - Returns a list of the numbers and a sum.

def main():
    # To start, we open the file, and set it to 'r' so it reads rather than writing.
    inFile = open('Prob-2-Input.txt', 'r')

    # Next we set up a variable called sum and set it to 0.0
    sum = 0.0
    
    # Now we start a for loop that checks for each line of the file.
    for line in inFile:
        # These lines get rid of the space at the end of each line (rstrip) and splitting each line into a list (split)
        line = line.rstrip("")
        line = line.split()

        # Now here we create a new loop within the previous for loop that checks each item in the list and prints it as 'value' while also adding it as a float to the previous number creating a large sum.
        for value in line:
            print(value)
            sum = sum + float(value)

    # Last we have some decoration and a final print command that prints out the total sum.
    print("~~~~~~")
    print(sum)


main()
