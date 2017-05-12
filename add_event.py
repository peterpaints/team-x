def add_event(bootcamp):
	event = input("enter calender name:")
	event_number = input("Enter event number:")
	todo = input("Enter event:")
	bootcamp[event][event_number] = todo

	return bootcamp




	