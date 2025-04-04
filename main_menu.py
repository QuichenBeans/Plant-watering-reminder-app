import json
from datetime import datetime


class Menu:
    def __init__ (self):
        self.saved_data = {}
        self.current_user = None
        self.current_plant = None

    def app_start(self):
        print("Welcome to the plant watering app")
        self.user_email()

    def main_menu(self):
        print("Please enter your choice between 1 and 8")
        print("1. Add your plants!")
        print("2. Enter when the plant was last watered")
        print("3. Check when a plant was last watered")
        print("4. Delete plant")
        print("5. Delete email address")
        print("6. Change your email address")
        print("7. Show saved data (plants and emails)")
        print("8. Exit")
    
        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                self.user_plant()
            elif choice == "2":
                self.input_last_watered_date()
            elif choice == "3":
                self.check_last_watered()
            elif choice == "4":
                self.delete_plant()
            elif choice == "5":
                self.delete_email()
            elif choice == "6":
                self.alter_email()
            elif choice == "7":
                self.show_saved_data()
            elif choice == "8":
                print("Exit")
                break
            else:
                print("Invalid choice")
    
    def user_email(self):
        self.current_user = input("To get started, please enter your email address:  ")
        if self.current_user in self.saved_data:
            print(f"This user already exists, welcome back {self.current_user}")
            self.main_menu()
        else:
            print(f"Welcome {self.current_user}")
            self.saved_data[self.current_user] = {}
            self.saved_plants()
        self.main_menu()

    def user_plant(self):
        self.current_plant = input("Please enter the plant name:  ")
        self.add_to_dict(self.saved_data, self.current_user, self.current_plant)
        print(f"Thank you, your plant {self.current_plant} have been added")
        
    def add_to_dict(self, saved_data, current_user, current_plant):
        if current_user in saved_data:
            if current_plant in saved_data[current_user]:
                ask_overwrite = input("A plant with that name already exists, do you still want to overwrite it? If you choose to overwrite it will remove existing data on that plant. Please answer 'yes' or 'no'.  ")
                if ask_overwrite.lower() == 'yes':
                    saved_data[current_user][current_plant] = None
                    self.saved_plants()
                else:
                    return  
            else:
                saved_data[current_user][current_plant] = None
                self.saved_plants()
        else:
            saved_data[current_user] = {current_plant : None}
            self.saved_plants()

    def check_last_watered(self):
        self.current_plant = input("Please enter the plant you wish to check:  ")
        if self.current_user in self.saved_data:
            if self.current_plant in self.saved_data[self.current_user]:
                last_watered = datetime.fromtimestamp(self.saved_data[self.current_user][self.current_plant])
                formatted_date = last_watered.strftime("%d/%m/%Y")
                print(f"The last watered date for '{self.current_plant}': {formatted_date}")

    def input_last_watered_date(self):
        self.current_plant = input("Please enter the name of the plant to update when it was last watered:  ")
        if self.current_plant in self.saved_data[self.current_user]:
            user_watered = input("Please enter the date you last watered the plant (Please enter the date format as 'DD/MM/YYYY'):  ")
            date_format = "%d/%m/%Y"
            parsed_date = datetime.strptime(user_watered, date_format)
            time_stamped = datetime.timestamp(parsed_date)
            self.saved_data[self.current_user][self.current_plant] = time_stamped
            self.saved_plants()
            print(f"Last watered date for {self.current_plant} has been updated.")
        else:
            print("This plant does not exist, please re-enter option 2 to try again.")

    def delete_plant(self):
        self.current_plant = input("Enter the name of the plant you want to delete: ")
        if self.current_plant in self.saved_data[self.current_user]:
            del self.saved_data[self.current_user][self.current_plant]
            print(f"The {self.current_plant} plant has been deleted from {self.current_user}")
        else:
            self.current_plant not in self.saved_data[self.current_user]
            print("The plant does not exist in the dictionary")
        self.saved_plants()

    def alter_email(self):
        if self.current_user in self.saved_data:
            new_email = input("Enter the new email address you'd like to use:  ")
            self.current_user = new_email
            self.add_to_dict(self.saved_data, self.current_user, self.current_plant)
            print(f"Thank you, you email has been updated to {new_email}")
        else:
            print("This email does not exist, please try again.")

    def delete_email(self):
        self.current_user = input("Enter the email address you want to delete: ")
        if self.current_user in self.saved_data:
            del self.saved_data[self.current_user]
            print(f"The {self.current_user} email address has been deleted")
        else:
            print("The email address does not exist in the dictionary")
        self.saved_plants()

    def saved_plants(self):
        try:
            with open ("stored_data.json", "r") as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = {}
        existing_data.update(self.saved_data)
        with open("stored_data.json", "w") as file:
            json.dump(self.saved_data, file, indent = 4) 

    def show_saved_data(self):
        with open("stored_data.json", "r") as file:
            json_data = json.load(file)
            print("Saved data:  ")
            for user, plants in json_data.items():
                print(f"User: {user}")
                for plant, timestamp in plants.items():
                    if timestamp:
                        formatted = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y")
                        print(f" - {plant}: last watered on {formatted}")
                    else:
                        print(f" - {plant}: Not watered yet")

 
        
# if __name__ == '__main__':
#     my_menu = Menu()
#     my_menu.app_start()


