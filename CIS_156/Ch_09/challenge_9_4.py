##############################################################
class Weight:
    show_in_mg = True
      
    def __init__(self):
        self.value_in_g = 0
  
    def print_value(self):

        ''' Your code goes here '''
        if self.show_in_mg:
            print(f'Weight in milligrams: {self.value_in_g * 1000}')
        else:
            print(f'Weight in grams: {self.value_in_g}')
  
powder_weight1 = Weight()
powder_weight1.value_in_g = int(input())
print('First weight measurement:')
powder_weight1.print_value()

Weight.show_in_mg = False

powder_weight2 = Weight()
powder_weight2.value_in_g = int(input())
print('Second weight measurement:')
powder_weight2.print_value()

##############################################################
class CourseEnrollment:
    students_count = 0
    
    def __init__(self):
        self.student_name = 'empty'
        self.student_number = 0

    def setup(self, applicant_name):

        ''' Your code goes here '''
        CourseEnrollment.students_count += 1
        self.student_number = self.students_count
        self.student_name = applicant_name
        ''' Your code goes here '''
    
    def print_value(self):
        print(f"{self.student_name}'s student number is {self.student_number}.")

for applicant_name in input().split():
    new_student = CourseEnrollment()
    new_student.setup(applicant_name)
    new_student.print_value()
print(f'The course has {CourseEnrollment.students_count} students.') 
##############################################################


##############################################################