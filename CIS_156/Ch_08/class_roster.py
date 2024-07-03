# Ahmed O. Roberts
# Module 08 - Programming Assignment
# Part A

# This program allows the user to enter the students on a class roster 
# after entering the number of students

roster = []
greeting = '\nWelcome to the student roster creator\n'
prompt_count = 'Enter the number of students: '
prompt_student_entry = 'Enter student name: '

print(greeting)
count_students = int(input(prompt_count))
student_name = input(prompt_student_entry)

for student in range(count_students):
  print(student)
  roster.append(student_name)
  print(roster)
  student_name = input(prompt_student_entry)
  print(roster)
  
print('\n', roster)