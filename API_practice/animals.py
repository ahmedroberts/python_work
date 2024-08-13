import requests

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
      print(response.text)
  else:
      print("Error:", response.status_code, response.text)
      
animals = ['panther', 'octopus', 'sloth', 'bear']
# animal_info('octopus')

for an in animals:
  animal_info(an)