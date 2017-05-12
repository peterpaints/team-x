import sys
from collections import OrderedDict

bootcamp = {}

def create_calendar():
    name = input("Please input a name for your calendar, eg. Week 1: ")
    bootcamp[name] = {}
    return bootcamp


def add_event():
    if len(bootcamp) < 1:
        print ("")
        print ("There are no calendars yet. Please add a calendar!")
        print ("")
    else:
        readable = {k: " ".join(v.keys()) for v in bootcamp.values() for k, v in bootcamp.items()}
        readable = OrderedDict(sorted(readable.items()))

        print ("Here are your current calendars ...")
        print('\n'.join("{}: {}".format(k, v) for k, v in readable.items()))

        event = input("Select a calendar to edit by typing it as it appears in the list above: ")
        if event not in bootcamp:
            print ("There is no such calendar! ")
        else:
            print ("")
            print ("You've selected %s" % (event))
            print ("")
            print ("Let's add some To Dos!")
            print ("")
            event_number = input("Enter To Do number, e.g. 1: ")
            print ("")
            todo = input("Enter To Do, e.g. Learn Git: ")
            print ("")
            bootcamp[event][event_number] = todo

            return bootcamp

def view_event():
    if len(bootcamp) > 0 :
        for boot in bootcamp:
            for j in bootcamp[boot]:
                for k in bootcamp[boot][j]:
                    print (k, end ="" )
    else:
        print("There are no upcoming events")


def view_last_event():
	#Checks if there are any upcoming events
	if len(bootcamp) > 0 :
		#If there are events pulls the last event and displays it to user
		print(format(bootcamp.popitem()))
	else :
		print("There are no upcoming events")


def welcome_page():
    print("")
    print("")
    print("BOOTCAMP ACTIVITIES TRACKER!")
    print("")
    print("")
    print("WELCOME!")
    print("")
    print("")

    while True:

        print("1. Create a New Calendar")
        print("2. Add event to a calendar")
        print("3. View list of events on a calendar")
        print("4. View last event on a calendar")
        print("5. Exit the app")

        print("")
        print("")
        user = input("Enter a number, eg. 1 to perform an action: ")
        if user == "1":
            create_calendar()
        elif user == "2":
            add_event()
        elif user == "3":
            view_event()
        elif user == "4":
            view_last_event()
        elif user == "5":
            sys.exit()
        else:
            print("Invalid input!")
            user = input("Enter a number, eg. 1 to perform an action: ")


if __name__ == "__main__":
    welcome_page()
