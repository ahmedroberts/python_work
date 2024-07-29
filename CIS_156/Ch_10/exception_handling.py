user_input = "\nEnter any key ('q' to quit): "
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print(f'BMI: {bmi}')
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except:
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")


print('\n---------------------------------------------\n')
try:
    number1 = int(input('\nEnter a Number: '))
    print(number1 * 2)

    number2 = int(input('\nEnter a 2nd Number: '))
    print(number2 * 2)
except:
    print('x')
print('e')

print('\n---------------------------------------------\n')
user_input = input('\nEnter a Number: ')
try:
    while user_input != 'q':
        number = int(user_input)
        print(number * 2)
        user_input = input()
except:
    print('x')
print('e')


print('\n---------------------------------------------\n')
user_input = ''
while user_input != 'q':
    try:
        weight = int(input("\nEnter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print(f'BMI: {bmi}')
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except ValueError:
        print('Could not calculate health info.\n')
    except ZeroDivisionError:
        print('Invalid height entered. Must be > 0.')

    user_input = input("Enter any key ('q' to quit): ")
    
    
    