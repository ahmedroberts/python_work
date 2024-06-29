# Ahmed O. Roberts
# Module 07 - Programming Assignment
# Part B

# This program formats a 10 digit phone numer in two different formats

phone_number = input('\nEnter a 10 digit phone number without punctuation: ')

while len(phone_number) != 10:
  phone_number = input('\nPlease enter 10 digits exactly with no punctuation: ')

# Print two formats of the current number
def display_formatted_phone(tele_num):
  print(f'({tele_num[:3]}){tele_num[3:6]}-{tele_num[6:10]}')
  print(f'{tele_num[:3]}-{tele_num[3:6]}-{tele_num[6:10]}')

# Change the letters for digits based on a key
def replace_letters_w_digits(str_x):
  str_x = str_x.replace('A', '2').replace('B', '2').replace('C', '2')
  str_x = str_x.replace('D', '3').replace('E', '3').replace('F', '3')
  str_x = str_x.replace('G', '4').replace('H', '4').replace('I', '4')
  str_x = str_x.replace('J', '5').replace('K', '5').replace('L', '5')
  str_x = str_x.replace('M', '6').replace('N', '6').replace('O', '6')
  str_x = str_x.replace('P', '7').replace('Q', '7').replace('R', '7').replace('S', '7')
  str_x = str_x.replace('T', '8').replace('U', '8').replace('V', '8')
  str_x = str_x.replace('W', '9').replace('X', '9').replace('Y', '9').replace('Z', '9')
  return str_x

# if the number has any letters, uppercase then display
if not phone_number.isdigit():
  phone_number = phone_number.upper()
  display_formatted_phone(phone_number)
  phone_number = replace_letters_w_digits(phone_number)
  
# display the current phone number
display_formatted_phone(phone_number)
