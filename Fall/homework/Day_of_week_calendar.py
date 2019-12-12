"""
Ian
9/12/19
this program calculates the day of the week for a given
day, month, and year.
sources: Worksheet with formula
OMH

"""
m = int(input("month: "))
d = int(input("\nday: "))
y = int(input("\nyear: "))

y0=(y-(14-m)//12)
x=(y0 + y0//4 -y0//100 + y0//400)
m0=(m+12*((14-m)//12)-2)
d0=(d+x+(31*m0//12))%7
print(d0)