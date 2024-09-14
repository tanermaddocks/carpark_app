class Carpark:
    def __init__(self, name):
        self.name = name
        self.slots = []

    def add_slot(self, slot):
        self.slots.append(slot)