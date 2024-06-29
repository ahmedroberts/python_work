# Ahmed O. Roberts
# Module 07 - Programming Assignment
# Part A

# This program counts the number of vowels in a given string

print('\nEnter a phrase or sentence: ')

evaluated_string = "aaaaaaaaarrrgghhh! -- King Ahmed is the 9th Raikage  AEIOUY aeiouy!"
evaluated_string = input()

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

def count_vowels(my_dict, string_to_evaluate):
  print('\nOccurrences of each vowel')
  make_line()
  vowel_count = 0
  for v in my_dict:
    curr_vowel_count = 0
    for char in string_to_evaluate:
      if char == v or char == my_dict[v]:
        curr_vowel_count += 1
    # print('---', v, char, curr_vowel_count)
    print(f'{v:9}{curr_vowel_count:3}')
    vowel_count += curr_vowel_count
  make_line()
  print(f'{"Total":9}{vowel_count:3}\n')

count_vowels(vowel_dict, evaluated_string)
 