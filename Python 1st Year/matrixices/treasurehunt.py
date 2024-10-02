clues = [[34, 21, 32, 41, 25], [14, 42, 43, 14, 31], [54, 45, 52, 42, 23], [33, 15,51, 31, 35], [21, 52, 33, 13]]
 
def checkTreasure (clue, row, col):
    coords = int(str(row) + str(col))
    if clue == coords:
        found = True
    else:
        found = False
        print (clue)
    return found
    
    
clue = clues[0][0]  #34
row = 1             #1
col = 1             #1


found = checkTreasure(clue, row, col)

#While its not found
while found == False:       #while not found is another option
    #get new coordinates and get the clue at the new coordinates   
    clue = str(clue)
    row = clue[0]
    col = clue[1]
    clue = clues[int(row)-1][int(col)-1]         #Minus 1 in order to get the co-ordinates of the new clue
    clue = int(clue)

    found = checkTreasure(clue, row, col)  #Check again is the treasure found
print ("We found the treasure!")