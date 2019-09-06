"""Ian Haile
9/6/19
this program has a conversation with this user
Sources: https://www.geeksforgeeks.org/string-find-python/
OMH
"""

response = input("Hello! How are you doing today?\n\n")
if(response.find('?') != -1): #a common reply is something like "Good, and you?". checking for a ? determines wether the user asked the computer how it is doing
	print("\nI'm doing well, thanks!")
else:
	print("\nThat's great to hear!")
response = input("\nAre you doing anything fun today?\n\n")
if(response.find('no') == 0): #checks if the user says no
	print("\nThat's too bad.")
else: 
	if(response.find('yes') != -1 & response.find(' ') == -1): #checks if the user says yes, and doesn't elaborate with other words
		response = input("\nWhat are you doing?\n\n")
		print("\n" + response + "? That sound really fun!")
	else: 
		print("\n That sounds like a lot of fun!")
response = input("\nWhat classes do you have today?\n\n")
if (response.find("don't") != -1 or response.find("none") != -1): #checks if you hace no classes
	print("\nIt's nice to have some time to relax!\n")
else: 
	classes = response.split() #this is to use only one word from the string
	print("\n" + classes[0] + "! That's my favorite!\n") #gets the first word said
print("\nI have to go now, it was great talking to you!\n")