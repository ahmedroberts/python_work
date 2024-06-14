# Ahmed Roberts The 9th Raikage 
# June 2024 - Estrella Mountain CC
# CIS156 Python Progamming - Level 1

code_break = '#-----------------------------------------------------------------------'
print(f'\n{code_break}\n')

#-----------------------------------------------------------------------
# Tuples
city_name = input('City name: ')
state_located = input('State located: ')
population_count = int(input('Enter population: '))

city_info = (city_name, state_located, population_count)

print(f'City name: {city_info[0]}, State: {city_info[1]}, Population: {city_info[2]}')

print(f'\n{code_break}\n')

#-----------------------------------------------------------------------
# Tuples 2

''' start missing '''
from collections import namedtuple
City = namedtuple('City', ['name', 'state', 'population'])
''' endof missing '''

city_name = input()
state_located = input()
population_count = int(input())

city_info = City(city_name, state_located, population_count)

print(f'City name: {city_info.name}, State: {city_info.state}, Population: {city_info.population}')

print(f'\n{code_break}\n')

#-----------------------------------------------------------------------
# Tuples 3

from collections import namedtuple

School = namedtuple('School', ['name', 'city', 'state', 'enrollment'])

school_name = input()
city_located = input()
state_located = input()
enrollment_count = int(input())


''' start missing '''
school_info = School(school_name, city_located, state_located, enrollment_count)
''' endof missing '''

print(f'School name: {school_info.name}, City: {school_info.city}, State: {school_info.state}, Enrollment: {school_info.enrollment}')