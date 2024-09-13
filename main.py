print ("Welcome to the Carpack Application.\n")

def create_menu ():
    print ("Enter 1 to add a parking slot.")
    print ("Enter 2 to delete a parking slot.")
    print ("Enter 3 to list all parking slots.")
    print ("Enter 4 to park a car.")
    print ("Enter 5 to find a parked car.")
    print ("Enter 6 to remove a car from the carpark.")
    print ("Enter 7 to exit the application.\n")

    choice = input ("Enter your choice: ")
    return choice

choice = ""
while choice != "7" :
    choice = create_menu()

print ("Thank you for using the Carpark Application.")