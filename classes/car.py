from classes.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, registration_number):
        self.registration_number = registration_number

    def get_registration_number(self):
        return self.registration_number

    def __str__(self):
        return f"Car with registration {self.registration_number}"