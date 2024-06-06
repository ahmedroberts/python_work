# Ahmed O. Roberts
# Python 2023

from datetime import datetime
import json

boss = "Ahmed O. Roberts"
The9thRaikage = "Ahmed Omar Roberts"
jsonFileLoc = "c:/Users/aroberts/Code/P1HT/zqj/json/superhumans.json"
frmtFileLoc = "c:/Users/aroberts/Code/P1HT/zqj/json/superhuman.txt"
currentDateTime = datetime.now()
supersList = []
customSpacer = "\n********************************************\n"

print(customSpacer)
print(boss + ' is the boss today,', currentDateTime)
print('The 9th Raikage | ' + The9thRaikage)

#Opening a JSON File in Memory
myFile = open(jsonFileLoc)

# readingg my file into a storage location
myData = json.load(myFile)

# loop through my lines
print(customSpacer)
print("Started Reading JSON file with data called superhumans.\n")
for super in myData['superhumans']:
    print(super)
print(customSpacer)

# Close my file
myFile.close()

# parse through my lines
print(frmtFileLoc)
print(customSpacer)
print("Started Reading JSON file with data called superhumans.\n")
with open(frmtFileLoc) as jf:
    for opHuman in jf:
        supersDict = json.loads(opHuman)
        supersList.append(supersDict)

# We have collected the data. Now we can display some
print(customSpacer)
print("Printing each JSON Decoded Object from superhumans\n")

for opHuman in supersList:
    print('Code Name:', opHuman["codename"])
