"""
Ian
9/10/19
this program determins wether 3 floats are in
ascending/descending order. answer is true or false.
sources: None
OMH
"""
x = float(input("x="))
y = float(input("\ny="))
z= float(input("\nz="))
if(x<y):
	if(y<z):
		output = True
	else:
		output = False
elif(y>z):
	output = True
else:
	output = False

print(str(output))