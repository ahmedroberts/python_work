# Ahmed Roberts
# Module 13 Programming Assignment
# Part A

# This program defines a pets a class and two derived classes.
# This program also demonstrates both derived classes

# Base class of pet
class Pet:
  def __init__(self):
    self.name = ''
    self.age_months = 0
    self.person = ''
    self.gender = 'M'
    
  def set_name(self, nomme):
    self.name = nomme
    
  def set_age(self, nani):
    self.age_months = nani
    
  def set_person(self, owner):
    self.person = owner
    
  def display(self):
    print("\nPet Info\n------------------------------")
    print(f'Name:   {self.name}')
    print(f'Months: {self.age_months}')
    print(f'Person: {self.person}')
    print(f'Sex:    {self.gender}')

# Lion Class derived from Pet Class
class Lion(Pet):
  def __init__(self):
    Pet.__init__(self)
    self.has_Mane = False
    
  def grow_mane(self):
    if (self.gender == 'M') and (self.age_months > 12):
      self.has_Mane = True
      
  def check_mane(self):
    if self.has_Mane:
      print('Has a luscious mane.')
    else:
      print('No mane on this one.')
  
  # extend base display()
  def display(self):
    Pet.display(self)
    print('Hakuna Matata')
      
# Tiger Class derived from Pet Class
class Tiger(Pet):
  def __init__(self):
    Pet.__init__(self)
    self.eats_cereal = False

# Bear Class derived from Pet Class
class Bear(Pet):
  def __init__(self):
    Pet.__init__(self)
    self.fights_fires = False

# Functions for demonstrations  
def demo_lion_class():
  lion_king =  Lion()
  lion_king.display()
  lion_king.check_mane()
  lion_king.set_name('Simba')
  lion_king.set_age(30)
  lion_king.grow_mane()
  lion_king.display()
  lion_king.check_mane()

def demo_tiger_class():
  tony_tiger = Tiger()
  tony_tiger.display()
  
def demo_bear_class():
  smokey_bear = Bear()
  smokey_bear.display()
 
# Call Demonstrations
demo_lion_class()
demo_tiger_class()
demo_bear_class() 
