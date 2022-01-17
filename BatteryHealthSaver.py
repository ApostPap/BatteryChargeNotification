
#pip install psutil
#pip install win10toast

import time
import psutil
from win10toast import ToastNotifier

toast = ToastNotifier()

#Set the limits for sending the notification
# Suggested: Low limit at 25 and high limit at 80
low_limit = 25 
high_limit = 80
show_notif = False

check_every_x_secs=20




while True:
    battery = psutil.sensors_battery()
   
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("At :",current_time,"|| Battery percentage :", battery.percent,"|| Power plugged in :", battery.power_plugged)

    if (battery.percent >= high_limit and show_notif):
        toast.show_toast("Battery Health Saver","Battery at "+str(high_limit)+"%",duration=20,icon_path="battery-high.ico")
        show_notif = False
    elif (battery.percent <= low_limit and show_notif):
        toast.show_toast("Battery Health Saver","Battery at "+str(low_limit)+"%",duration=20,icon_path="battery-low.ico")
        show_notif = False
    elif (battery.percent > low_limit and battery.percent < high_limit):
        show_notif = True

    time.sleep(check_every_x_secs)





