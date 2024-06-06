import requests
import json

url2 = "https://cars-by-api-ninjas.p.rapidapi.com/v1/cars"

querystring2 = {"model":"corolla"}
querystring3 = {"model":"camry"}

headers2 = {
	"X-RapidAPI-Key": "6240c50c49mshbf180b1f6764593p1e4fd2jsn2b6f54be56dd",
	"X-RapidAPI-Host": "cars-by-api-ninjas.p.rapidapi.com"
}

response2 = requests.get(url2, headers=headers2, params=querystring3)

print(response2.json())

# Also Let's Build!!      ------------------------------------------------------------------
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("Hello 9th Raikage, Age:", y["age"])