retail = {"Tesco":["Cork","Dublin","Tralee","Ballymun","Dingle"], "Aldi":["Cork","Tralee"], "Costco":["Kerry","Dingle","Cork"], "7Eleven":["Cork","Kerry","Dingle","Dublin","Cashel"]}

def BiggestRetailChain(d):
    chain_towns = {}                        #Sets up an empty dict for storing data relating to the stores namely how many towns they serve and their name
    for chain, towns in d.items():          #Gets the chain name and the towns it serves from the dictionary
        chain_towns[chain] = len(towns)     #Inserts the data into the empty dictionary
    sorted_chains = sorted(chain_towns.items(), key=lambda x: x[1], reverse=True)       #extracts the number of appearances from the value pairs
    largest_chains = [chain[0] for chain in sorted_chains if chain[1] == sorted_chains[0][1]] #gets the highest value/s and returns the chain name attached
    return largest_chains
  

result = BiggestRetailChain(retail)
print(result)

