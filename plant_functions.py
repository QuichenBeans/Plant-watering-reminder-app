import datetime
import dateutil.relativedelta as relativedelta
from main_menu import Menu




if __name__ == "__main__":
    saved_data = {}
    menu = Menu(saved_data)
    menu.main_menu()
   
    

# Think about a function that informs the user when the plant was last watered. This will check if the tracked moisture level has increased
# if it has print the date it was watered on. If not, the user is a shitter and hasn't watered their plants - print a message about watering
# but it will track the moisture level of the plant if it increases or decreases.
# If the value decrease (more moisture) we can inform the user that the plant doesn't need watering
# The function will record the last watered date of the plant and store it in the :value of the nested dictionary - should 
# include if the plants moisture hasn't gotten wetter since the email reminder was sent out advice them to water the plant (maybe ask
# if they could then enter the date of watering? Can then store that in the nest dict value)
# Write a tracked moisture function - tracks the moisture movements to check to see if the user watered the plant (track the changes
# over something less than 5 out of the 30hz)


# def last_watered():
    

# def track_moisture():






# Once moisture reaches a low level (whatever level we decided on) it will ping the user with a message reminding them to water the plant
# this message of reduced moisture will be passed into the last_time_watered function
# this will then compare the date the plant was last watered with the current date
# If the user waters the plant, the date will be updated to the current date - use if statement and 
# evaluate as True or False depending on if the plant was watered on that date
# If the user does not water the plant, the date will remain the same and the user will continue to receive reminders - think while loop
def is_moisture():
    moisture_detection = 100
    while moisture_detection >= 80:
        print("The plant has moisture")
        break
    else:
        print("The plant needs watering")


