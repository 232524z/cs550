import random

# x = random.random()
# while x>.5:
# 	print(x)
# 	x = random.random()

# count = 1
# while count<=5:
# 	print("*"*count)
# 	count +=1

# for x in range(1,6):
# 	print("*"*x)

# myList = list(range(7,700001,7))
# print(myList)

# L = []
# for i in range(7,700001,7):
# 	L.append(i)
# print(L)

# newList = [x for x in range(7,700001,7)]
# print(len(newList))
while(True):
	response = int(input("sample size:\n"))
	numbers = 0
	stars = 0
	List = [round(100*random.random())for x in range(0,response)]

	for x in range(10, 100, 10):
		for i in List:
			if i < x and i > x-10:
				numbers += 1
		stars = round(numbers*(100/response))
		print("*"*stars)
		numbers = 0
		stars = 0
