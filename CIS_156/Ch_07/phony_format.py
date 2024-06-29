# Ahmed O. Roberts
# Module 07 - Programming Assignment
# Part B

# This program formats a 10 digit phone numer in two different formats

print('\nEnter a 10 digit phone number without punctuation: ')
raw_phone_num = '88865469872'
raw_phone_num_w_letters = '900Mixalot'

phone_number = raw_phone_num_w_letters
phone_number = raw_phone_num

def display_formatted_phone(tele_num):
  print(f'({tele_num[:3]}){tele_num[3:6]}-{tele_num[6:]}')
  print(f'{tele_num[:3]}-{tele_num[3:6]}-{tele_num[6:]}')
 
print('\n# ####################################################### #\n')

# display_formatted_phone(raw_phone_num_w_letters)
# display_formatted_phone(raw_phone_num)
# display_formatted_phone(phone_number)

if not phone_number.isdigit():
  phone_number = phone_number.upper()
  display_formatted_phone(phone_number)
display_formatted_phone(phone_number)
 

print('\n# ####################################################### #\n')
formatted_phone_num = "\n(888) 654-9872\n888-654-9872"
formatted_phone_num_w_letters = "\n(900) MIX-ALOT\n900-MIX-ALOT"
# print(formatted_phone_num, formatted_phone_num_w_letters)
# print(raw_phone_num, raw_phone_num.isdigit())
# print(raw_phone_num_w_letters, raw_phone_num_w_letters.isdigit())
print('\n# ####################################################### #\n')
