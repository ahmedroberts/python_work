# k = int(input())
list_data = [123, 67, 'poet', 'world']

k = 3
thingy = 'rabbit penguin 89 khaki 67 51 waxflower 61'

# for elem in input().split():
for elem in thingy.split():
	if elem.isdigit(): # If elem is a digit, then convert to int.
		list_data.append(int(elem))
	else:
		list_data.append(elem)

print(f'List item: {list_data[k-1]}')
print(len(list_data), thingy)

# ##################################################### #

sales_data = [
	'Ken', 20, 'Ina', 7, 
	'Avi', 15, 'Mia', 8, 
	'Abe', 19, 'Guy', 14, 
	'Ava', 5, 'Jan', 16, 
	'Tia', 9, 'Jen', 18, 
]
sales_person_idx = int(input('Enter and even number from 0 - 18: '))

print(f'{sales_data[sales_person_idx]} made {sales_data[sales_person_idx+1]} today.')

# ##################################################### #
'''Integer n and string my_name are read from input.
Then, five strings are read from input and stored in the list names_data.
Delete the second element in names_data,
then replace the n-th element of names_data with my_name.
n = int(input())
my_name = input()
names_data = input().split()
'''
''' Your code goes here '''

# print(f'My favorite names: {names_data}')
new_sales = sales_data[6:-4]
print('\n', sales_data, '\n', new_sales)

# ##################################################### #

# ##################################################### #