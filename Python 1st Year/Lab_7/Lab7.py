#15/11/22
#lab 7

#Q1a.

'''inFile = open ("debanks.txt", "r")
lyrics = inFile.readline()
number = 1


while lyrics != "":
    print(number, lyrics)
    number += 1
    lyrics = inFile.readline()


inFile.close'''

#b
'''inFile = open ("debanks.txt", "r")
i = 0
number = 1


for lyrics in inFile:
    lyrics = inFile.read()
    lyrics = lyrics.strip("\n")
    lyrics_lines = lyrics.split("\n")
    for line in lyrics_lines:
        lines = lyrics_lines[i]
       
        i += 1
        print(number, lines)
        number += 1
        

inFile.close'''

#c
'''inFile = open ("debanks.txt", "r")
i = 0
number = 1

for lyrics in inFile:
    lyrics = inFile.readlines()
    for item in lyrics:
        lyrics_lines = lyrics[i]
        i += 1
        print(number, lyrics_lines)
        number += 1

inFile.close()'''

#d
'''inFile = open ("debanks.txt", "r")
i = 0
number = 1
for lyrics in inFile:
    lyrics = inFile.readlines()
    for x in lyrics:
       
        print(number, lyrics[i])
        i += 1
        number += 1'''

#2
'''inFile = open ("dna.txt", "r")
i = 0
number = 0

for dna in inFile:
    dna = inFile.read()
    dna = dna.strip("\n")
    dna = dna.split("\n")
    for data in dna:
        data = dna[i]
        print(number,": ", data, sep="")
        i += 1
        number += 1
        
inFile.close()'''

'''inFile = open("dna.txt", "r")
i = 0
number = 1


for para in inFile:
    file_contents = inFile.read()
    dna = file_contents.split("\n\n")
    for item in dna:
        dna_data = dna[i]
        i += 1
        print(number, dna_data)    
        number += 1'''

inFile = open("dna.txt", "r")
i = 0
number = 1


for contents in inFile:
    file_contents = inFile.read()
    dna_data = file_contents.split("\n\n")
    
for data in dna_data:
    dna = data.replace("\n", "")
    print(i ,":", dna)
    i += 1


    



   



inFile.close()
