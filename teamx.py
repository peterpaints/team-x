import sys


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
