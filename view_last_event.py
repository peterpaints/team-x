def view_last_event():

	bootcamp= {"""'Alice': {
            'phone': '2341',
            'addr': '87 Eastlake Court'
            },

        'Beth': {
            'phone': '9102',
            'addr': '563 Hartford Drive'
            }"""}
	#Checks if there are any upcoming events
	if len(bootcamp) > 0 :
		#If there are events pulls the last event and displays it to user
		print(format(bootcamp.popitem()))
	else :
		print("There are no upcoming events")
view_last_event()