'''
user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


sum_extra = 0 # Initialize 0 before your loop

for score in test_grades:
    score = int(score)
    if score > 100:
        sum_extra += score - 100

print(f'Sum extra: {sum_extra}')
'''

'''
List samples_list contains integers read from input, representing data samples from an experiment. For each element in samples_list:

If the element's value is greater than or equal to 45, then increment passed_count and output the element's value, followed by ' at index ', the element's index, and ' passed'.
Otherwise, output the element's value, followed by ' at index ', the element's index, and ' failed'.
'''

# Read input and split input into tokens
tokens = input().split()

samples_list = []
for token in tokens:
    samples_list.append(int(token))

print(f'Raw samples: {samples_list}')

passed_count = 0

''' Your code goes here '''
for i, score in enumerate(samples_list):
    if score >= 45:
        print(f'{score} at index {i} passed')
        passed_count += 1
    else:
        print(f'{score} at index {i} failed')
''' end code '''

print(f'Total passed samples: {passed_count}')

# #################################################### #
# Read input and split input into tokens
tokens = input().split()

pressure_data = []
for token in tokens:
    pressure_data.append(int(token))

print(f'All data: {pressure_data}')

''' Your code goes here '''
sum_passed = 0
for index, score in enumerate(pressure_data):
    if (index % 2 == 1) and (score >= 55):
        print(f'Index {index}: {score}')
        sum_passed += score
''' end my code '''

print(f'Sum of selected elements is: {sum_passed}')

# #################################################### #
# Read input and split input into tokens
tokens = input().split()

sequence_data = []
for token in tokens:
    sequence_data.append(int(token))

print(f'Sequence: {sequence_data}')

min_diff = None

''' Your code goes here '''
for index in range(len(sequence_data)-1):
    neighbor_diff = sequence_data[index+1] - sequence_data[index]
    print(f'{sequence_data[index+1]} - {sequence_data[index]} = {neighbor_diff}')
    
    if min_diff == None:
        min_diff = neighbor_diff
    else:
        min_diff = neighbor_diff if (neighbor_diff < min_diff) else min_diff
''' end my code '''