# Ahmed O. Roberts
# Module 07 - Programming Assignment
# Part A

# This program counts the number of vowels in a given string

evaluated_string = "King Ahmed is the 9th Raikage  AEIOUY aeiouy!"

# vowel_count = 0
# count_a = 0
# count_e = 0
# count_i = 0
# count_o = 0
# count_u = 0
# count_y = 0

vowel_dict = {
  'A': 'a',
  'E': 'e',
  'I': 'i',
  'O': 'o',
  'U': 'u',
  'Y': 'y'
}

def make_line():
  print(f'{"-" * 24}')

make_line()  
# for char in evaluated_string:
#   if char == 'A' or char == 'a':
#     count_a += 1
#     print(char, count_a)
  
  # print(char)

# vowel_count += count_a

# print('A', count_a, '==> vc', vowel_count)
make_line()  


def count_vowels(my_dict):
  vowel_count = 0
  curr_vowel_count = 0
  for v in my_dict:
    for char in evaluated_string:
      if char == v or char == my_dict[v]:
        curr_vowel_count += 1
        # print(v, my_dict[v], '==>', curr_vowel_count)
    print('---', v, char, curr_vowel_count)
    curr_vowel_count = 0
  vowel_count += curr_vowel_count
  print('***', v, char, curr_vowel_count, vowel_count)
  # print('vowel count ==>', vowel_count)
  
count_vowels(vowel_dict)
make_line()
 