# Ahmed Roberts
# New Boston supplement

# This program loops through a list of foods

foods = ['raisins', 'gatorade zero', 'peanuts', 'salad', 'rib tips']

for f in foods[2:4]:
  print(f)
  print(len(f))
  
# This program loops with range
power_level = 5
code_break = '# -------------------------------------'

# ----------------------------------------------------
def line_break(): {
  print(code_break)
}
line_break()
# ----------------------------------------------------
for x in range(5, 12):
  print(f'{x} in range (5, 12)')
  
line_break()
# ----------------------------------------------------
for x in range(10, 40, 5):
  print(f'{x} in range (10, 40, 5)')
  
line_break()
# ----------------------------------------------------
while power_level < 10:
  print(f'Power level is {power_level}.')
  power_level += 1
  
line_break()
