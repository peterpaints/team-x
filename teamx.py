import sys
from collections import OrderedDict

# bootcamp = {}
bootcamp = []
dicbootcamp = {}

def create_calendar():
    name = input("Please input a name for your calendar, eg. Week 1: ")
    name = name.lower()
    dicbootcamp[name]= {}
    # bootcamp[name] = {}
    bootcamp.append(dicbootcamp)
    return bootcamp


def add_event():
    if len(bootcamp) < 1:
        print ("")
        print ("There are no calendars yet. Please add a calendar!")
        print ("")
    else:
        # readable = {k: " ".join(v.keys()) for v in bootcamp.values() for k, v in bootcamp.items()}
        # readable = OrderedDict(sorted(readable.items()))

        print ("Here are your current calendars ...")
        calendar_items = []
        for calendar in bootcamp:
            for item in calendar:
                print (item.title())
                calendar_items.append(item)
        # print('\n'.join("{}: {}".format(k, v) for k, v in readable.items()))

        event = input("Select a calendar to edit from the list above by typing it in: ")
        event = event.lower()

        if event not in calendar_items:
            print ("There is no such calendar! ")
        else:
            print ("")
            print ("You've selected %s" % (event.title()))
            print ("")
            print ("Let's add some To Dos!")
            print ("")
            event_number = input("Enter To Do number, e.g. 1: ")
            print ("")
            todo = input("Enter To Do, e.g. Learn Git: ")
            print ("")
            for calendar in bootcamp:
                for item in calendar:
                    if item == event:
                        calendar[item][event_number] = todo

            return bootcamp

def view_event():
    if len(bootcamp) > 0 :
        print(bootcamp)
        """for boot in bootcamp:
            for j in bootcamp[boot]:
                # for k in bootcamp[boot][j]:
                    print (j, end ="" )"""
    else:
        print("There are no upcoming events")


def view_last_event():
    if len(bootcamp) > 0:
        print (bootcamp[-1])
    else:
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
