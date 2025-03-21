import json
import datetime
import dateutil.relativedelta as relativedelta
from email_notifs import all_email_func
# import RPi.GPIO as GPIO


# The grow hat will send pulses as a Hz value between 0 and 30, the lower the number the wetter, the highter the dryer
# I want to track in real time when the plant was watered and store that date into the json to access later
# Work out how to nest a new dictionary into the list of values i.e {email:{bonsai:14/03/2025}}
# In the above example, email is the key of the first dictionary and the new dictionary is the value of the first dictionary
# Inside this dictionary the name of the plant i.e 'bonsai' is the key and the value is the date when the plant was watered 


class Moisture:

    def __init__(self):
        self.moisture_level = 0
        self.dry_threshold = 20
        self.wet_threshold = 10
        self.wet_point = 3
        self.dry_point = 25
        self.called = False
        times = []

    def read_moisture(self):
        self.moisture_level = 0
        return self.moisture_level
    
    def convert_to_percent(self):
        float_value = self.read_moisture
        print("{:.2%}".format(float_value))

    # def dry_point(self):
    #     self.moisture_level <= self.dry_point

    # def wet_point(self):
    #     self.moisture_level >= self.wet_point

    def run_program(self):
        while True:
            moisture_reading = self.read_moisture
            if moisture_reading >= self.moisture_threshold:
                all_email_func() # Send email - need to work out how to incorporate the info stored in the dictionary
            else:
                print("The plant does not need watering")
            break



    def plant_watered(self):
        if self.moisture_level <= 17:


        



    def plant_watered_data(self):
        with open("stored_data.json", "w") as file:
            json.dump(self.times, file, indent = 4)


    def last_watered_date(self):
        if all_email_func() 

        if self.read_moisture >= self.moisture_threshold:
            no_moisture = self.read_moisture >= self.moisture_threshold
            if no_moisture < :
                current_date = datetime.today().strftime('%Y-%m-%d')
                delta = current_date - no_moisture
                print(f"The plant was watered {delta} of days ago") # Need to work out how to get the date when the plant got too dry
        else:
            print(f"There is currently {self.convert_to_percent}% moisture in your plant, so it doesn't need watering yet")                                            

    
def plant_moisture():
    soil_moisture = Moisture
    soil_moisture.read_moisture 
    soil_moisture.run_program

plant_moisture()
    
