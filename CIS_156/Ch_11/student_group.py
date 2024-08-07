# Ahmed O. Roberts
# Module 11 Programming Assignment
# Part A

# This program randomly assigns students to a group

import random

students = ['Clark', 'Diana', 'Bruce', 'Hal', 'John', 'Arthur', 'Barry', 'Lois', 'Alfred', 'Selina']
print(len(students))
student_group = []

num_in_group = int(input('\nInput the number (1 - 10) of students in the group: '))

# only select as many as needed
while len(student_group) < num_in_group:
  selected_student = random.choice(students)
  # if student not already in the list (assunmes names to be unique)
  if selected_student not in student_group:
    student_group.append(selected_student)

print('The group is:')
for student in student_group:
  print(student)
  
print()