#Selection Sort

L = [5,8,2,9,7,3]

#go through the list n-1 times
for passNo in range (len(L)-1, -1, -1):
    #find the maximum number and it's position
    largest = max(L[:passNo+1])
    largestPos = L.index(largest)
    #make one to the "end" of the list
    temp = L[largestPos]
    L[largestPos] = L[passNo]
    L[passNo] = temp
    print(L)