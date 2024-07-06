##################################################################
class RaceTime:

    def __init__(self, start_hrs, start_mins, end_hrs, end_mins, dist):
        self.start_hrs = start_hrs
        self.start_mins = start_mins
        self.end_hrs = end_hrs
        self.end_mins = end_mins
        self.distance = dist

    def print_time(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        print(f'Time to complete race: {hours}:{minutes}')

    def print_pace(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        total_minutes = hours*60 + minutes
        print(f'Avg pace (mins/mile): {total_minutes / self.distance:.2f}')

distance = 5.0

start_hrs = int(input('Enter starting time hours: '))
start_mins = int(input('Enter starting time minutes: '))
end_hrs = int(input('Enter ending time hours: '))
end_mins = int(input('Enter ending time minutes: '))

race_time = RaceTime(start_hrs, start_mins, end_hrs, end_mins, distance)

race_time.print_time()
race_time.print_pace()

##################################################################
class Rectangle:
    def __init__(self, length=9, width=3):
        self.length = length
        self.width = width

rectangle1 = Rectangle(12, 7)
rectangle2 = Rectangle(11)
rectangle3 = Rectangle()

print(rectangle2.length)
print(rectangle1.length)
print(rectangle3.length)

##################################################################
class Rectangle:
    def __init__(self, color, length=3, width=5):
        self.color = color
        self.length = length
        self.width = width

rectangle1 = Rectangle('red', 5, 2)
rectangle2 = Rectangle('orange')
rectangle3 = Rectangle('blue', 9)

print(rectangle1.color)
print(rectangle1.width)
print(rectangle2.width)
print(rectangle3.width)

##################################################################
class Rectangle:
    def __init__(self, color, length=2, width=8):
        self.color = color
        self.length = length
        self.width = width

rectangle1 = Rectangle('red')
rectangle2 = Rectangle('pink', length=12, width=7)
rectangle3 = Rectangle('yellow', width=9, length=10)

print(rectangle1.length, rectangle1.width)
print(rectangle2.length, rectangle2.width)
print(rectangle3.length, rectangle3.width)

##################################################################
class PhonePlan:
    # FIXME add constructor

    ''' Your solution goes here '''
    def __init__(self, num_mins=0, num_messages=0):
        self.num_mins = num_mins
        self.num_messages = num_messages

    def print_plan(self):
        print(f'Mins: {self.num_mins}', end=' ')
        print(f'Messages: {self.num_messages}')


my_plan = PhonePlan(int(input()), int(input()))
dads_plan = PhonePlan()
moms_plan = PhonePlan(int(input()))

print('My plan...', end=' ')
my_plan.print_plan()

print('Dad\'s plan...', end=' ')
dads_plan.print_plan()

print('Mom\'s plan...', end= ' ')
moms_plan.print_plan()

##################################################################
class Passenger:
    def __init__(self, name, airport_code, plane_num):
        self.name = name
        self.airport_code = airport_code
        self.plane_num = plane_num

name1 = input()
airport_code1 = input()
plane_num1 = int(input())

''' Your code goes here '''
passenger1 = Passenger(name1, airport_code1, plane_num1)

print(f'passenger1 data: {passenger1.name}, flying to {passenger1.airport_code}, Flight #{passenger1.plane_num}')

##################################################################
class Profile:
    def __init__(self, status, username):

        ''' Your code goes here '''
        self.status = status
        self.username = username

status2 = input()
username2 = input()

profile1 = Profile('active', 'yellow-tortoise')
profile2 = Profile(status2, username2)

print(f'profile1 data: {profile1.status}, user {profile1.username}')
print(f'profile2 data: {profile2.status}, user {profile2.username}')

##################################################################
class Voicemail:

    ''' Your code goes here '''
    def __init__(self, name, number=0, greeting='Leave a message'):
        self.name = name
        self.number = number
        self.greeting = greeting

name2 = input()
number2 = int(input())
greeting2 = input()

default_voicemail = Voicemail('Ina')
voicemail2 = Voicemail(name2, number2, greeting2)

print(f"Default voicemail data: {default_voicemail.name}'s inbox, {default_voicemail.number}, {default_voicemail.greeting}")
print(f"voicemail2 data: {voicemail2.name}'s inbox, {voicemail2.number}, {voicemail2.greeting}")

##################################################################
class Profile:
    def __init__(self, location, status, username): 
        self.location = location
        self.status = status
        self.username = username

    def change_location(self, new_loc):
        self.location = new_loc

    def print_data(self):
        print(f'Profile data: located in {self.location}, {self.status}, user {self.username}')

location1 = input()
status1 = input()
username1 = input()
new_loc = input()

''' Your code goes here '''
profile1 = Profile(location1, status1, username1)

profile1.print_data()
profile1.change_location(new_loc)
profile1.print_data()

##################################################################
##################################################################