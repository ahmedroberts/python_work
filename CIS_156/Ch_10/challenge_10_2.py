print('\n------------------------------------\n')
numbers = [2, 4, 5, 8]
user_input = input()
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor > 20:
            # Possible NameError
            # compute() is not defined
            result = compute(result)
        elif divisor < 0:
            # Possible IndexError
            result = numbers[divisor]
        else:
            # Possible ZeroDivisionError
            result = 20 // divisor          # // truncates to an integer
        print(result, end=' ')
    except (ValueError, ZeroDivisionError):
        print('r', end=' ')
    except (NameError, IndexError):
        print('s', end=' ')
    user_input 
    
print('\n------------------------------------\n')

user_input = input()
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor < 0:
            # Possible NameError
            # compute() is not defined
            print(compute(divisor), end=' ')
        else:
            # Possible ZeroDivisionError
            print(20 // divisor, end=' ')     # // truncates to an integer
    except ValueError:
        print('v', end=' ')
    except ZeroDivisionError:
        print('z', end=' ')
    except:
        print('x', end=' ')
    user_input = input()
print('OK')

print('\n------------------------------------\n')

try:
	num_days = int(input())
	total_travelers = 100.0
	print(f'Average number of travelers per day is {total_travelers / num_days}')

# Your code goes here
except ValueError:
    print('int(): Input is not an integer.')
except ZeroDivisionError:
    print('total_travelers / num_days: Denominator cannot be zero.')
    
"""
Dictionary num_to_word contains key-value pairs 
5.5: 'five point five', 
9.5: 'nine point five', 
1.5: 'one point five', 
7.0: 'seven point zero', 
8.5: 'eight point five', and 2.5: 'two point five'. 
In the try block, float num_key is read from input. 
The key-value pair with num_key as the key in num_to_word is output. 
Complete the following tasks:

Write an exception handler to catch ValueError and output 'Input has to be a float.'
Write an exception handler to catch KeyError and output 'num_key is not a key in num_to_word.'
"""

num_to_word = {
	5.5: 'five point five', 9.5: 'nine point five', 1.5: 'one point five',
	7.0: 'seven point zero', 8.5: 'eight point five', 2.5: 'two point five'
}

try:
	num_key = float(input())
	print(f'{num_key} -> {num_to_word[num_key]}')

# Your code goes here
except ValueError:
  print('Input has to be a float.')
except KeyError:
  print('num_key is not a key in num_to_word.')