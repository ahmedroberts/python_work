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