"""
A command line calendar
author: Dezhi Zhao
date: 08/28/2017
"""
from time import sleep, strftime
USER_NAME = "ROGER"
calendar = {}

#welcome function
def welcome():
  print "Welcome, " + USER_NAME + "."
  print "The calendar is opening."
  sleep(1)
  print "Today is: " + strftime("%A %b %d, %Y")
  print strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"

#the basic function of calendar
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "The calendar is empty!"
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date? (MM/DD/YYYY) ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "Invalid input of date!"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_agian.upper()
        if try_agian == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Event was added successfully!"
        print calendar
    elif user_choice == "D":
      if calendar.keys() < 1:
        print "Calendar is empty!"
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if calendar[date] == event:
            del calendar[date]
            print "Event was deleted successfully!"
            print calendar
          else:
            print "Error! Can not find the event!"
    elif user_choice == "X":
      start = False
    else:
      print "Invalid command!"
      start = False
      
start_calendar()
