"""
Ian
OMH
1/23/19
This program calculates how long it would take to read every book in the Choate library. It uses weighted randomness based on data gained from books from the library. It simulates each book with a weighted random numbers for the length of the book, how many words are on each page, and how long it takes to read a word (wich reflects the difficulty of different types of books). There are 46,780 books in the library.
Source:https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice, https://matplotlib.org/users/index.html
This program requires the library matplotlib to be installed. It can be downloaded from Pip.
"""
#the choice function chooses a random index from a given list with given weights
from random import choices
import matplotlib.pyplot as plt



#simulates a book with given pages, words, and time
def readBook(pages, words, time):
	return pages*words*time

#selects a weighted random number of pages
def rPages():
	return int(choices(pageprob[0],pageprob[1])[0])

#selects a weighted random number of words per page
def rWords():
	return int(choices(wordsppprob[0],wordsppprob[1])[0])

#selects a weighted random number of how long it takes to to read per word
def rTime():
	return 10/(int(choices(timeprob[0],timeprob[1])[0]))

#converts seconds to years
def secondsToYears(seconds):
	return seconds/31536000

#reads the entire library one time, and outputs the time in years
def readLibrary():
	totaltime = 0
	#simulates a random book for every book in the library
	for i in range(totalbooks):
		pages = rPages()
		words = rWords()
		time = rTime()
		num = readBook(pages, words, time)
		totaltime += num

	#converts the time in seconds to years
	totaltime = secondsToYears(totaltime)
	return totaltime




#the total number of books in the library is 46,780.
totalbooks = 46780
time_per_library = []





#data from a random sampling of books in the library
pageprob = [[x for x in range(125,626,25)],[1,4,2,4,3,1,6,4,4,3,3,1,2,1,0,0,0,1,0,2,3]]
wordsppprob = [[x for x in range(325, 551, 25)],[1,0,1,2,2,1,2,0,1,1]]
#counted as words/time (10 seconds)
timeprob = [[x for x in range(28,58,1)],[1,0,0,1,0,0,0,0,0,0,1,2,0,0,1,1,0,0,0,0,0,3,0,0,0,0,0,0,0,1]]


#calculates the time to read the library 100 times, and adds them to a list to be graphed
for i in range(100):
	time_per_library.append(readLibrary())

#creates the histogram for the number of years it would take to read the entire library
plt.hist(time_per_library)
plt.xlabel('Consecutive Years of Reading')
plt.ylabel('Frequency Out Of 1000 Trials')
plt.title("Distribution of Times To Read Every Book in the Library")
plt.show()