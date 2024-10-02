class calculate():
    def __init__(self):
        num_list = []
        i = 0
        for n in range(5):
            i += 1
            num = int(input("Please enter number %i " %(i)))
            num_list.append(num)
        print("The sum of the numbers is" , sum(num_list))
        average = sum(num_list) / len(num_list)
        print("The average of the numbers is" , average)
        

calculate()