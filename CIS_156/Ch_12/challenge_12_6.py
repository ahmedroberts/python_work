'''
A with statement can be used to open a file, execute a block of statements, 
and automatically close the file when complete.

Forgetting to close a file can sometimes cause problems. 
For example, a file opened in write mode cannot be written to by other programs. 
Good practice is to use a with statement 
when opening files to guarantee that the file is closed when no longer needed.
'''
print('Opening myfile.txt')

# Open a file for reading and appending
with open('myfile.txt', 'r+') as f:
    # Read in two integers
    num1 = int(f.readline())
    num2 = int(f.readline())

    product = num1 * num2

    # Write back result on own line
    f.write('\n')
    f.write(str(product))

# No need to call f.close() - f closed automatically 
print('Closed myfile.txt')
print('\n------------------------------------\n')

'''

'''
print('\n------------------------------------\n')