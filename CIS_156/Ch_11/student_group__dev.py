# Ahmed O. Roberts
# Module 11 Programming Assignment
# Part A

# This program randomly assigns students to a group

import random

students = ['Clark', 'Diana', 'Bruce', 'Wally', 'John', 'Oswald', 'Selina', 'Edward', 'Rachel', 'Alfred']
print(len(students))
student_group = []
count = 0

num_in_group = int(input('\nInput the number (1 - 10) of students in the group: '))

while len(student_group) < num_in_group:
  count += 1
  selected_student = random.choice(students)
  print(count, selected_student)
  if selected_student not in student_group:
    student_group.append(selected_student)
  
print(student_group, '\n-------\n')

print('The group is:')
for student in student_group:
  print(student)
  
print()