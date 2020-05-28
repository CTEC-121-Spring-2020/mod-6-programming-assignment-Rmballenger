# Module 7
#   Programming Assignment 10
#     Prob-2.py

# Robert Ballenger

# I - 
# P -
# O -

def main():
    infile = open('Prob-2-Input.txt' ,'r')
    sum = 0.0
    for line in infile:
        sum = sum + float(line)
    print(sum)

def test():
    inFile = open('/mod-6-programming-assignment-Rmballenger/Prob-2/Prob-2-Input.txt', 'r')
    contents = inFile.read()
    print(contents)

test()