class Time:
  """ A class that represents a time of day """
  def __init__(self):
    self.hours = 0
    self.minutes = 0
        
''' Hello '''

my_time = Time()
my_time.hours = 7
my_time.minutes = 15

print(f'{my_time.hours} hours', end=' ')
print(f'and {my_time.minutes} minutes')

class Superhero:
  """ A class that represents a Superhero """
  def __init__(self):
    self.secret_identity = ''
    self.supername = ''
    strength = 0
    speed = 0
    stealth = 0
    laser = 0
    
raikage_ahmed = Superhero()

raikage_ahmed.strength = 6
raikage_ahmed.speed = 7
raikage_ahmed.laser = 5

print(f'My Speed is: {raikage_ahmed.speed}')