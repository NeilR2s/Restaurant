"""
INSTRUCTIONS:

The system will automatically initialize upon running. 
However, data types (including date, time, and integers)
should be strictly followed. 

Time format: "HH:MM AM/PM" (11:11 AM)
Date format: "MMM DD, YYYY" (October 25 2025)

"""
from datetime import datetime

class ReservationSystem:
    def __init__(self):
        self.reservations = []  # Storage for created reservations

    def filter_integer(self, int_check, zero_input=False):
        while True:
            try:
                integer_input = int(input(int_check))  # Check if input is integer
                if not zero_input and integer_input < 1:  # Validate non-zero values
                    raise ValueError("Value for this parameter must be at least 1.")
                return integer_input
            except ValueError:  # Catch non-integer inputs
                print("Invalid Input: Please enter a valid integer.")

    def filter_string(self, str_check): 
        while True: 
            str_input = input(str_check) # check if input is not blank
            
            if str_input:
                return str_input # did not catch special characters, as some usernames may have numbers or special characters
            else:
                print("Enter a valid string input. Name must not be blank")        

    def filter_date(self, date_check): 
        while True:
            date_input = input(date_check)
            try:
                valid_date = datetime.strptime(date_input, "%b %d, %Y") # converts from str to a formatted datetime type (if fail, improper input)
                if valid_date > datetime.now(): # catch cases of entering past dates
                    return valid_date.strftime("%b %d, %Y") # return str date if following specific formatting MMM DD, YYYY
                else:
                    print("The reservation date must be at least one day in advance")
            except ValueError:
                print("Enter a valid date format. Date format: 'MMM DD, YYYY' (October 25, 2025).")

    def filter_time(self, time_check):
        while True:
            time_input = input(time_check)
            try:
                valid_time = datetime.strptime(time_input, "%I:%M %p") # converts from str to a formatted datetime type
                return valid_time.strftime("%I:%M %p") # return str time if following specific formatting HH, MM, AM/PM
            except ValueError:
                print("Enter a valid time format. Time format: 'HH:MM AM/PM' (11:11 AM).")

    def view_reservations(self):
        if len(self.reservations) == 0: # catch case no reservation
            print("No reservations have been made.") 

        else:
            print("\n#   | Date       | Time | Name     | Adults | Children | Subtotal ") # medyo GUI
            print("-----------------------------------------------------------------------")
            for index, reservation in enumerate(self.reservations, start=1): # iterate through list, print dictionary elements per index
                print(f"{index:<3} | {reservation['date']:<10} | {reservation['time']:<7} | {reservation['name']:<10} | {reservation['adults']:<5} | {reservation['children']:<7} | PHP {reservation['subtotal']:<7}") # attempt at alignment

    def make_reservation(self):
        print("\n----- Make a Reservation -----") # assign filtered inputs to variable
        name = self.filter_string("Enter name: ")
        date = self.filter_date("Enter date of reservation (e.g., Oct 25, 2025): ")
        time = self.filter_time("Enter time of reservation (e.g., 11:11 AM): ")
        adults = self.filter_integer("Enter number of adults (at least 1): ", zero_input=False)
        children = self.filter_integer("Enter number of children (can be 0): ", zero_input=True)
        subtotal = (children * 300) + (adults * 500) # subtotal calculation based on rate
        reservation = { # append to dictionary
            "name": name,
            "date": date,
            "time": time,
            "adults": adults,
            "children": children,
            "subtotal": subtotal
        }
        self.reservations.append(reservation) # store data as dictionary in list
        print("Reservation made successfully!")

    def delete_reservation(self):
        if len(self.reservations) == 0: # catch case of deleting empty reservation
            print("No reservations to delete.")
            return 

        self.view_reservations() 

        try:
            index = self.filter_integer("Enter the reservation number to delete: ") - 1 # access reservation to delete by index, -1 because of base 1 label
            if index < 0 or index >= len(self.reservations): # catch index out of range error
                print("Invalid reservation number.")
            else:
                deleted = self.reservations.pop(index) # delete from list 
                print(f"Deleted reservation: {deleted['name']} on {deleted['date']} at {deleted['time']}")
        except ValueError:
            print("Invalid input. Please enter a valid reservation number.")

    def generate_report(self):
        if not self.reservations: # catch case no reservations to delete
            print("No reservations to report.")
            return

        self.view_reservations() 

        total_adults = sum(res["adults"] for res in self.reservations) # sum of values per specified column
        total_children = sum(res["children"] for res in self.reservations)
        total_grand = sum(res["subtotal"] for res in self.reservations)

        print(f"\nTotal number of Adults: {total_adults}") # display relevant totals
        print(f"Total number of Children: {total_children}")
        print(f"Grand Total: PHP {total_grand}")

    def exit_system(self):
        print("Exiting the reservation system. Thank you!")

    def system_menu(self): # access functions through user input
        actions = {
            "a": self.view_reservations,
            "b": self.make_reservation,
            "c": self.delete_reservation,
            "d": self.generate_report,
            "e": self.exit_system
        }

        while True:
            print("\nSystem Menu \na. View all Reservations\nb. Make Reservation\nc. Delete Reservation\nd. Generate Report\ne. Exit")
            letter = input("Choose an option (a-e): ").lower()

            if letter in actions:
                actions[letter]()
                if letter == "e":
                    break
            else:
                print("Invalid Input: Enter a letter between 'a' and 'e'.") # catch case where input outside a-e
            
            

reservation_system = ReservationSystem()
reservation_system.system_menu()

