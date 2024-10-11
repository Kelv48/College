#31/01/23


#I dont fully understand the dict comprehension so i commented it out
'''def generateEircodeAreas (filename):
    eircodeAreas = {}
    with open(filename) as f:
        eircodeAreas = {str(k): v for line in f for (k, v) in [line.strip().split(None, 1)]}
    return eircodeAreas'''

def generateEircodeAreas (filename):
    inFile = open(filename, 'r')


    eircodeAreas = inFile.readline()
    eircodeDictionary = {}
    tempList = []

    while eircodeAreas != "" :
        eircodeAreas = eircodeAreas.strip("\n")
        tempList.append(eircodeAreas)
        eircodeAreas = inFile.readline()
    for item in tempList :
        item = item.split(" ")
        eircodeDictionary[item[0]] = item[1]
    inFile.close()
    return eircodeDictionary


def getTownLand(eircode):
    townland = eircodeAreas[eircode]
    return townland

def checkLegitEirCode(eircode):
    firstchar = eircode[0]
    if eircode in eircodeAreas:
        if firstchar.isalpha():
            for char in range(1, 8):
                eircode.isnumeric()
                legitimate = True
            return legitimate
    else:
        legitimate = False 
        return legitimate
             

eircodeAreas = generateEircodeAreas("eircodes.txt")
userEircode = input("Please enter your eircode ")

legit = checkLegitEirCode(userEircode)
if legit:
    area = getTownLand(userEircode)
    print("You live in", area)
else:
    print("There has been an error verifying your eircode please try again")


