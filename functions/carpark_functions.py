from classes.parking_slot import ParkingSlot
from classes.car import Car

def add_slot(carpark):
    #input id of the parking slot
    slot_id = input ("Enter the id for the parking slot: ")
    #create an instance of the parking slot
    parking_slot = ParkingSlot(slot_id)
    #add that instance to the carpark
    carpark.add_slot(parking_slot)
    print ("Parking Slot Added")

def delete_slot(carpark):
    #take input the id of the parking slot
    slot_id = input ("Enter the id of the parking slot: ")
    #delete the parking slot
    print("Parking slot deleted.") if carpark.delete_slot(slot_id) else print("No parking spot with that id.") 

def list_slots(carpark):
    all_slots = carpark.get_slots()
    print("Listing slots...")
    if not all_slots:
        print ("No slots found.")
    for slot in all_slots:
        print (slot)

def park_car(carpark):
    #take input car rego
    reg_no = input("Enter the registration number of the car: ")
    #take input parking slot id
    slot_id = input("Enter the id of the parking slot: ")
    #find the parking slot
    slot_to_park =  carpark.find_slot(slot_id)
    if slot_to_park:
        # create an instance of the car with rego
        car_to_park = Car(reg_no)
        # add the car to the parking slot
        if slot_to_park.add_car(car_to_park):
            print("Car parked successfully")
        else:
            print("Car already parked in the slot")
    else:
        print("Slot with that id does not exist")