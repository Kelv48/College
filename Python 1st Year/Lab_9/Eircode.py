#31/01/23

eircodeAreas = {'A63': 'Greystones', 'A98':'Bray', 'P17':'Kinsale', 'A86':'Dunboyne', 'W23':'Cellbridge', 
'F45':'Castlerea', 'F35':'Ballyhaunis', 'H14':'Belturbet', 'N39':'Longford', 'F56':'Ballymote'}

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
             


userEircode = input("Please enter your eircode ")

legit = checkLegitEirCode(userEircode)
if legit:
    area = getTownLand(userEircode)
    print("You live in ", area)
else:
    print("There has been an error verifying your eircode please try again")
