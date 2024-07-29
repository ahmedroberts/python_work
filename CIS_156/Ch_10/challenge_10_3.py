'''
Integers total_avocados and avocados_requested are read from input, representing the number of avocados 
available and the number of avocados a customer wants to buy. In the try block:

Raise a ValueError exception with the message 'Number of avocados available must be positive' 
if total_avocados is less than or equal to 0.
Raise a ValueError exception with the message 'Number of avocados requested must be within range' 
if avocados_requested is less than 0 or is greater than total_avocados.
'''

try:
    total_avocados = int(input())  
    avocados_requested = int(input())  

    # Your code goes here
    if total_avocados <= 0:
      raise ValueError('')
    if (avocados_requested < 0) or (avocados_requested > total_avocados):
      raise ValueError('')

    avocados_remaining = total_avocados - avocados_requested

    print(f'Avocados remaining: {avocados_remaining}')

except ValueError as excpt:
    print(f'Error: {excpt}')
    
try:
    offices_per_floor = int(input())  
    num_floors = int(input())  

    # Your code goes here
    if offices_per_floor < 0:
        raise ValueError('Number of offices per floor must be positive')
    if num_floors <= 0:
        raise ValueError('Number of floors in the building must be positive')

    total_offices = offices_per_floor * num_floors

    print(f'Number of offices in the building: {total_offices}')

except ValueError as excpt:
    print(f'Error: {excpt}')
    
print('\n-------------------------------------------------\n')

color_tuple = ('pink', 'denim', 'salmon')

try:
    tuple_index = int(input())

    if (tuple_index < 0) or (tuple_index >= len(color_tuple)):
        raise IndexError(f'Valid range is 0 to {len(color_tuple) - 1}.')
    
    print(f'Value is {color_tuple[tuple_index]}.')

# Your code goes here
except IndexError as excpt1:
    print(excpt1)
    print('Tuple operation is unsuccessful.')
    
    