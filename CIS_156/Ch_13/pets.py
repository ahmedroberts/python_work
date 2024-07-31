# Ahmed Roberts
# Module 13 Programming Assignment
# Part A

# This program defines a pets a class and two derived classes.
# This program also demonstrates derived classes

''' Global Variables '''
spacer1 = '-'*25

''' Classes '''
# Base class of Pet
class Pet:  
  def __init__(self):
    self.name = 'unkown'
    self.age_months = 0
    self.person = 'unknown'
    self.gender = 'M'
    self.species = 'unknown'
    self.birth_year = '1980'
    
  def set_name(self, nomme):
    self.name = nomme
    
  def set_age(self, nani):
    self.age_months = nani
    
  def set_person(self, owner):
    self.person = owner
  
  def set_species(self, pet_type):
    self.species = pet_type
    
  def set_birth_year(self, first_appearance):
    self.birth_year = first_appearance
    
  def year_born(self):
    print(f'First Apperance of {self.name} was {self.birth_year}')
    
  def display(self):
    print(f'Pet {self.species} Info')
    print(spacer1)
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
    print(f'Has mane: {self.has_Mane}')
    print(f'Song:   Hakuna Matata')
    
# Tiger Class derived from Pet Class
class Tiger(Pet):
  def __init__(self):
    Pet.__init__(self)
    self.eats_cereal = False
    
  def ambush_prey(self):
    print('Hide from and stalk prey')
    
  def add_eats_cereal(self, pref):
    self.eats_cereal = pref
    
  def show_cereal_pref(self):
    if self.eats_cereal:
      print('Loves Frosted Flakes')
    else:
      print('Prefers meat to cereal.')
    
  # extend base display()
  def display(self):
    Pet.display(self)
    print(f'Eats cereal: {self.eats_cereal}')
    print("Phrase: They're Great!")

# Bear Class derived from Pet Class
class Bear(Pet):
  def __init__(self):
    Pet.__init__(self)
    self.fights_fires = False
    
  def will_fight_fires(self, fighter):
    self.fights_fires = fighter
    
  # extend base display()
  def display(self):
    Pet.display(self)
    print(f'Fights Fires: {self.fights_fires}')
    print('Hat:   Park Ranger')
    print('Fav Food:  Honey')
    
  def firefighter(self):
    print(f'Smokey says - Care...')
    print('Remember... Only you can prevent forest fires')
    
''' Functions '''
# Functions for demonstrations  
# Lion, Tiger, and Bear demos
def demo_lion_class():
  print(f'\n{spacer1}\n{spacer1}')
  lion_king =  Lion()
  lion_king.set_species('Lion')
  # lion_king.display()
  # lion_king.check_mane()
  lion_king.set_name('Simba')
  lion_king.set_age(30)
  lion_king.set_birth_year('1994')
  lion_king.set_person('Walt Disney')
  lion_king.grow_mane()
  lion_king.display()
  lion_king.year_born()
  lion_king.check_mane()
  print(f'{spacer1}\n{spacer1}\n')

def demo_tiger_class():
  print(f'\n{spacer1}\n{spacer1}')
  tony_tiger = Tiger()
  tony_tiger.set_species('Tiger')
  tony_tiger.set_name('Tony')
  tony_tiger.set_person('Kellogs')
  tony_tiger.add_eats_cereal(True)
  tony_tiger.set_age(55)
  tony_tiger.set_birth_year('1952')
  tony_tiger.display()
  tony_tiger.year_born()
  tony_tiger.ambush_prey()
  tony_tiger.show_cereal_pref()
  print(f'{spacer1}\n{spacer1}\n')
  
def demo_bear_class():
  print(f'\n{spacer1}\n{spacer1}')
  smokey_bear = Bear()
  smokey_bear.set_species('Bear')
  smokey_bear.set_name('Smokey')
  smokey_bear.set_person('National Wildlife')
  smokey_bear.set_age(99)
  smokey_bear.set_birth_year('1947')
  smokey_bear.will_fight_fires(True)
  smokey_bear.display()
  smokey_bear.year_born()
  smokey_bear.firefighter()
  print(f'{spacer1}\n{spacer1}\n')
 
''' Initialize U/I '''
# Call Demonstrations
demo_lion_class()
demo_tiger_class()
demo_bear_class() 
