import requests
import json
import os

# Path of file on my system: gettysburg = os.path.join('CIS_156', 'Ch_12', 'address.txt')
# Path of file if ran from same directory: gettysburg = "address.txt"
gettysburg = os.path.join("address.txt")

MY_API_KEY = 'qg+0oBakQjRBk7e7fBppSQ==94MKtUIGtIj3rlqh'

name = 'cheetah'
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)

# response = requests.get(api_url, headers={'X-Api-Key': MY_API_KEY})
# if response.status_code == requests.codes.ok:
#     print(response.text)
# else:
#     print("Error:", response.status_code, response.text)
    
def animal_info(animal):
  api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal)
  response = requests.get(api_url, headers={'X-Api-Key': MY_API_KEY})
  if response.status_code == requests.codes.ok:
      # print(response.text)
      animal_data = response.json()
  else:
      print("Error:", response.status_code, response.text)
  return animal_data
      
# animals = ['panther', 'octopus', 'sloth', 'bear']
# animal_info('octopus')

# for beast in animals:
#   animal_info(beast)

animal_data = animal_info('sloth') 
animal_data_path = os.path.join('API_practice', 'animal_data.json')
with open(animal_data_path, 'w') as outfile:
  json.dump(animal_data, outfile, ensure_ascii=False, indent=4)
  
print("\n\t-- All Done. --\n")