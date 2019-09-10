"""
Ian
9/10/19
this program sums the sin^2 and cos^2 for an entered number
it also calculates the distance given points on a
cartesian coordinate plane
1
when computing force = g*mass1*mass2/radius*radius,
the computer does not see that both radii are under the
vinculum, so it multiplies radius * 1/radius, getting 1.
the final answer will just be g*mass1*mass 2.
a change to the program would be:
force=(g*mass1*mass2)/(radius*radius)
an alternative would be
force=g*mass1*mass2/radius/radius
OMH
"""
#2
import math
θ = float(input("sum of sine^2 and cosine^2\n"))
output = ((math.sin(θ))**2)+((math.cos(θ))**2)
print("Sum: ",output)
'''
output is not always 1 since there is some rounding
that must be done when calculating the sine and cosine.
when both round down, the sum will be just under 1
'''
print("\n\n\ndistance on cartesian coordinate plane")
x = float(input("\nx\n"))
y = float(input("y\n"))
distance = ((x**2)+(y**2))**(1/2)
print("distance: ",distance)