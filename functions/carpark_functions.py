from classes.parking_slot import ParkingSlot

def add_slot(carpark):
    #input id of the parking slot
    slot_id = input ("Enter the id for the parking slot: ")
    #create an instance of the parking slot
    parking_slot = ParkingSlot(slot_id)
    #add that instance to the carpark
    carpark.add_slot(parking_slot)
    print("Parking Slot Added")

def list_slots(carpark):
    all_slots = carpark.get_slots()
    print("\nListing slots...")
    if not all_slots:
        print ("No slots found.")
    for slot in all_slots:
        print (slot)