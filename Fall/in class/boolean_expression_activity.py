#1
"""
num = int(input("number = "))
near10 = 10*round(num/10)
isTrue = abs(near10-num)<=2
print(isTrue)
"""

#2
"""
num1 = int(input("number 1 = "))
num2 = int(input("\nnumber 2 = "))
isTrue = num1%num2 == 0 or num2%num1 == 0
print(isTrue)
"""

#3
"""
year = int(input("year: "))
isTrue = year%4== 0
print(isTrue)
"""

#4
"""
temperature = int(input("Temperature:"))
is_summer = input("Is summer? ") == "True"
tempLow = temperature < 60
tempHigh = (temperature > 100) or (temperature > 90 and is_summer == False)
isTrue = (tempLow == False) & (tempHigh == False)
print(isTrue)
"""
#5
"""
a = int(input("a= "))
b = int(input("\nb= "))
c = int(input("\nc= "))

Close = abs(a-b) <=1 or abs(a-c) <= 1
Far = (abs(a-b) >=2 or abs(a-c) >=2) and abs(b-c) >=2
isTrue = Close == True and Far == True
print(isTrue)
"""