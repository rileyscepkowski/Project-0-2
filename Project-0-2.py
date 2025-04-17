 # List of authorized vehicles
AllowedVehiclesList = [
  'Ford F-150',
    'Chevrolet Silverado',
    'Tesla Cybertruck',
    'Toyota Tundra',
    'Nissan Titan',
 ]

#Function to print the list of vehicles
def print_vehicles ():
 print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
 for vehicle in AllowedVehiclesList:
  print(vehicle)

# Function to display the menu and get user input
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

# Main Program Function
def main():
  while True:
    display_menu() #show menu
    user_choice = input() # get user input

    if user_choice == '1':
      print_vehicles()
    elif user_choice == '2':
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!") # exit message
      break # close program

    else:
        print("Invalid choice, please try again.") # invalid input message

if __name__ == "__main__":
    main() # run the main function