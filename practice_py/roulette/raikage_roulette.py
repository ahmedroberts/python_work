'''
Ahmed The 9th Raikage
Using Python with real roulette
February 12, 2024
'''

import os
import numpy as np

my_cwd = os.getcwd()
print(my_cwd)
# File Path from P1HT
raw_spins_file_path = "zqj/py/roulette/1603_real_spins.txt"

'''
Let's get our file and our modules
We need location (os) and injest text file number data (NumPy)
'''

# red text into NumPy array
spins_array = np.loadtxt(raw_spins_file_path)
print(f'\n{spins_array.dtype}')
print(len(spins_array))

print(f'NumPy Array:\n{spins_array}\n')

# convert to Python List
spins_list = spins_array.tolist()
# print(f'List: {spins_list}')
print(type(spins_list))
print(len(spins_list))
# Start:End:Jump
print(f'Python List:\n{spins_list[0:99:9]}\n')



'''
f_spins = open(raw_spins_file_path, "r")
print(f_spins.read())
f_spins.close()
'''
