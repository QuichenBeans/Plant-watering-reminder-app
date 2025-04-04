import time
from email_notifs import all_email_func
from main_menu import Menu
# import RPi.GPIO as GPIO



# The grow hat will send pulses as a Hz value between 0 and 30, the lower the number the wetter, the highter the dryer
# I want to track in real time when the plant was watered and store that date into the json to access later

# What happens when the plant's moisture is read by the pi:
    # The sensors will detect the moisture of the plant's soil if it is above 20hz (hits the dry threshold) it will trigger an email to be sent to the user
    # The user will water the plant and update the 3rd option in the menu giving a date when it was watered
        # If the user does not water the plant and the function tracked_moisture continues to ping that the plant is still dry it will send the user another email
        # (Could make another function that has stronger wording)

# To do off the above notes:
    # Make a tracked moisture function that will track the moisture of plants using the pi sensors - it will track between wet threshold 10 and dry 20
    # Another email function that will send another email if the user decides not to water the plant of the day of the first reminder
    # Consider tying tracked_moisture function in with the date the reminder email is sent 
        # for example the moisture tracking pings that the plant is dry so an email is sent out and the user waters the plant - if the user actually watered the plant
        # the tracked moisture would become more wet which then would update the last_watered function and the value of that stored in the dict



class MoistureTracker:

    def __init__(self, current_user, saved_data={}):
        self.saved_data = saved_data 
        self.dry_value = 0.85
        self.wet_value = 0.15
        self.dry_threshold = 50
        self.current_user = current_user
        self.current_plant = None
        self.sensor_count = 3
        # self.gh = grow_hat 

    def read_sensor(self, sensor_index):
        if sensor_index not in range(self.sensor_count):
            raise ValueError("Use sensor index of 0, 1, or 2")
        return self.gh.moisture[sensor_index]

    def read_moisture(self, sensor_index):
        raw = self.read_sensor(sensor_index)
        percent = 100 * (1 - raw - self.wet_value) / (self.dry_value - self.wet_value)
        return max(0, min(100, percent))
    
    def check_plants(self):
        for i in range(self.sensor_count):
            self.current_plant(i)
            moisture = self.read_moisture(i)
            need_water = moisture < self.dry_threshold
            if need_water:
                self.check_and_send_alert(self.current_plant)

    def check_and_send_alert(self, saved_data):
        last_alert = saved_data.get(self.current_user,{}).get(self.current_plant)
        if time.time() - last_alert < 3600:
            return
        self.send_email_alert()

    def send_email_alert(self):
        all_email_func()


test = MoistureTracker(current_user)
test.email_details(current_user)

    
        



    
                                    
    
