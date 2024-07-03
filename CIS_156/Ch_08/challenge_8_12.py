'''
Integer num_data is read from input, representing the number of remaining strings in the input. 
Use a for loop to read the remaining strings from input. Each string consists of a key string and a value string separated by a space. 
Add each key-value pair into the dictionary favorite_food.
'''
def code_breaker():
  print('\n################################################\n')

code_breaker() ################################################

favorite_food = {}
num_data = int(input())

''' Your code goes here '''
for i in range(num_data):
    tokens = input().split()
    favorite_food[tokens[0]] = tokens[1] 
''' end my code '''

print('Favorite food:')
print(favorite_food)

code_breaker() ################################################

'''
Read strings from input until 'stop' is read. 
For each string read, 
if the string is a key in dictionary favorite_food, 
delete the key from favorite_food.
'''

favorite_food = {'Ava': 'potato', 'Zoe': 'beans', 'Mel': 'corn'}

print('Original favorite food:')
print(favorite_food)

''' Your code goes here '''
inp = input()
while inp != 'stop':
    if (inp in favorite_food):
        del favorite_food[inp]
    inp = input()
''' end my code '''

print('Updated favorite food:')
print(favorite_food)

code_breaker() ################################################