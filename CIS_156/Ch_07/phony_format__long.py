# Ahmed O. Roberts
# Module 07 - Programming Assignment
# Part B

# This program formats a 10 digit phone numer in two different formats

print('\nEnter a 10 digit phone number without punctuation: ')
raw_phone_num = '88865469872'
raw_phone_num_w_letters = 'a00MixalotZ the quick brown fox jumped over the lazy dogs'

phone_number = raw_phone_num
phone_number = raw_phone_num_w_letters

def display_formatted_phone(tele_num):
  print(f'({tele_num[:3]}){tele_num[3:6]}-{tele_num[6:]}')
  print(f'{tele_num[:3]}-{tele_num[3:6]}-{tele_num[6:]}')
  
def replace_letters_w_digits(str_x):
  str_x = str_x.replace('A', '2').replace('B', '2').replace('C', '2')
  str_x = str_x.replace('D', '3').replace('E', '3').replace('F', '3')
  str_x = str_x.replace('G', '4').replace('H', '4').replace('I', '4')
  str_x = str_x.replace('J', '5').replace('K', '5').replace('L', '5')
  str_x = str_x.replace('M', '6').replace('N', '6').replace('O', '6')
  str_x = str_x.replace('P', '7').replace('Q', '7').replace('R', '7').replace('S', '7')
  str_x = str_x.replace('T', '8').replace('U', '8').replace('V', '8').replace(' ', '')
  str_x = str_x.replace('W', '9').replace('X', '9').replace('Y', '9').replace('Z', '9')
  return str_x
 
print('\n# ####################################################### #\n')

# display_formatted_phone(raw_phone_num_w_letters)
# display_formatted_phone(raw_phone_num)
# display_formatted_phone(phone_number)

if not phone_number.isdigit():
  phone_number = phone_number.upper()
  display_formatted_phone(phone_number)
  phone_number = replace_letters_w_digits(phone_number)
display_formatted_phone(phone_number)
 

print('\n# ####################################################### #\n')
formatted_phone_num = "\n(888) 654-9872\n888-654-9872"
formatted_phone_num_w_letters = "\n(900) MIX-ALOT\n900-MIX-ALOT"
# print(formatted_phone_num, formatted_phone_num_w_letters)
# print(raw_phone_num, raw_phone_num.isdigit())
# print(raw_phone_num_w_letters, raw_phone_num_w_letters.isdigit())
print('\n# ####################################################### #\n')
