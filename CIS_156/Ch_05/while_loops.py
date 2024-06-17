# Ahmed Roberts

# This program executes code WHILE some condition remains true
code_break = '# -------------------------------------\n'

# ----------------------------------------------------
def line_break(): {
  print(code_break)
}
line_break()

# ----------------------------------------------------
age = int(input("Enter your age: "))

while age < 0:
  print("Age can't be negative")
  age = int(input("Enter your age: "))

print(f"You are {age} years old.")

line_break()

# ----------------------------------------------------
food = input("Enter a food you like (q to quit): ")

while not food == "q":
  print(f"You like {food}.")
  food = input("Enter another food you like (q to quit): ")
  
print("bye")

line_break()

# ----------------------------------------------------
num = int(input("Enter a # between 1 - 10: "))

while (num < 1) or (num > 10):
  print(f"{num} is not valid.")
  num = int(input("Please enter a # between 1 - 10: "))
  
print(f"Your number is {num}.")

line_break()