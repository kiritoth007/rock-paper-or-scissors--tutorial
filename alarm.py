import datetime
from playsound import playsound
alarm_hour = int(input("Enter hour: "))
alarm_minute = int(input("Enter minutes: "))
alarm_ap = input("am/pm: ")

if alarm_ap == "pm":
    alarm_hour += 12

while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute:
        print("Playing")
        playsound("C:/Users/Lenovo/Desktop/audio.mp3")
        break
