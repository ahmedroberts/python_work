'''
A programmer modifies every element of a list in the same way, such as adding 10 to every element. 
The Python language provides a convenient construct, known as 
list comprehension, 
that iterates over a list,
modifies each element, 
and returns a new list of the modified elements.

A list comprehension construct has the following form:

new_list = [expressoin for loop_variable_name in iterable]
new_list = [expressoin for loop_variable_name in iterable ( if condition)]
'''
def code_breaker():
  print('\n################################################\n')

code_breaker() ################################################

my_list = [10, 20, 30]
list_plus_5 = [(i + 5) for i in my_list]

print(my_list, '... + 5')
print(f'New list contains: {list_plus_5}')

code_breaker() ################################################