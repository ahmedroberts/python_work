'''
Instead of writing the literal path = "subdir\\bat_mobile.jpg", 
a programmer should write path = os.path.join('subdir', 'bat_mobile.jpg'), 
which will result in "subdir\\bat_mobile.jpg" on Windows and "subdir/bat_mobile.jpg" on Linux/Mac.
'''

'''
x: In Windows, the path to a file is represented as "subdir\\bat_mobile.jpg", 
but on a Mac, the path is "subdir/bat_mobile.jpg". 
The character between directories, "\\"or "/", is called the path separator, 
and using the incorrect path separator may result in that file not being found.
'''

print('\n------------------------------------\n')

'''

'''
print('\n------------------------------------\n')

# os.path.split(path) – Splits a path into a two-tuple (head, tail), 
# where tail is the last token in the path string and head is everything else.
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print(os.path.split(p))

# os.path.exists(path) – Returns True if path exists, else returns False
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
if os.path.exists(p):
    print('Suit up....')
else:
    print('The Lamborghini then?')
    
# os.path.isfile(path) – Returns True if path is an existing file, 
# and false otherwise (e.g., path is a directory)
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'bat_chopper')
if os.path.isfile(p):
    print('Found a file....')
else:
    print('Not a file....')
    
# os.path.getsize(path) – Returns the size in bytes of path.
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print(f'Size of file: {os.path.getsize(p)} bytes')



