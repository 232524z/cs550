import matplotlib.pyplot as plt

"""
Ian
OMH
1/17/19
This program calculates how long it would take to read every book in the Choate library. It uses weighted randomness based on data gained from books from the library. It simulates each book with a weighted random numbers for the length of the book, how many words are on each page, and how long it takes to read a word (wich reflects the difficulty of different types of books). There are 46,780 books in the library.
Source:https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
"""
#the choice function chooses a random index from a given list with given weights
from random import choices


#simulates a book with given pages, words, and time
def readBook(pages, words, time):
	return pages*words*time

#selects a weighted random number of pages
def rPages():
	c = int(choices(pageprob[0],pageprob[1])[0])
	page.append(c)
	return c

#selects a weighted random number of words per page
def rWords():
	return int(choices(wordsppprob[0],wordsppprob[1])[0])

#selects a weighted random number of how long it takes to to read per word
def rTime():
	return 10/(int(choices(timeprob[0],timeprob[1])[0]))

#converts seconds to years
def secondsToYears(seconds):
	return seconds/31536000

#the total number of books in the library is 46,780.
totalbooks = 46780
totaltime = 0
page = []

#data from a random sampling of books in the library
pageprob = [[x for x in range(125,626,25)],[10,40,20,40,30,10,60,40,40,30,30,10,20,10,5,5,5,10,5,20,30]]
wordsppprob = [[x for x in range(325, 551, 25)],[1,0,1,2,2,1,2,0,1,1]]
#counted as words/time (10 seconds)
timeprob = [[x for x in range(28,58,1)],[1,0,0,1,0,0,0,0,0,0,1,2,0,0,1,1,0,0,0,0,0,3,0,0,0,0,0,0,0,1]]



#simulates a random book for every book in the library
for i in range(totalbooks):
	totaltime += readBook(rPages(), rWords(), rTime())

#converts the time in seconds to years
totaltime = secondsToYears(totaltime)



#returns the total time
print(f'{totaltime} Years')


plt.hist(page)
plt.xlabel('Number of pages')
plt.ylabel('Number of books')
plt.title("Distribution of pages per book")
plt.show()
