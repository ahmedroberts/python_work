import arithmetic
import data
import red
import yellow
import first_funcs


def calculate(number):
    return number + 5

print(arithmetic.calculate(data.small))
print(calculate(data.small))
print(red.medium)
print(yellow.medium)

def fct_a(number):
    return number ** 2

def fct_b(number):
    return number * 1

def fct_c(number):
    return fct_a(number) - fct_b(number)

print(fct_c(4))
print(first_funcs.fct_c(4))
print(first_funcs.fct_d(4))