'''
src_name is assigned with a file's name read from input. Perform the following tasks:

Open the file named src_name, and assign a variable leek_file with the file object.
Use leek_file's read() to read the contents of src_name and assign leek_data with the string read.
Close leek_file.
'''

src_name = input()

''' Your code goes here '''
leek_file = open(src_name)
leek_data = leek_file.read()
leek_file.close()
''' Your code ends here '''

print(leek_data)

print('\n--------------------------------------\n')

'''
A file's name is read from input. The file is opened and yam_file is assigned with the file object. 
Each line in yam_file contains an integer representing the number of yams eaten in a day. 
Use a loop to read each line of yam_file. 
Inside the loop, subtract each integer in yam_file from quantity_remaining.
'''

quantity_remaining = 40
print(f'Total yams: {quantity_remaining}')

yam_file = open(input())

''' Your code goes here '''
lines = yam_file.readlines()

for ln in lines:
    quantity_remaining -= int(ln)
''' Your code ends here '''

yam_file.close()

print(f'Yams remaining: {quantity_remaining}')