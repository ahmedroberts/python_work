# Ahmed Roberts

# This program executes code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
  print("You did not enter your name")
  name = input("Enter your name: ")
print(f"Hello, {name}.")