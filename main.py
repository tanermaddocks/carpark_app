from colored import Fore, Back, Style
from classes.carpark import Carpark
from functions.carpark_functions import add_slot, delete_slot, list_slots, park_car
from functions.file_functions import save_and_exit, load_from_file

print(f"{Fore.yellow}{Back.red}Welcome to the Carpark Application!!!{Style.reset}")

def create_menu ():
    print ("\nEnter 1 to add a parking slot.")
    print ("Enter 2 to delete a parking slot.")
    print ("Enter 3 to list all parking slots.")
    print ("Enter 4 to park a car.")
    print ("Enter 5 to find a parked car.")
    print ("Enter 6 to remove a car from the carpark.")
    print ("Enter 7 to exit the application.\n")

    choice = input ("Enter your choice: ")
    return choice

choice = ""

carpark = Carpark("Carparker")

load_from_file(carpark)

while choice != "7" :
    choice = create_menu()
    match choice:
        case "1":
            add_slot(carpark)
        case "2":
            delete_slot(carpark)
        case "3":
            list_slots(carpark)
        case "4":
            park_car(carpark)
        case "5":
            print ("Find car")
        case "6":
            print ("Exit carpark")
        case "7":
            save_and_exit(carpark)
        case _:
            print ("Invalid choice")

print ("\nThank you for using the Carpark Application.")