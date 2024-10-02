from time import perf_counter

size = int(input("Please enter a number "))



def grow_by_append(size):
    start_time_append = perf_counter()
    append_list = []
    i = 0
    while i != size:
        append_list.append(i)
        i += 1
    end_time_append = perf_counter()
    time_to_append = end_time_append - start_time_append
    print("Runtime to append", size ,"integers" ,time_to_append, "seconds")

def grow_by_insert0(size):
    start_time_insert = perf_counter()
    insert_list = []
    i = 0
    while i != size:
        insert_list.insert(0, i)
        i += 1
    end_time_insert = perf_counter()
    time_to_insert = end_time_insert - start_time_insert
    print("Runtime to insert", size ,"integers" ,time_to_insert, "seconds")





grow_by_append(size)
grow_by_insert0(size)
