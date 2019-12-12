import random
# a = [[3,7,4],[1,1,1,],[5,8,9,],[2,3,7],[1,2,3,4],[1,6,4]]

def niceprint(a):
	for i in a:
		print(*i)
	print("\n")

# for row in a:
# 	for col in row:
# 		print(col+5)

# for row in range(len(a)):
# 	for col in range(len(a[row])):
# 		a[row][col] += 5
# niceprint(a)

# b = [[random.randint(1,5) for x in range(5)] for y in range(7)]
# niceprint(b)

c = [[random.randint(0,1) for x in range(8)] for y in range(2)]
niceprint(c)

# d = [[x+y*20 for x in range(2, 21, 2)] for y in range(0, 10)]
# niceprint(d)

e = [[0 for x in range(7)] for y in range(3)]
niceprint(e)