import my_funcs

n = int(input('Enter number: '))
fact = my_funcs.factorial(n)

for i in range(1, n + 1):
    print(i, end=' ')
    if i != n:
        print('*', end=' ')

print(f'= {fact}')