'''
Ian
9/14/19
This program calculates a grade based on a number input 1-5
Sources: https://www.geeksforgeeks.org/python-list/
https://www.jquery-az.com/5-examples-get-python-list-length-array-tuple-dictionary-also/
https://wiki.python.org/moin/ForLoop
OMH
'''
gradeNumbers = [0, 1, 1.5, 2, 2.5, 2.85, 3.2, 3.5, 3.85, 4.2, 4.5, 4.65, 4.85]
gradeLetters = ['F','D-','D','D+','C-','C','C+','B-','B','B+','A-','A','A+']
score = float(input("Score (0-5)\n"))
if score < 0 or score > 5:
	print("Error! Score must be between 0 and 5!")
	exit()
for i in range(0, len(gradeNumbers)) :
	if score >= gradeNumbers[i]:
		grade=gradeLetters[i]
print(grade)