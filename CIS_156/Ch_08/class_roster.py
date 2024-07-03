# Ahmed O. Roberts
# Module 08 - Programming Assignment
# Part A

# This program allows the user to enter the students on a class roster 
# - after entering the number of students

roster = []
greeting = '\nWelcome to the student roster creator\n'
prompt_count = 'Enter the number of math students: '
prompt_student_entry = 'Enter student name: '

# Greet
print(greeting)
# Get the number of students
count_students = int(input(prompt_count))

# Add each student to roster from input
for student in range(count_students):
  student_name = input(prompt_student_entry)
  roster.append(student_name)
  
# Print the full roster
print('\n', roster, '\n')