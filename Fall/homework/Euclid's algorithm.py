#Ian
#OMH
#10/13/19
#This program uses recursion to find the greatest common denominator between 2 numbers.
#sources: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
#gets numbers
A = int(input("A: "))
B = int(input("B: "))

def gdc(a,b):
	#ends if b = 0
	if b == 0:
		return a
	#for the next run of the function, sets a to b and b to a%b
	return gdc(b, a%b)
print(gdc(A,B))