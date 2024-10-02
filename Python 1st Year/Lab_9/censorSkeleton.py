MASK = "*"

def generate_banned_words():
    #read banned words in from file bannedWords and return a list
    inFile = open("bannedWords.txt", "r")

    #of banned words
    
    #THIS IS WHERE YOU START (STEP 1)
    bannedWords = []
    temp = inFile.readline()
    while temp !="":
        temp = temp.strip("\n")
        bannedWords.append(temp)
        temp = inFile.readline()
    print(bannedWords)
    return bannedWords

def bleeped(word):
    # Return a cleaned version of parameter 'word' with
    # any black-listed word replaced by asterisks. Ignore any
    # non-letters at the beginning or end of 'word'.
    
    return word

def censor_line(line):
    # Return censored version of the text in string parameter
    # 'line' while preserving word breaks and punctuation. 
    
    #split the lines into words and return a clean version of the word by invoking the bleeped function

    return " ".join(words)

def censor_file(filename):
    # Generate a trandformed version of the named text file containing
    # a censored version of the text.
    
    #THIS IS WHERE YOU COMPLETE STEP 2
    #This will invoke the function censor_line
     print

bannedWords = generate_banned_words()   
censor_file("someText.txt")
