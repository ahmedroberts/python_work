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

