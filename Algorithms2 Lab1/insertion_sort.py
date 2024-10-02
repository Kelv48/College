from random import randint

def insertionSort(arr):
    n = len(arr)  
      
    if n <= 1:
        return  
 
    for i in range(1, n):  
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]:  
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = key  
counter = 0
random_list = []
while counter < 10:
    choice = randint(1, 100)
    random_list.append(choice)
    counter += 1
insertionSort(random_list)
print(random_list)