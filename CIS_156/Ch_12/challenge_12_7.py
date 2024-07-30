'''

'''
import csv

with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    for row in grades_reader:
        print(f'Row #{row_num}: {row}')
        row_num += 1


print('\n------------------------------------\n')

import csv

# Dictionary that maps student names to a list of scores
grades = {}

# Use with statement to guarantee file closure
with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    first_row = True
    for row in grades_reader:
        # Skip the first row with column names
        if first_row:
            first_row = False
            continue

        ## Calculate final student grade ##

        name = row[0]

        # Convert score strings into floats
        scores = [float(cell) for cell in row[1:]]

        hw1_weighted = scores[0]/10 * 0.05
        hw2_weighted = scores[1]/10 * 0.05
        mid_weighted = scores[2]/100 * 0.40
        fin_weighted = scores[3]/100 * 0.50

        grades[name] = (hw1_weighted + hw2_weighted + 
                        mid_weighted + fin_weighted) * 100

for student, score in grades.items():
    print(f'{student} earned {score:.1f}%')
    
'''

'''

print('\n------------------------------------\n')

import csv

row1 = ['100', '50', '29']
row2 = ['76', '32', '330']

with open('gradeswr.csv', 'w', newline='') as csvfile:
    grades_writer = csv.writer(csvfile)

    grades_writer.writerow(row1)
    grades_writer.writerow(row2)

    grades_writer.writerows([row1, row2])

# ------------------------------------------------------
print('\n------------------------------------\n')

'''
Airline,Destination,Departure time,Plane
Southwest,Phoenix,615,B747
Alitalia,Milan,1545,B757
British Airways,London,1230,A380
'''

import csv
with open('myfile.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)
    
import csv
with open('myfile.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        print(row[1])

# ----------------------------------------------------------