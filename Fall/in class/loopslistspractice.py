#Loops and Lists Basic Practice
import random
import math
 
# 1. Create a list that holds the numbers 1-99 in reverse order.

# l199 = [100-x for x in range(1,100)]
# print(l199)
 
 
# 2. Create a loop that loops through a list of random numbers (ranging from 0-100) and throws away or removes any number greater than 10. This should work for lists of any length.

# lg10 = [(100*random.random()) for x in range(round(1000*random.random()))]
# print(lg10)
# i = 0
# while(True):
# 	if len(lg10)-1<i:
# 		break
# 	if lg10[i]>10:
# 			lg10.pop(i)
# 	else:
# 		i+=1
# print('\n\n')
# print(lg10)
 
# 3. Write a function that will return a list of the first n numbers in the fibonacci sequence. No recursion allowed!

# fib = [1,1]
# n = int(input("n:"))
# for i in range(2,n):
# 	fib.append(fib[i-1]+fib[i-2])
# print(fib)
 
# 4. Write some code that, given a list, will tell you if a given value is in the list. 

# lvalue = [round(10*random.random()) for x in range(10)]
# print(lvalue)
# n = int(input("n:"))
# numberContained = n in lvalue

# print(numberContained)
 
# 5. Write some code that, given a list of 30 random numbers between 1 and 30, will print to the screen "Yahtzee!" if the first six multiples under 30 of any number 1-6 are all in the list. For example, 1, 2, 3, 4, 5, and 6 = yahtzee, 3, 6, 9, 12, 15 = yahtzee, etc. 

# ylist = [round(30*random.random()) for x in range(30)]
# ynumber = 0
# print(ylist)
# for x in range(1,7):
# 	ynumber = 0
# 	for i in range (1,6):
# 		if x*i in ylist:
# 			ynumber +=1
# 	if ynumber == 5:
# 		print("Yahtzee!")
 
# 6. Write a function that accepts an array of numbers, and returns the sum of the numbers in the array, except sections of numbers starting with a 6 and extending to the next 7 will be ignored in the sum (every 6 will be followed by at least one 7). Return 0 for no numbers. For example: 1, 2, 3, 6, 4, 5, 7, 7 would return 13.

# a67 = [random.randint(1, 10) for x in range(10)]
# asum = 0
# ignore = False
# for i in range(len(a67)):
# 	if a67[i]==6:
# 		ignore = True
# 	if ignore == False:
# 		asum += a67[i]
# 	if a67[i]==7:
# 		ignore = False

# print(a67)
# print(asum)











