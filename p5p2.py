import random
# file names
fileName1 = 'dna1.txt'
readOriginal = 'Original Sequence Read from File: '

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

strand = list(file_contents1)
strand1copy = strand
strand1copy = [] + strand    #creates copy of strand
print(f'{strand}')

index = 0          # This loop prints the list


##listLength = len(strand)
##while index < listLength:
##    print (strand[index])
##    index += 1


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


# gets 5 random simulated simple mutations in the DNA sequence
comp = []
randomPosition = random.randint(1, 4)
if randomPosition == 1:
    for i in strand:
        if i == "T":
                comp.append("M")
        if i == "A":
            comp.append("T")
        if i == "G":
            comp.append("C")
        if i == "C":
            comp.append("G")
if randomPosition == 2:
    for i in strand:
        if i == "T":
                comp.append("T")
        if i == "A":
            comp.append("M")
        if i == "G":
            comp.append("C")
        if i == "C":
            comp.append("G")
if randomPosition == 3:
    for i in strand:
        if i == "T":
                comp.append("T")
        if i == "A":
            comp.append("A")
        if i == "G":
            comp.append("M")
        if i == "C":
            comp.append("G")
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
    

##comp = []
##randomPositon = random.randint(1, 5)
##if randomPositon == 1:
##    for i in strand:
##        if i == "T":
##            comp.append("M")
##        
##if randomPositon == 2:
##    for i in strand:
##        if i == "A":
##            comp.append("M")
##        
##if randomPositon == 3:
##    for i in strand:
##        if i == "G":
##            comp.append("M")
##        
##if randomPositon == 4:
##    for i in strand:
##        if i == "C":
##            comp.append("M")
##print(comp)

    


##
##
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
##
##
##sequenceFile = ['GGTACGGATG']
###Get the substring user is searching for
##substring = input('Please enter substring: ')
### Get the substring user is searching for
##substring_index = strand.index(substring)
##print(substring_index)
##    
##except ValueError:
##    substring = input('Please enter substring: ')

    
    


