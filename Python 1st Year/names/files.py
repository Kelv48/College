#Step 1: Create the connection to the file
inFile = open ("names.txt", "r")

#Step 2: Read from your text file
#1 file iterate (Python specific)

# Type 1: File iterator
for name in inFile:
    name = name.strip("\n")         #or
    name = name.strip()
    print(name)        #Used in loop but returns with \n attachted

# Type 2: Read method - Gets the entire data file as a string
#names = inFile.read()

#Type 3: Readline method - gets one line at a time including \n
#name = inFile.readline()

#Type 4: Readlines method - gets all the lines as a list of strings include the \n
#names = inFile.readlines()

#Step 3: Close the connection i.e. delete the file object    
inFile.close()