"""
def begin():

	park_choice = input("Do you want to go to the park?\n").lower().strip()
	if park_choice == 'yes' or park_choice == 'yeah' or park_choice == 'y':
		print("Hooray!")
	elif park_choice == 'no':
		print("Ok. I didn't want to go anyway")
	else:
		print("Ok.")

begin()
"""

def begin():
	dogWalk = input("You're dog looks like he wants to go outside. Do you go out or stay inside?\n")
	if "out" in dogWalk:
		print("you go outside.")
		dogEscapes()
	else:
		print("your dog looks sad.")

begin()
def dogEscapes():
	escape? = input("Your dog gets free of his leash. Do you chase him or call him to you?\n")
	if "call" in response:
		print("he turns around and runs back towards you. that was a close call.")
	else:
		print("he starts to run faster. He runs into somebody's back yard, but when you look for him, he is gone.")