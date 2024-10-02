L = [5,8,2,9,7,3]

#go through the list n-1 times
for passNum in range(len(L)-1):
    #need to look at n-1 pairs for every pass/cycle through the list
    for pairNum in range(len(L)-1):
        #if a number is greater than the number after the swap
        if L[pairNum] > L[pairNum + 1]:
            temp = L[pairNum]
            L[pairNum] = L[pairNum + 1]
            L[pairNum + 1] = temp
    print(L)
#if not move to the number and repeat

#print out the state of the list after every pass