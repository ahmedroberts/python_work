# Ahmed O. Roberts
# Module 09 Programming Assignment
# Part A

# Yhis program creates a class to keep track of aircraft

"""
  _summary_
  You're helping a small airport design a simple system to assist their air traffic controllers, 
  and your task is to develop and test a class for keeping track of aircraft in the area in a file aircraft.py. 

First, create an Aircraft class with the following specifications:

Attributes
aircraft_id (this is an alphanumeric identification code. For example, N121PP  or N898TS)
altitude (this is the aircraft's altitude above sea level, in feet).
distance (this is the aircraft's distance from the airport, in miles).
A constructor with parameters for each of the three attributes
Methods
increase_altitude, which adds 500 to the aircraft's altitude
decrease_altitude, which reduces its altitude by 500
move_closer, which decreases distance by 10
move_farther, which adds 10 to the distance
print_position, which prints out the aircraft's id, altitude, and distance
Next, write code in the main section of your script (not in the class definition) 
that prompts the user to input information for two aircraft and creates two objects of the Aircraft class using their responses.

Then, call each of the methods at least one time (making sure at least one method is called on each object). 
Finally, use the print_position method to output information about both objects.
"""

class Aircraft:
  def __init__(self, aircraft_id, altitude, distance):
    self.aircraft_id = aircraft_id
    self.altitude = altitude
    self.distance = distance
    
  def increase_altitude(self, altitude):
    increased_altitude = altitude + 500
    return increased_altitude
  
  def decrease_altitude(self, altitude):
    decreased_altitude = altitude - 500
    return decreased_altitude
  
  def move_closer(self, distance):
    closer_distance = distance - 10
    return closer_distance
  
  def move_farther(self, distance):
    farther_distance = distance + 10
    return farther_distance
  
  def print_position(self):
    print(f'\nId: {self.aircraft_id}\nAltitude: {self.altitude}\nDistance: {self.distance}')
    

aircraft1_id = input('Enter first aircraft id: ')
aircraft1_alt = int(input('Enter first aircraft altitude: '))
aircraft1_dist = int(input('Enter first aircraft distance: '))

aircraft2_id = input('Enter second aircraft id: ')
aircraft2_alt = int(input('Enter second aircraft altitude: '))
aircraft2_dist = int(input('Enter second aircraft distance: '))

aircraft1 = Aircraft(aircraft1_id, aircraft1_alt, aircraft1_dist)
aircraft2 = Aircraft(aircraft2_id, aircraft2_alt, aircraft2_dist)

print()
aircraft1.print_position()
aircraft2.print_position()

print('\n# Aircraft 1: increase 99, decrease 5, closer 22')
aircraft1.increase_altitude(99)
aircraft1.decrease_altitude(5)
aircraft1.move_closer(22)

print('# Aircraft 2: increase 75, decrease 15, closer 44\n')
aircraft2.decrease_altitude(15)
aircraft2.move_closer(44)
aircraft2.increase_altitude(75)

aircraft1.print_position()
aircraft2.print_position()
  