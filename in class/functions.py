import math

def greet(user_name1, user_name2 = None user_name3 = None):
	if user_name2 == None:
		print("Hello, "+user_name1)
	elif user_name3 == none:
		print("Hello "+user_name1+" and "+user_name2+'!')
	else:
		print("Hello "+user_name1+", "+user_name2+", and "+user_name3+"!")

def distance(x1, y1, x2=0, y2=0):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)

greet("Bob", "martha")
greet("Sue")

print(distance(1, 0, 4, 4))
print(distance(6, 13))