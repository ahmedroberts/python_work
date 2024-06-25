phrase = 'Someday I will have three goats, six horses, and nine llamas.'
print('\n\t', phrase)

# Replace English with Spanish.
phrase = phrase.replace('one', 'uno')
phrase = phrase.replace('two', 'dos')
phrase = phrase.replace('three', 'tres')
phrase = phrase.replace('four', 'cuatro')
phrase = phrase.replace('five', 'cinco')
phrase = phrase.replace('six', 'seis')
phrase = phrase.replace('seven', 'siete')
phrase = phrase.replace('eight', 'ocho')
phrase = phrase.replace('nine', 'nueve')

print('Translation:', phrase, '\n')


phone_number = '202-555-0106'

separator = ';'
phone_number_tokens = phone_number.split('-')
print(separator.join(phone_number_tokens))

string_of_letters = 'Ahmed is the 9th Raikage'

m_index = string_of_letters.find('m')
new_string = string_of_letters.replace('m', '++')

if 'm' in string_of_letters:
    print(f'Located at index: {m_index}')
    print(new_string)
else:
    print('No results')
    
name1 = 'Raikage'
name2 = 'Ahmed'

if (name1 == name2):
    print('Same characters')
else:
    smaller_name = name1 if (name1 < name2) else name2
    print(smaller_name)

"""
String string_input is read from input. If the first two characters are all digits,
and the rest of the string is whitespace, output 'Valid'.
Otherwise, output 'Invalid'.
"""
string_input = '9th Raikage'

first_2 = string_input[:2]
after_2 = string_input[2:]

if first_2.isdigit() and after_2.isspace() :
    print('Valid')
else:
    print('Invalid')
    
"""
String string_data is read from input with leading and trailing whitespaces. 
Remove any leading and trailing whitespaces in the string. 
If string_data contains the string 'Paint color:', lowercase all the characters in string_data. 
Otherwise, capitalize the first letter for each word in string_data. 
Finally, print out the resulting string.
"""
string_data = 'ahmed is the 9th Raikage'
string_data = string_data.strip()

if 'Paint color' in string_data:
    string_data = string_data.lower()
else:
    string_data = string_data.capitalize()
    
print(string_data)

""" asdkj;kladsj;"""
beverage_choices = 'muscle milk, water, soda, juice'
insert_at = 2

beverage_list = beverage_choices.split(',')
beverage_list.insert(insert_at, 'coffee')

print(beverage_list)

"""
List tias_number is read from input. Join the strings in tias_number 
together to create a single string with ']-[' 
as the separator and assign formatted_number with the result.

Ex: If the input is +55 9 600 892, then the output is:

Tia's number: [+55]-[9]-[600]-[892]
"""
tias_number = '+1 291 555 5874'
tias_number.split()

joiner = ']-['
formatted_number = joiner.join(tias_number)

formatted_number = '[' + formatted_number + ']'
print(f"Tia's number: {formatted_number}")