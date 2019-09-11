"""
Ian
9/11/19
this program calculates the day of the week for a given
day, month, and year.
sources: http://mathforum.org/dr.math/faq/faq.calendar.html
I received help from Kai and Will Greive
OMH

"""
import math
m_input = int(input("month: "))
k = int(input("\nday: "))
year = input("\nyear: ")
m=(m_input+10)%12
c = int(year[0]+year[1])
d = int(year[2]+year[3])

dayOfWeek=math.floor((k+((13*m-1)/5+d+(d/4)+(c/4)-2*c))%7)
print(dayOfWeek)