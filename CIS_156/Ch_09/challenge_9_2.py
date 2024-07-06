class BookDetails:
    def __init__(self):
        self.title = 'unknown'
        self.year_published = 0
        self.num_chapters = 0

''' Your code goes here '''
book = BookDetails()
book.title = input()
book.year_published = int(input())
book.num_chapters = int(input())

print('Book details:', end=' ')
print(f'{book.title},', end=' ')
print(f'published in {book.year_published},', end=' ')
print(f'{book.num_chapters} chapters')

###########################################################################

class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

rect1 = Rectangle()
rect1.length = int(input())
rect1.width = int(input())

''' Your code goes here '''
total_perimeter = 2 * (rect1.length + rect1.width)

print(f'Total perimeter: {total_perimeter}')

###########################################################################
'''
Define a class named StudentData that contains the attributes age, credit_hr, and birthplace. 
Initialize age and credit_hr with 0 and initialize birthplace with 'unknown'.
'''

''' Your code goes here '''
class StudentData:
  def __init__(self):
    self.age = 0
    self.credit_hr = 0
    self.birthplace = 'unknown'

student = StudentData()

print('Student data (before):', end=' ')
print(f'{student.age} years old,', end=' ')
print(f'{student.credit_hr} credits,', end=' ')
print(f'{student.birthplace}')

student.age = int(input())
student.credit_hr = int(input())
student.birthplace = input()

print('Student data (after):', end=' ')
print(f'{student.age} years old,', end=' ')
print(f'{student.credit_hr} credits,', end=' ')
print(f'{student.birthplace}')