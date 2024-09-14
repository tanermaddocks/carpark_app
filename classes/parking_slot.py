class ParkingSlot:
    def __init__(self, id):
        self.id = id
        self.car = None
    
    def add_car(self, car):
        if self.car:
            return False
        else:
            self.car = car
            return True

    def __str__(self):
        return f"Parking slot with id {self.id} and has the following car: {self.car}" if self.car else f"Parking slot with id {self.id}" # may have issue
    
