# Ahmed O. Roberts
# Python 2023
# Ref: 
# https://www.youtube.com/watch?v=9N6a-VLBa2I&t=406 | Corey Schafer

from datetime import datetime
import json

boss = "Ahmed O. Roberts"
The9thRaikage = "Ahmed Omar Roberts"
jsonFileLoc = "c:/Users/aroberts/Code/P1HT/zqj/json/superhumans.json"
currentDateTime = datetime.now()
supersList = []
customSpacer = "\n********************************************\n"

print(customSpacer)
print(boss + ' is the boss today,', currentDateTime)
print('The 9th Raikage | ' + The9thRaikage)
print(customSpacer)


''' JavaScript Object Notation '''

# a python string that just happens to be valid JSON
people_string = '''
{
  "superhumans": [
    {
      "codename": "Blue Marvel",
      "firstName": "Adam",
      "lastName": "Brashear",
      "universe": "Marvel",
      "brotherhood" : true
    },
    {
      "codename": "Spawn",
      "firstName": "Albert",
      "lastName": "Simmons",
      "universe": "Image",
      "brotherhood" : false
    },
    {
      "codename": "Storm",
      "firstName": "Oro",
      "lastName": "Monroe",
      "universe": "Marvel",
      "gender": "female",
      "brotherhood" : false
    },
    {
      "codename": "Black Panther",
      "firstName": "T'Challa",
      "lastName": null,
      "ancestory": "Son of T'Chaka",
      "universe": "Marvel",
      "brotherhood" : true
    }
  ]
}
'''

# load this into a python object from a string
myData =  json.loads(people_string)

# so i worte the data as a key-value pair which makes it a dictked
print('What is myData:',type(myData))
print('What is myData | superhumans:',type(myData['superhumans']))

print(customSpacer)

print('myData\n',myData)

print(customSpacer)

# since superHumans is a list we can access each element
for opHuman in myData['superhumans']:
    print(opHuman['codename'])

print(customSpacer)

# Delete python key, values from Python Dictionary
for humanoid in myData['superhumans']:
    del humanoid['universe']
    del humanoid['brotherhood']

# Dump Python objects into JSON String
new_json_string = json.dumps(myData, indent=2, sort_keys=True)

print(new_json_string)
