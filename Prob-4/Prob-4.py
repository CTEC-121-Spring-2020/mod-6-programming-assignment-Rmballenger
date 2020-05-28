# Module 7
#   Programming Assignment 10
#     Prob-4.py

# Robert Ballenger

# I - A file is given that the program opens and reads. Also gets an interest rate from user.
# P - Program takes the numbers in the file, multiplies them by the interest rate and then adds the original value to create a new value.
# O - A list of new values is written to the program by overwriting it.

# To start I use 3 functions in this program.
# The first function is set to open the file and pull the text from the file, save it as a list, and close the file.
def openFile():
    
    # Opening the file with the 'r' for read. Giving it the name inFile.
    inFile = open('balances.txt', 'r')
    # Creating a new variable called originalBalances and using inFile read and splitlines to create a list with each value.
    originalBalances = inFile.read().splitlines()
    # Closeing the file.
    inFile.close
    # Calling a new function and sending the originalBalances variable to it.
    calculateNewBalance(originalBalances)

# This second variable does all the calculations. It takes the list of 6 values, removes them and turns them into floats, does the math formula and puts it all back in a  list with a name of newBalance.
def calculateNewBalance(originalBalances):

    # Here we get the interest rate from the user, and save it as a float named interestRate.
    interestRate = float(input("What is the interest rate?  "))
    
    # Here's where things get sloppy. First I need to remove all the values from the list and convert them to floats.
    var1, var2, var3, var4, var5, var6 = [originalBalances[i] for i in (0, 1, 2, 3, 4, 5)]
    convertedVar1 = float(var1)
    convertedVar2 = float(var2)
    convertedVar3 = float(var3)
    convertedVar4 = float(var4)
    convertedVar5 = float(var5)
    convertedVar6 = float(var6)
    
    # Then I take the convertedVars and do the maths to get a new variable with interest applied.
    newVar1 = round(((interestRate * convertedVar1) + convertedVar1), 2)
    newVar2 = round(((interestRate * convertedVar2) + convertedVar2), 2)
    newVar3 = round(((interestRate * convertedVar3) + convertedVar3), 2)
    newVar4 = round(((interestRate * convertedVar4) + convertedVar4), 2)
    newVar5 = round(((interestRate * convertedVar5) + convertedVar5), 2)
    newVar6 = round(((interestRate * convertedVar6) + convertedVar6), 2)
    
    # Last I add the values to a new list with the name newBalance.
    newBalance = []
    newBalance.append(newVar1)
    newBalance.append(newVar2)
    newBalance.append(newVar3)
    newBalance.append(newVar4)
    newBalance.append(newVar5)
    newBalance.append(newVar6)
    
    # Now we call the final function and send the newBalance list to it.
    saveFile(newBalance)

# Final function where the file will be written to and saved.
def saveFile(newBalance):
    # Honestly I'm not 100% sure how all this code here works. Google helped me find it. But I'll do my best to explain it how I see it.
    # here it opens the file set to write and saves it as filehandle (I think)
    with open('balances.txt', 'w') as filehandle:
        # Next a for loop that writes each value of a line of newBalance into the page. Again, this is really something i'm not sure 'how' it works...but it works. ¯\_(ツ)_/¯
        for listitem in newBalance:
            filehandle.write('%s\n' % listitem)

# Last we call the first function to start the process.
openFile()