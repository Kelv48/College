#Binary search 
L = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
itemToSearchFor = 54

startPos = 0
endPos = len(L) - 1

#find the midpoint (position)
#get item at that position
#check if its equal to the item you're searching for
#if it is print item

midpoint = (len(L)-1) // 2


found = False

while found == False:
    item = L[midpoint]
    if itemToSearchFor == item:
        found = True
        print (item)
    else:
        if itemToSearchFor > item:
            startPos = midpoint + 1
        else:
            endPos = midpoint 
        midpoint = (startPos + endPos) // 2 