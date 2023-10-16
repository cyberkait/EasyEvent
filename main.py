# A simple program to create Outlook calendar events.


#imports
import win32com.client as win
import pyinputplus as pyip
from dateTools import enterDate
from dateTools import minsBetween
from timeTools import enterTime


# Getting info
print("Welcome to EasyEvent!")
name = input("What is the name of your event?").title()
startDate = enterDate("Enter the start date for your event: \n Example: May 17, 2007 or 12/25/1983 \n")
startTime = enterTime("Enter the start time for your event.")
sameDay = pyip.inputYesNo("Does your event end on the same day it starts?")
if sameDay == "no":
    endDate = enterDate("When does your event end?")
else:
    endDate = startDate
endTime = enterTime("What time does your event end?")
start = f"{startDate} {startTime}"
end = f"{endDate} {endTime}"
mins = minsBetween(end, start)
location = input("Where is your event?")

# Creating the object
print("Creating...")
outlook = win.Dispatch("Outlook.Application")
cal = outlook.CreateItem(1)
cal.Subject = name
cal.Start = startDate
cal.Duration = mins
cal.Location = location
cal.Save()


print("Your event has been created. \n Thanks for using EasyEvent! \n Goodbye.")