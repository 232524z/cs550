t = float(input("t="))
v = float(input("v="))
windchill = int((35.74)+(0.6215*t)+((0.4275*t)-35.75)*(v**.16))
output = "Feels like " + str(windchill) + "˚F"
if(abs(t)>50 or v>120 or v<3):
	output = "error"
print(output)