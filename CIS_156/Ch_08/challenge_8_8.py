'''
Ahmed O. Roberts
2024.07.02
'''
def code_breaker():
  print('\n################################################\n')

code_breaker() ################################################

my_list = [10, 20, 30]
list_plus_5 = [(i + 5) for i in my_list]

print(my_list, '... + 5')
print(f'New list contains: {list_plus_5}')

code_breaker() ################################################

'''
List raw_list contains integers read from input. 
Assign processed_list with a new list where each element is three times the corresponding element in raw_list.
'''

raw_list = []

# Read input
# tokens = input().split()
# for token in tokens:
#     raw_list.append(int(token))

raw_list = [19, 21, 32, 4, 5, 6, 9]

processed_list = [(num * 3 ) for num in raw_list]

print(f'Original: {raw_list}')
print(f'Processed: {processed_list}')

code_breaker() ################################################
'''
List num_list contains strings read from input. 
Use list comprehension to convert each string in num_list to an integer, 
and assign updated_list with the new list returned by list comprehension.
'''
num_list = ['16', '11', '22', '7', '22', '7', '9']
updated_list = [(int(num_string)) for num_string in num_list]

print(f'Raw: {num_list}')
print(f'Updated: {updated_list}')

code_breaker() ##########################################samples_list = [int(x) for x in input().split()]

samples_list = [-42, 26, 31, -48, -11, 16, 20, -18, -1, 40]
filtered_list = [i for i in samples_list if i < 0]

print(f'All numbers: {samples_list}')
print(f'Negative numbers: {filtered_list}')######

code_breaker() ################################################
inp_list = [[47, 41], [19, 34, 5], [100], [5, 2]]
processed_list = [sum(row) for row in inp_list]

print(f'All numbers: {inp_list}')
print(f'Sum of each row: {processed_list}')

code_breaker() ################################################
'''
Get the sum of the max from each row
'''

# num_rows = int(input())
# data_list = []
# for i in range(num_rows):
#     data_list.append([int(x) for x in input().split()])

data_list = [[45, 44], 
             [31, 36, 26, 49], 
             [4, 40, 17, 28, 41, 32, 19, 8], 
             [1, 42, 12, 35, 21, 7, 17, 43], 
             [48, 22, 11, 31, 12, 40, 5, 37], 
             [11, 43, 23, 31, 30, 25]
             ]
computed_value = sum([max(row) for row in data_list])

print(f'All numbers: {data_list}')
print(f'Sum of the largest values from each row: {computed_value}')

code_breaker() ################################################