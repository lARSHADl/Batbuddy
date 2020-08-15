import psutil
import time
import requests

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = int(battery.percent)
count = 0
low_val = 20
up_val = 81


def monitor():
    while True:
      time.sleep(10)

      if percent <= low_val:
         val = requests.post('http://192.168.43.36/control?cmd=GPIO,5,1')
         print("Cahrger powered On")

      if percent >= up_val:
         val = requests.post('http://192.168.43.36/control?cmd=GPIO,5,0')
         print("Charger power off")



if __name__ == "__main__":
   monitor()