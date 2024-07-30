f = open('myfile.txt', 'w')  # Open file
f.write('Example string:\n  test....')  # Write string
f.close()  # Close the file

print('\n------------------------------------\n')

num1 = 5
num2 = 7.5
num3 = num1 + num2

f = open('myfile.txt', 'w')
f.write(str(num1))
f.write(' + ')
f.write(str(num2))
f.write(' = ')
f.write(str(num3))
f.close()

print('\n------------------------------------\n')

'''
Read mode 'r' opens a file for reading. If the file is missing, then an error will occur.
Write mode 'w' opens a file for writing. If the file is missing, then a new file is created. Contents of any existing file are overwritten.
Append mode 'a' opens a file for writing. If the file is missing, then a new file is created. Writes to the file are appended to the end of an existing file's contents.
Additionally, a programmer can add a '+' character to the end of a mode, like 'r+' and 'w+' to specify an update mode. Update modes allow for both reading and writing of a file at the same time.
'''

paints_data = input()
one_paint_value = input()

''' Your code goes here '''
paints_file = open(paints_data, 'a')
paints_file.write(one_paint_value)
paints_file.write('\n')
paints_file.close()
''' Your code ends here '''

print('\n------------------------------------\n')



