# Ahmed O. Roberts
# Module 07 - Programming Assignment
# Part A

# This program counts the number of vowels in a given string

evaluated_string = "aaaaaaaaarrrgghhh! -- King Ahmed is the 9th Raikage  AEIOUY aeiouy!"

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
  vowel_count = 0
  for v in my_dict:
    curr_vowel_count = 0
    for char in string_to_evaluate:
      if char == v or char == my_dict[v]:
        curr_vowel_count += 1
    print('---', v, char, curr_vowel_count)
    vowel_count += curr_vowel_count
  print('*** Total Vowel Count: ', v, vowel_count)
  print(char, curr_vowel_count, )
  
  return count_vowels

print('\nEnter a phrase or sentence: ', evaluated_string)
print('\nOccurrences of each vowel')
make_line()   
count_vowels(vowel_dict, evaluated_string)
make_line()
 