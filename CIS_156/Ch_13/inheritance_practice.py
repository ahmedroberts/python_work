class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print('Moving at: ', end = '')
        self.print_speed()


myCar = Car()
myCar.set_speed(35)
myCar.print_car_speed()

print('\n----------------------------------\n')

class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print('Speed: ', end = '')
        self.print_speed()


class AnimalPowered(Vehicle):
    def __init__(self):
        self.animal = ''

    def set_animal(self, animal_to_set):
        self.animal = animal_to_set

    def print_animal_speed(self):
        print(f'{self.animal} speed: ', end = '')
        self.print_speed()


myCar = Car()
chariot = AnimalPowered()

myCar.set_speed(30)
chariot.set_speed(12)
chariot.set_animal('Camel')

myCar.print_car_speed()
chariot.print_animal_speed()