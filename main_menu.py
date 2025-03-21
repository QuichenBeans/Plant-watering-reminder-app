import json
from datetime import datetime
# from email_notifs import all_email_func
# from moisture_sensor import Moisture


class Menu:
    def __init__ (self, saved_data):
        self.saved_data = saved_data

    def main_menu(self):
        print("Welcome to the plant watering app")
        print("1. Add your email, plants and when the plants were last watered")
        print("2. Add plants to an existing email")
        print("3. Enter when the plant was last watered")
        print("4. Check when a plant was last watered")
        print("5. Delete plant")
        print("6. Delete email address")
        print("7. Show saved data (plants and emails)")
        print("8. Exit")
    
        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                self.user_input()
            elif choice == "2":
                self.add_to_existing_email()
            elif choice == "3":
                self.input_last_watered_date()
            elif choice == "4":
                pass
            elif choice == "5":
                self.delete_plant()
            elif choice == "6":
                self.delete_email()
            elif choice == "7":
                self.show_saved_data()
            elif choice == "8":
                print("Exit")
                break
            else:
                print("Invalid choice")
            

    def user_input(self):
        user_email = input("Please enter your email address:  ")
        plant_name = input("Please enter the plant name:  ")
        self.add_to_dict(self.saved_data, user_email, plant_name)
        self.input_last_watered_date(user_email, plant_name)
        print(f"Thank you, your email {user_email} and plant {plant_name} have been added")

    def add_to_existing_email(self):
        user_email = input("Please enter the existing email you want to add plants to: ")
        if user_email in self.saved_data:
            new_plant = input("Please enter the plant you want to add: ")
            self.add_to_dict(self.saved_data, user_email, new_plant)
            print(f"Your {new_plant} has been added to the {user_email} email address")
        # Need to add to this function so that when the user enters the new plant, they can also enter the date they 
        # last watered the new plant
        
    def add_to_dict(self, dictionary, user_email, plant_name):
        if user_email in dictionary:
            if plant_name in dictionary[user_email]:
                ask_overwrite = input("A plant with that name already exists, do you still want to overwrite it? If you choose to overwrite it will remove existing data on that plant. Please answer 'yes' or 'no'.  ")
                if ask_overwrite.lower == 'yes':
                    dictionary[user_email][plant_name] = None
                elif ask_overwrite.lower == 'no':
                    self.saved_plants()
            else:
                dictionary[user_email][plant_name] = None
        else:
            dictionary[user_email] = {plant_name : None}
        self.saved_plants()

    def check_last_watered(self, user_email):
        plant_check = input("Please enter the plant you wish to check:  ")
        if user_email in self.saved_data:
            if plant_check in self.saved_data[user_email]:
                print(f"The last watered date for '{plant_check}': {self.saved_data[user_email][plant_check]}")
    # Need to add the conversion of the unix time stamp that's stored in the dictionary back into a readable format for the user        


    def input_last_watered_date(self, user_email, plant_name):
        date_format = "%d/%m/%Y"
        user_watered = input("Please enter the date you last watered the plant (Please enter the date format as 'DD/MM/YYYY'):  ")
        parsed_date = datetime.strptime(user_watered, date_format)
        time_stamped = datetime.timestamp(parsed_date)
        self.saved_data[user_email][plant_name] = time_stamped
        self.saved_plants()

    def delete_plant(self):
        user_email = input("Please enter the email address you want to delete the plant from: ")
        del_plant = input("Enter the name of the plant you want to delete: ")
        if user_email in self.saved_data and del_plant in self.saved_data[user_email]:
            del self.saved_data[user_email][del_plant]
            print(f"The {del_plant} plant has been deleted from {user_email}")
        elif del_plant not in self.saved_data[user_email]:
            print("The plant does not exist in the dictionary")
        else:
            print("The email address does not exist in the dictionary")
        self.saved_plants()

    def delete_email(self):
        del_email = input("Enter the email address you want to delete: ")
        if del_email in self.saved_data:
            del self.saved_data[del_email]
            print(f"The {del_email} email address has been deleted")
        else:
            print("The email address does not exist in the dictionary")
        self.saved_plants()

    def saved_plants(self):
        with open("stored_data.json", "w") as file:
            json.dump(self.saved_data, file, indent = 4) 

    def show_saved_data(self):
        with open("stored_data.json", "r") as file:
            self.saved_data = json.load(file)
            print("Plant dictionary: ", self.saved_data)

    

        

my_menu = Menu(saved_data = {})
my_menu.main_menu()

