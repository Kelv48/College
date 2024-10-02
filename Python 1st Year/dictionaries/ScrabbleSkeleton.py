#Part 1
scrabbleDictionary = {"A": 1, "B": 3, "C": 3, "D": 2, "E":1, "F":4, "G": 2, "H":4, "I": 1, "J": 8, "K":5
, "L":1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z":10}

def calculateScore (word):
    score = 0

    for letter in word:
        if letter.isalpha():
            letter = letter.upper()
            score += scrabbleDictionary [letter]
        else:
            print("Not a valid character")
            exit()

    return score


'''w = input("Enter a word: ")
while w != "":
    final_score = calculateScore (w)
    print(final_score)
    w = input("Enter a word: ")'''


inFile = open("userWords.txt", "r")
i = 0
records = inFile.readlines()
for record in records:
    record = record.strip("\n")
    record = record.split(",")
    player_name = record[0]
    player_words = record[1:]

    for words in player_words:
        



inFile.close()