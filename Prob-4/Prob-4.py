# Module 7
#   Programming Assignment 10
#     Prob-4.py

# Robert Ballenger

def openFile():

    
    inFile = open('CTEC121/Module_6/Module_6_Programming_Assignment/mod-6-programming-assignment-Rmballenger/Prob-4/balances.txt', 'r')
    originalBalances = inFile.read().splitlines()
    inFile.close

    calculateNewBalance(originalBalances)

def calculateNewBalance(originalBalances):

    interestRate = float(input("What is the interest rate?  "))
    

    for i in originalBalances:
        newBalance = (interestRate * i) + i
    
    saveFile(newBalance)

def saveFile(newBalance):
    inFile = open('CTEC121/Module_6/Module_6_Programming_Assignment/mod-6-programming-assignment-Rmballenger/Prob-4/balances.txt', 'w')

    inFile.write(newBalance)

    inFile.close


openFile()