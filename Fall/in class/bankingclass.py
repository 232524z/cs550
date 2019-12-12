class bank:

	def __init__(self,balance=0,apy=0,accountnum = 0,bank = 'Chase'):
		self.balance = balance
		self.apy = apy
		self.accountnum = accountnum
		self.bank = bank

	def withdraw(self,amount):
		if amount > self.balance:
			return "Not enough money!"
		self.balance -= amount
		return "Withdrew $"+str(amount) + "\n"

	def deposit(self,amount):
		self.balance += amount
		return "Deposited $"+str(amount) + "\n"

	def showdetails(self):
		result = "Balance: $"+str(self.balance)
		result += "\nAPY: "+str(self.apy)+"%"
		result += "\nAccount number: "+str(self.accountnum)
		result += "\nBank: "+self.bank
		result += "\n"
		return result

	def changeRate(self,new):
		a = self.apy
		self.apy = new
		return "Interest changed from "+str(a)+"% to "+str(new)+"%\n"



b1 = bank(1000,1,32,"Local Bank")
print(b1.withdraw(200))
print(b1.changeRate(2))
print(b1.showdetails())

