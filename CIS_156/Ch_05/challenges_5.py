# Ahmed Roberts
# Challenges

# --------------------------------------------
# Challenge 5.2 - Level 1

sum_ints = 0
user_num = int(input('some number < 10: '))

while user_num < 10:
    print('before', sum_ints)
    sum_ints = sum_ints + user_num
    print('after', sum_ints)
    user_num = int(input('any number < 10: '))

print(sum_ints)

# --------------------------------------------
# Challenge 5.2 - Level 2

output_num = 0
num_input = int(input())

while num_input >= 0:
  if num_input % 3 == 0:
    print('miss')
  else:
    print('hit')
    output_num = output_num + 1
  num_input = int(input())
  
print(f'Output number is {output_num}')

# --------------------------------------------
# Challenge 5.3 - practice
import random
random.seed(5)

keep_bidding = 'y'
next_bid = 0

while keep_bidding != 'n':
   next_bid = next_bid + random.randint(1, 10)
   print(f'I\'ll bid ${next_bid}!')
   print('Continue bidding? (y/n)', end=' ')
   keep_bidding = input()
   
# --------------------------------------------
# Challenge 5.3 - practice

num_insects = int(input()) # Must be >= 1

while num_insects <= 100:
    print(num_insects, end=' ')
    num_insects = 2 * num_insects
    
# --------------------------------------------
# Challenge 5.3 - Level 1
    
num_successes = 0;

curr_velocity = int(input())

while num_successes < 2:
    if 15 <= curr_velocity <= 61:
        num_successes = num_successes + 1
        print(curr_velocity)

num_threshold = int(input())

k = 24

while k >= num_threshold:
    print(k)
    k -= 2
    

# --------------------------------------------------
outer_val = int(input())
inner_val = int(input())

count = 0
i = 0
while i <= outer_val:
    j = 0
    while j <= inner_val:
        count += 1
        j += 1
    i += 1

print(f'Inner loop ran {count} times')

# -------------------------------------------------------
first_range = int(input())
second_range = int(input())

count = 0
for i in range(first_range):
    for j in range(second_range):
        count += 1

print(f'Inner loop ran {count} times')

# -------------------------------------------------------
input_num = int(input())

for i in range(input_num + 1):
    print('#' * i, end='')
    print(i)
    
# --------------------------------------------------------
# -- Challenge 5.8.4

num_rows = int(input())
num_columns = int(input())

current_row = 1
for i in range(num_rows):
    current_column_letter = 'A'
    for j in range(num_columns):

        print(f'{i+1}{current_column_letter}', end=' ')
        current_column_letter = chr(ord(current_column_letter) + 1)  # Used to increment letters
    print()
    
# ----------------------------------------------------------
# Challenge 5.10.2

user_score = 0
simon_pattern = input()
user_pattern  = input()

for i in range(len(simon_pattern)):
    if user_pattern[i] == simon_pattern[i]:
        user_score += 1
    else:
        break

print(f'User score: {user_score}')

    
# ----------------------------------------------------------
# Challenge 5.10.2

origins = [4, 8, 10]

for (index, value) in enumerate(origins):
    print(f'Element {index}: {value}')
    
# ----------------------------------------------------------
# Challenge 5.12.2 - Level 1
beverage_orders = [input(), input(), input()]

for (order, beverage) in enumerate(beverage_orders):
    print(f'#{order + 1}: {beverage}')

# ----------------------------------------------------------
# Challenge 5.12.2 - Level 2
num_athletes = int(input())

athletes_list = []
for i in range(num_athletes):
    athletes_list.append(input())

for (pos, athlete) in enumerate(athletes_list):
    print(f'Athlete {athlete} is at position {pos + 1}')
    
# ----------------------------------------------------------
# Challenge 5.12.2 - Level 3
'''
Integer num_samples is read from input, representing the number of applicant names to be read from input. 
List applicants_list contains the applicant names read from the remaining input. For each element in applicants_list:

If the element's index is even, output the element followed by ' is scheduled for Wednesday'.
Otherwise, output the element followed by ' is scheduled for Monday'.
'''

num_samples = int(input())

applicants_list = []
for i in range(num_samples):
    applicants_list.append(input())

for (index, applicant) in enumerate(applicants_list):
    the_day = 'Monday' if (index % 2 != 0) else 'Wednesday'
    print(f'{applicant} is scheduled for {the_day}')

# ----------------------------------------------------------
#
channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}

for c in channels:
    print(f'{c} is on channel {channels[c]}')
    
