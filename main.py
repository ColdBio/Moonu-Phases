import rumps
import py2app
import time
import math
import numpy as np
from datetime import datetime
from time import strftime
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

datetime_now = datetime.now() +  timedelta(days=-10)
todays_date = datetime_now.date()
current_month = strftime('%B')
final_date = None

lunar_days = 29.53058770576
lunar_secs = lunar_days * (24 * 60 * 60)


current_unixtime = time.mktime(todays_date.timetuple())
new2000 = 947182440 
totalsecs =   current_unixtime - new2000 
x = math.fmod(totalsecs, lunar_secs)

if x < 0:
    x += lunar_secs

current_frac = x / lunar_secs
current_days = current_frac * lunar_days

print(current_frac)
print(f"Day: {current_days}")
print(datetime_now)
print(current_unixtime)
print("--------------------------------")


def find_phase(value):
    if 0.0 <= value <= 0.033863193308711:
        return "new"
        
    if 0.033863193308711 <= value <= 0.216136806691289:
        return "waxing_crescent"
    
    if 0.216136806691289 <= value <= 0.283863193308711:
        return "first_quarter"
    
    if 0.283863193308711 <= value <= 0.466136806691289:
        return "waxing_gibbous"
    
    if 0.466136806691289 <= value <= 0.533863193308711:
        return "full"
    
    if 0.533863193308711 <= value <= 0.716136806691289:
        return "waning_gibbous"
    
    if 0.716136806691289 <= value <= 0.783863193308711:
        return "last_quarter"
    
    if 0.783863193308711 <= value <= 0.966136806691289:
        return "waning_crescent"
    
    if 0.966136806691289 <= value <= 1.0:
        return "new"

phase = find_phase(current_frac)

all_phases = {
    "new": "🌑",
    "waxing_crescent": "🌒",
    "first_quarter": "🌓",
    "waxing_gibbous": "🌔",
    "full": "🌕",
    "waning_gibbous": "🌖",
    "last_quarter": "🌗",
    "waning_crescent": "🌘",
    "new": "🌑" 
}

todays_phase = ""

for key, value in all_phases.items():
    if phase == key:
        todays_phase = value

print(todays_phase)




rumps.debug_mode(True)

about_text = """

Author: ColdbBio
License: MIT License
Version: v1.0
Repository: https://github.com/ColdbBio/Moonu-Phases

""".center(20, "0")

class Moonu_Phases(object):
        def __init__(self):
            self.config = {
                "app_name": f"{todays_phase}",
                "About": "About"
            }

            self.app = rumps.App(self.config["app_name"])
            self.about_button = rumps.MenuItem(title=self.config["About"], callback=None)
            self.app.menu = [self.about_button]
        
        @rumps.clicked("About")
        def about(self):
            # ! MAKE SURE TO CHANGE THE FILE PATH NAME TO THE CORRECT ONE
            rumps.alert("Moonu Phases", f"{about_text}", "Close", icon_path="/Users/ColdBio/Documents/Python-Projects/Moonu App - Python/Waning_crescent_moon_emoji_icon_png_large.png")


        def run(self):
            self.app.run()

if __name__ == "__main__":
    app = Moonu_Phases()
    app.run()
