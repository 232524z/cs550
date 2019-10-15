#recursion

def factorial(n):
	if n == 0 or n==1:
		return 1
	return factorial(n-1)*n

#print(factorial(998))

def fibr(n):
	if n == 1 or n ==2:
		return 1
	return fib(n-1)+fib(n-2)


def fibl(n):
	a,b = 1,1
	for i in range(n-1):
		a,b=b, b+a
	return a
#print(fibl(100))

def findx(string):
	if len(string)<1:
		return 0
	if string[0] == "x":
		return 1 + findx(string[1:])
	return findx(string[1:])

def eights(num):
	string = str(num)
	if len(string)<1:
		return 0
	if string[0] == "8":
		if len(string)>1:
			if string[1] == "8":
				return 2+eights(string[1:])
		return 1+eights(string[1:])
	return eights(string[1:])

print(eights(880430981823894910298382988))





