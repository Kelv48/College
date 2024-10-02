##Kelvin Osagie 122318693


#Q1 p1
"""programming_languages = ('php','java','python','c++','c')

result = map(lambda x: x.upper(), programming_languages) 
print(tuple(result))

#p2

newlist = [x.upper() for x in programming_languages]
print(newlist)"""

#p3
"""programming_languages = ['php','java','python','c++','c']

newlist = []
for x in programming_languages:
    x = x.upper()
    newlist.append(x)
print(newlist)"""

#Q2
"""def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(starts_with_A, fruit)
print(list(map_object))

#newlist = [bool(x) for x in fruit if x[0] == "A"]
#print(list(newlist))

result = [item[0] =="A" for item in fruit]
print(result)"""

#Q3 a
zipWith = map(lambda n1, n2: n1 - n2, [7,8,9], [3,2,1])
#function has two list which it takes data from n1 and n2
#it takes the item at each index and performs n1 - n2 
#the output will be [4, 6, 8]

#Q3 b
"""n1 = [7,8,9]
n2 = [3,2,1]

newlist = []

def zipWith():
    i = 0
    for x in n1 and n2:
        x = n1[i]
        y = n2[i]
        n3 = x - y
        i += 1
        newlist.append(n3)
    return newlist

results = zipWith()
print(results)"""

#Q3 c 
"""summation = [n for n in range (17) if n > 10] 
print(list(summation))"""

"""newlist = []
def summation():
    for n in range(17):
        if n > 10:
            newlist.append(n)
    return newlist
newlist = summation()
print(newlist)"""

#Q4
"""retail = {"Tesco":["Cork","Dublin","Tralee","Ballymun"], "Aldi":["Cork","Tralee"], "Costco":["Kerry","Dingle","Cork"], "7Eleven":["Cork","Kerry","Dingle","Dublin"]}

def BiggestRetailChain():
    other_lengths = [len(item) for item in retail.values()] #makes of the length value of the list, eg4
    listMax = max(other_lengths)    #goes through list and gets highest value
    # value = 0
    # valueList = []
    storeList = []
    count = 0

    while count <= listMax:
        for item in other_lengths:
            if item == listMax:
                index = other_lengths.index(item)
                biggestRetail = list(retail)[index] #indexing the retail store
                if biggestRetail not in storeList :
                    storeList.append(biggestRetail) #appends largest retail to new list
                    other_lengths[index] = 0    #sets used value to 0 to avoid duplicates

        return storeList

results = BiggestRetailChain()
print(results)

def CommonTowns(d, rc1, rc2):
    rc1 = d[rc1]
    rc2 = d[rc2]
    newlist = []
    for item in rc1:
        if item in rc2:
            newlist.append(item)
    return newlist

res = CommonTowns(retail, "Tesco", "Aldi")
print(res)"""

#5
dict_properties  = {"Property1" : ["Drywall:1000", "Painting:1300", "Roof:5000", "Exterior:10000"],
                    "Property2" : ["Drywall:5000", "Painting:2000", "Roof:3567", "Exterior:2300"],
                    "Property3" : ["Drywall:10020", "Painting:1300", "Roof:235532", "Exterior:10000"], 
                    "Property4" : ["Drywall:1000", "Painting:235", "Roof:53000", "Exterior:4552"], 
                    "Property5" : ["Drywall:1000", "Painting:13400", "Roof:236", "Exterior:10000"], 
                    "Property6" : ["Drywall:1000", "Painting:1300", "Roof:5000", "Exterior:10000"], 
                    "Property7" : ["Drywall:10300", "Painting:2352", "Roof:57000", "Exterior:10000"], 
                    "Property8" : ["Drywall:1000", "Painting:235", "Roof:5000", "Exterior:10000"], 
                    "Property9" : ["Drywall:1000", "Painting:1300", "Roof:5000", "Exterior:10000"], 
                    "Property10" : ["Drywall:466", "Painting:23456", "Roof:5245", "Exterior:190000"]
                    }
 
 
 
'''cost per property'''
"""def cost_per_property(dictionary):
    #gets the keys, the list in my dictionary
    # i = keys
    for i in (dictionary):
        #item = each individual lists aka values
        items = dictionary[i]
        cost = 0
        #temporary list used for splitting the values
        l1 = []
        #lits used for the calculating the costs
        l2 = []
 
        for item in items:
            l1.append(item)
 
        #gets list inside a list, first part with the number
        for tempVal in l1 :
            tempVal = (tempVal.split(":"))
            #appends the numbers/costs per property
            l2.append(int(tempVal[1]))
 
        #adding up the costs but assigning it with a temp value (tempVal2)
        for tempVal2 in l2:
            cost += tempVal2
 
        print(i, ":", cost)
cost_per_property(dict_properties)
 
 
'''Cost per aspect'''
def cost_per_aspect(dictionary):
    drywallCost = []
    paintingCost = []
    roofCost = []
    exteriorCost = []
    for i in (dictionary):
        #item = each individual lists aka values
        items = dictionary[i]
 
        count = 0
        #temporary list used cost list
        l1 = []
        #lits used for the calculating the costs
        l2 = []
 
        #gets list inside a list, first part with the number
        for cost in items :
            cost = (cost.split(":"))
            #appends the numbers/costs per property
            l1.append(int(cost[1]))
 
        #separates the values
        drywallCost.append(l1[count])
        paintingCost.append(l1[count+1])
        roofCost.append(l1[count+2])
        exteriorCost.append(l1[count+3])
 
    drywallCost = sum(drywallCost)
    paintingCost = sum(paintingCost)
    roofCost = sum(roofCost)
    exteriorCost = sum(exteriorCost)
 
    return "Drywall:"+str(drywallCost), "Painting:"+str(paintingCost), "Roof:"+str(roofCost), "Exterior:"+str(exteriorCost)
 
print(cost_per_aspect(dict_properties))
 
 
'''The total cost of renovating all properties.'''
def total_properties_cost(dictionary):
    total_cost = 0
    #gets the keys, the list in my dictionary
    # i = keys
    for i in (dictionary):
        #item = each individual lists aka values
        items = dictionary[i]
        cost = 0
        #temporary list used for splitting the values
        l1 = []
        #lits used for the calculating the costs
        l2 = []
 
        for item in items:
            l1.append(item)
 
        #gets list inside a list, first part with the number
        for tempVal in l1 :
            tempVal = (tempVal.split(":"))
            #appends the numbers/costs per property
            l2.append(int(tempVal[1]))
 
        #adding up the costs but assigning it with a temp value (tempVal2)
        for tempVal2 in l2:
            cost += tempVal2
 
        total_cost += cost
    print("Total Cost:", total_cost)
total_properties_cost(dict_properties)
 

'''The property costing the most to renovate.  '''
def max_cost(dictionary):
    maxCost = 0
    propNumber = "nothing"
    #gets the keys, the list in my dictionary
    # i = keys
    for i in (dictionary):
        #item = each individual lists aka values
        items = dictionary[i]
        cost = 0
        #temporary list used for splitting the values
        l1 = []
        #lits used for the calculating the costs
        l2 = []

        for item in items:
            l1.append(item)

        #gets list inside a list, first part with the number
        for tempVal in l1 :
            tempVal = (tempVal.split(":"))
            #appends the numbers/costs per property
            l2.append(int(tempVal[1]))

        #adding up the costs but assigning it with a temp value (tempVal2)
        for tempVal2 in l2:
            cost += tempVal2

        if cost > maxCost:
            propNumber = propNumber.replace(propNumber, i)
            maxCost = cost

    print(propNumber, ":", maxCost)
max_cost(dict_properties)"""

#6
''' A reading the file into a dictionary '''


def load_data(filename):
    dic = {}
    i = 0
    list = []
    myFile = open(filename, "r")
    for data in myFile:
        data = myFile.readline()
        list.append(data)
        i += 1
        for x in list:
            x = data.strip("\n")
            x = data.strip(",")
            print(x)
            
        
        

res = load_data("occurences.txt")




















  



