'''
Set course_student's last_name to Smith, age_years to 20, and id_num to 9999.

Sample output for the given program:
Name: Smith, Age: 20, ID: 9999
'''
class PersonData:
    def __init__(self):
        self.last_name = ''
        self.age_years = 0

    def set_name(self, user_name):
        self.last_name = user_name

    def set_age(self, num_years):
        self.age_years = num_years

    # Other parts omitted

    def print_all(self):
        output_str = f'Name: {self.last_name}, Age: {self.age_years}'
        return output_str


class StudentData(PersonData):
    def __init__(self):
        PersonData.__init__(self)  # Call base class constructor
        self.id_num = 0

    def set_id(self, student_id):
        self.id_num = student_id

    def get_id(self):
        return self.id_num


course_student = StudentData()

''' Your solution goes here '''
course_student.last_name = "Smith"
course_student.age_years = 20
course_student.id_num = 9999
''' Your solution ends here '''

print(f'{course_student.print_all()}, ID: {course_student.get_id()}')