import second

def fct_a(number):
    return number - 3

def fct_b(number):
    return number * 5

def fct_c(number):
    return fct_a(number) + fct_b(number)

def fct_d(number):
    return second.fct_c(number)