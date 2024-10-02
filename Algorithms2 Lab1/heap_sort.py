# def heap_setup(array, i):
#     while i > 0:
#         parent = (i - 1)//2
#         if array[i] <= array[parent]:
#             break
#         array[i], array[parent] = array[parent], array[i]
#         i = parent
from random import randint

def Bubble_Heap(array, i, heap_size):
    while True:
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        largest = i

        if left_child < heap_size and array[left_child] > array[largest]:
            largest = left_child

        if right_child < heap_size and array[right_child] > array[largest]:
            largest = right_child

        if largest == i:
            break

        array[i], array[largest] = array[largest], array[i]
        i = largest
    
    return

def heap_sort(array):
    n = len(array)

    #this steps through the list by -1 each time and stop when it reaches the end
    for i in range(n // 2 - 1, -1, -1):
        Bubble_Heap(array, i, n)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        Bubble_Heap(array, 0, i) 

if __name__ == "__main__":
    counter = 0
    random_list = []
    while counter < 10:
        choice = randint(1, 10)
        while choice in random_list:
            choice = randint(1, 10)
        random_list.append(choice)
        counter += 1
    
    print("Original List:", random_list)
    
    heap_sort(random_list)

    print("Sorted List:", random_list)
