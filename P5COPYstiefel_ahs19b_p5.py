import random
MENUCHOICE1 = 1
MENUCHOICE2 = 2
MENUCHOICE3 = 3
MENUCHOICE4 = 4
def main():
    fileSelected = getUserFileInput()
    print(fileSelected)

    userMenuChoice = getUserMenuChoice()
    print(userMenuChoice)

    if userMenuChoice == MENUCHOICE1:
        convertTocomplement(fileSelected)
    elif userMenuChoice == MENUCHOICE2:
        mutateStrand(fileSelected)
    elif userMenuChoice == MENUCHOICE3:
        findSubstrand(fileSelected)
        
        
        

def getUserFileInput():

    # file names
    fileName1 = 'dna1.txt'
    fileName2 = 'dna2.txt'
    fileName3 = 'dna3.txt'
    readOriginal = 'Original Sequence Read from File: '

    # Get file name user wants to open

    fileEntered = input('Please enter a file name: ')

    # Figure out which file the user would like to
    # enter. And also make sure the user enters a
    # valid file name

    if fileEntered == fileName1:
        # open a file named dna1.txt
        infile1 = open('dna1.txt', 'r')
        # read the files contents.
        file_contents1 = infile1.read()
        # print origanal sequence message
        print(f'{readOriginal} {file_contents1}')
        # if selected set fileSelected to this file
        fileSelected = file_contents1
        
    elif fileEntered == fileName2:
        # open a file named dna2.txt
        infile2 = open('dna2.txt', 'r')
        # read the files contents.
        file_contents2 = infile2.read()
        # print origanal sequence message 
        print(f'{readOriginal} {file_contents2}')
        # if selected set fileSelected to this file
        fileSelected = file_contents2
        
        
    elif fileEntered == fileName3:
        # open a file named dna3.txt
        infile3 = open('dna3.txt', 'r')
        # read the files contents.
        file_contents3 = infile3.read()
        # print origanal sequence message
        print(f'{readOriginal} {file_contents3}')
        # if selected set fileSelected to this file
        fileSelected = file_contents2
        
    else:
        fileEntered = input('Cannot open file. Enter a new file name: ')

    return fileSelected


def getUserMenuChoice():
    # promt the user to enter a choice 1-4
    userChoice = 0
    while (userChoice>4 or userChoice <1):
        print('''\nEnter a number 1-4
        1. Find the complement of the strand
        2. Mutate the DNA strand
        3. Find substrand within the strand
        4. Quit
        ''')

        # Get the choice that the user wants
        userChoice = int(input('Enter your choice: '))

        if userChoice == 1:
            userMenuChoice = MENUCHOICE1
        elif userChoice == 2:
            userMenuChoice = MENUCHOICE2
        elif userChoice == 3:
            userMenuChoice = MENUCHOICE3
        elif userChoice == 4:
            userMenuChoice = MENUCHOICE4
        else:
            print(' Invalid Selection\n')
            
    return userMenuChoice


def convertTocomplement(dnaSequence):
    strand = list(dnaSequence)
    #Gets the complement of DNA sequence
    comp = []
    for i in strand:
        if i == "T":
                comp.append("A")
        if i == "A":
            comp.append("T")
        if i == "G":
            comp.append("C")
        if i == "C":
            comp.append("G")
    print(comp)


def mutateStrand(dnaSequence):
    strand = list(dnaSequence)
    comp = []
    randomPosition = random.randint(1, 4)
    if randomPosition == 1:
        for i in strand:
            if i == "T":
                    comp.append("M")
            if i == "A":
                comp.append("A")
            if i == "G":
                comp.append("G")
            if i == "C":
                comp.append("C")
    if randomPosition == 2:
        for i in strand:
            if i == "T":
                    comp.append("T")
            if i == "A":
                comp.append("M")
            if i == "G":
                comp.append("G")
            if i == "C":
                comp.append("C")
    if randomPosition == 3:
        for i in strand:
            if i == "T":
                    comp.append("T")
            if i == "A":
                comp.append("A")
            if i == "G":
                comp.append("M")
            if i == "C":
                comp.append("C")
    if randomPosition == 4:
        for i in strand:
            if i == "T":
                    comp.append("T")
            if i == "A":
                comp.append("A")
            if i == "G":
                comp.append("G")
            if i == "C":
                comp.append("M")
    print(comp)

    
def findSubstrand(dnaSequence):
    
##    # This is how to get substring index
##    dnaSequence == sequenceFile
    substring = input('Please enter substring: ')
    # Get the substring user is searching for
    try:
        substring_index = dnaSequence.index(substring)
        print(substring_index)
    except ValueError:
        print ('Not a valid substring')
    









# Call the main function
if __name__ == "__main__":
    main()
    

##strand = list(file_contents1)
##print(f'{strand}')
##if userChoice == 1:
##
##    
### This is how to get substring index
##sequenceFile = 'GGTACGGATG'
##substring = input('Please enter substring: ')
### Get the substring user is searching for
##try:
##    substring_index = sequenceFile.index(substring)
##    print(substring_index)
##except ValueError:
##    print ('Not a valid substring')
##
##
###Gets the complement of DNA sequence
##comp = []
##for i in strand:
##    if i == "T":
##            comp.append("A")
##    if i == "A":
##        comp.append("T")
##    if i == "G":
##        comp.append("C")
##    if i == "C":
##        comp.append("G")
##print(comp)







    








