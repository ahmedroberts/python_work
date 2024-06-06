import math

#-----------------------------------------------------------------------
c_meters_per_sec = 299792458  # Speed of light (m/s)
joules_per_AA_battery = 4320.5  # Nickel-Cadmium AA batteries
joules_per_TNT_ton = 4.184e9

#Read in a floating-point number from the user
mass_kg = float(input('Hello Openheimer, how may kgs is it?: '))

#Compute E = mc^2.
energy_joules = mass_kg * (c_meters_per_sec**2)  # E = mc^2
print('Total energy released:', energy_joules, 'Joules')

#Calculate equivalent number of AA and tons of TNT.
num_AA_batteries = energy_joules / joules_per_AA_battery
num_TNT_tons = energy_joules / joules_per_TNT_ton

print('Which is as much energy as:')
print('  ', num_AA_batteries, 'AA batteries')
print('  ', num_TNT_tons, 'tons of TNT')
#-----------------------------------------------------------------------
n_value = float(input("enter a value for `n`: "))

p = -1.5 * (n_value * n_value) - 2.5 * n_value + 4.5

print(f'{p:.3f}')

#-----------------------------------------------------------------------
circle_radius = float(input())
circle_area = math.pi * (circle_radius * circle_radius)

''' Your code goes here '''
print(f'Area is {circle_area:.6f}')

#-----------------------------------------------------------------------
light_power  = float(input('Enter light power: ' ))
area_covered = float(input('Enter area covered: '))

light_intensity = light_power / area_covered

print(f'Light intensity is {light_intensity:.3f}')

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point_dist = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)) 

print(f'Points distance: {point_dist:.1f}')
#-----------------------------------------------------------------------