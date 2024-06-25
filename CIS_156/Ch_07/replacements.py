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
    
string_input = '9th Raikage'

first_2 = string_input[:2]
after_2 = string_input[2:]

if first_2.isdigit() and after_2.isspace() :
    print('Valid')
else:
    print('Invalid')