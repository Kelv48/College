codon_map = {'AUG' : 'Methionine', 'UUU' : 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA' : 'Leucine', 'UUG' : 'Leucine', 'UCU' : 'Serine', 'UCC' : 'Serine', 'UCA' : 'Serine', 'UCG' : 'Serine', 'UAU' : 'Tyrosine', 'UAC' : 'Tyrosine', 'UGU' : 'Cysteine', 'UGC' : 'Cysteine', 'UGG' : 'Tryptophan', 'UAA' : 'stop', 'UAG' : 'stop', 'UGA' : 'stop' }


def proteins (RNA, codon_dictionary):
    i = 0
    var = ""
    list = []
    newlist = []
    for String in RNA:
        list.append(String)
        newlist.append(list[i : (i + 2)])
        i += 3
    print(newlist)
            
    


    
    #generate a list of the codons making up the RNA string. 
    #Hint: think of string slicing and how you might do that in a for loop
    
    
    #Take each codon from the codon list and use this to get the corresponding protein from the dictionary. 
    #print the list of codons to screen as well as the proteins to the screen. 
    #It should terminate if a stop codon is encountered    
    
   
RNAString = "AUGUUUUCU"
proteins(RNAString, codon_map)