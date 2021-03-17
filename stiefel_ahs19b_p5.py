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
    
elif fileEntered == fileName2:
    # open a file named dna2.txt
    infile2 = open('dna2.txt', 'r')
    # read the files contents.
    file_contents2 = infile2.read()
    # print origanal sequence message 
    print(f'{readOriginal} {file_contents2}')
    
elif fileEntered == fileName3:
    # open a file named dna3.txt
    infile3 = open('dna3.txt', 'r')
    # read the files contents.
    file_contents3 = infile3.read()
    # print origanal sequence message
    print(f'{readOriginal} {file_contents3}')
    
else:
    fileEntered = input('Cannot open file. Enter a new file name: ')

# promt the user to enter a choice 1-4
print('''\nEnter a number 1-4
1. Find the complement of the strand
2. Mutate the DNA strand
3. Find substrand within the strand
4. Quit
''')

# Get the choice that the user wants
userChoice = input('Enter your choice: ')

strand = list(file_contents1)
print(f'{strand}')
if userChoice == 1:

    
# This is how to get substring index
sequenceFile = 'GGTACGGATG'
substring = input('Please enter substring: ')
# Get the substring user is searching for
try:
    substring_index = sequenceFile.index(substring)
    print(substring_index)
except ValueError:
    print ('Not a valid substring')


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







    








