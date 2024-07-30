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

'''
File 'data.txt' is opened for writing. file_obj is assigned with the opened file. Integer start_x is read from input. Complete the following tasks:

Write 'Three values: ' to file_obj.
Write the values of start_x, start_x - 2, and start_x - 4 to file_obj. Separate each value with a comma (',').
Write a newline to file_obj.
'''

file_obj = open('data.txt', 'w')
start_x = int(input())

''' Your code goes here '''
file_obj.write('Three values: ')
file_obj.write(str(start_x))
file_obj.write(',')
file_obj.write(str(start_x - 2))
file_obj.write(',')
file_obj.write(str(start_x - 4))
file_obj.write('\n')
''' Your code ends here '''

file_obj.close()

print('\n------------------------------------\n')

'''
File name foods_data and value one_food_value are read from input. 
Perform the following tasks:

Open the file foods_data with the 'w+' update mode for reading and writing at the same time. 
Assign foods_file with the opened file.
Write one_food_value to foods_file, overwriting any existing contents.
Call foods_file's flush().
'''

foods_data = input()
one_food_value = input()

''' Your code goes here '''
foods_file = open(foods_data, 'w+')
foods_file.write(one_food_value)
foods_file.flush()
''' Your code ends here '''

# When a file is in update mode, 
# seek(0, 0) rewinds the file to enable reading from the beginning
foods_file.seek(0, 0)  

file_data = foods_file.read()
print(file_data)

foods_file.close()