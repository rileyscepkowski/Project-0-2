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

# Function to search for a specific vehicle
def search_vehicle():
  print("Please Enter the full Vehicle name:")
  search_query = input().strip()

  if search_query in AllowedVehiclesList:
    print(f"{search_query} is an authorized vehicle.")
  else:
    print(f"{search_query} is not an authorized vehicle, if you received this in error please check the spelling and try again")

# Function to display the menu and get user input
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")
    print("********************************")


# Main Program Function
def main():
  while True:
    display_menu() #show menu
    user_choice = input() # get user input

    if user_choice == '1':
      print_vehicles()
    elif user_choice == '2':
      search_vehicle()
    elif user_choice == '3':
      print("Thank you for using AutoCountry Vehicle Finder, goodbye!")
      break # end else/if loops
    else:
      print("Invalid choice, please try again.")

if __name__ == "__main__":
    main() # run the main function