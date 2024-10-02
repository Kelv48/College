def load_data(filename):
    inFile = open(filename, "r")
    dict = {}

    #reads it in line by line including \n
    importedFile = inFile.readline()
    while importedFile != "":
        importedFile = importedFile.strip("\n")
        tempL = []
        #makes the imported file into a list
        importedFile = importedFile.split(',')
        for item in importedFile:
            #removes the empty spaces
            item = item.strip(" ")
            #marks the key 
            key = importedFile[0]
            #removes the spaces for the key in order for the validation to work
            key = key.strip(" ")
            if item != key:
                #appends value to a list
                tempL.append(int(item))
        #creating the dictionary of K:V pair
        dict[key] = tempL
        importedFile = inFile.readline()

    inFile.close()
    return dict
print(load_data('occurences.txt'))


def daily_cases(cumulative):
    dict = load_data(cumulative)
    new_dict = {}
    #key here is the ACTUAL key in the dictionary
    for key in dict:
        tempL = (dict[key])
        l1 = []
        for index in range(len(tempL)):
            if index == 0:
                l1.append(tempL[index])
            else: 
                tempVal = tempL[index] - tempL[index-1]
                l1.append(tempVal)
        new_dict[key] = l1 

    print(new_dict)

        

daily_cases('occurences.txt')
