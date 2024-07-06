##############################################################

class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

#   def ... Add new method here ...
#        ...
    def calculate_pay(self):
        amount = self.wage * self.hours_worked
        return amount

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f'Alice:\n Net pay: {alice.calculate_pay():.2f}')

barbara = Employee()
barbara.wage = 11.50
barbara.hours_worked = 20
print(f'Barbara:\n Net pay: {barbara.calculate_pay():.2f}')

##############################################################

class Time:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    ''' Your code goes here '''
    def print_values(self):
        print(f'{self.hours}:{self.minutes}:{self.seconds}')

time1 = Time()
time1.hours = int(input())
time1.minutes = int(input())
time1.seconds = int(input())

time2 = Time()
time2.hours = int(input())
time2.minutes = int(input())
time2.seconds = int(input())

print(f'First time is:')
time1.print_values()
print(f'Second time is:')
time2.print_values()

##############################################################

class Coordinates3D:
    def __init__(self):
        self.x_coord = 0
        self.y_coord = 0
        self.z_coord = 0

    ''' Your code goes here '''
    def scale_x_y_z(self, scaler):
      self.x_coord = self.x_coord * scaler
      self.y_coord = self.y_coord * scaler
      self.z_coord = self.z_coord * scaler
    ''' Your code goes here '''

location1 = Coordinates3D()
location1.x_coord = int(input())
location1.y_coord = int(input())
location1.z_coord = int(input())
location2 = Coordinates3D()
location2.x_coord = int(input())
location2.y_coord = int(input())
location2.z_coord = int(input())

scaling_factor1 = int(input())
scaling_factor2 = int(input())

print(f"First location's original coordinates {location1.x_coord}, {location1.y_coord}, {location1.z_coord}")
print(f"Second location's original coordinates {location2.x_coord}, {location2.y_coord}, {location2.z_coord}")
location1.scale_x_y_z(scaling_factor1)
print(f"First location's scaled coordinates {location1.x_coord}, {location1.y_coord}, {location1.z_coord}")
location2.scale_x_y_z(scaling_factor2)
print(f"Second location's scaled coordinates {location2.x_coord}, {location2.y_coord}, {location2.z_coord}")

##############################################################
##############################################################