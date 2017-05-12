def view_event():

	bootcamp={'Alice': {
            'phone': '2341',
            'addr': '87 Eastlake Court'
            },

        'Beth': {
            'phone': '9102',
            'addr': '563 Hartford Drive'
            }}
	#Checks if there are any upcoming events
	if len(bootcamp) > 0 :
		#If there are events pulls all events and displays them to the user
		for boot in bootcamp:
			for j in bootcamp[boot]:
				for k in bootcamp[boot][j]:
				  print(k, end ="" )
	else :
		print("There are no upcoming events")
view_event()
