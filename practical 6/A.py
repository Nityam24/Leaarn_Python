# A) Create a class account with necessary methods – showBalance, withdraw, deposit and
# transfer. Also, implement necessary getters and setters. Instantiate 2 objects of that
# class and show different method calls using them

class account:

    def __init__(self):
        self.balance = 0
        self.acno = 0

    def showBalance(self):
        print("Current Bal:", self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance-amt
            print("Withraw of ₹{} successful".format(amt))

    def deposit(self, amt):
        if amt == 0:
            print("Must Be Non Zero")
        else:
            self.balance = self.balance+amt
            print("Deposite of ₹{} successful".format(amt))

    def transfer(self, amt, ac2):
        if amt == 0:
            print("Must Be Non Zero")
        elif amt > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance-amt
            print("Transfer from {} to {} of ₹{} successful, current balance {}".format(
                self.acno, ac2, amt, self.balance))

    def getters(self):
        print(self.balance)
        print(self.acno)

    def setters(self, acno, balance):
        self.balance = balance
        self.acno = acno


print("OBJ 1")
ac1 = account()
ac1.setters(12345678910111, 5000)
ac1.deposit(5000)
ac1.withdraw(500)
ac1.showBalance()
ac1.transfer(5000, 12534258741230)

print("OBJ 2")
ac2 = account()
ac2.setters(52425784201203, 50000)
ac2.deposit(50000)
ac2.withdraw(5000)
ac2.showBalance()
ac2.transfer(40000, 12534258741230)
# A) Create a class account with necessary methods – showBalance, withdraw, deposit and
# transfer. Also, implement necessary getters and setters. Instantiate 2 objects of that
# class and show different method calls using them

class account:

    def __init__(self):
        self.balance = 0
        self.acno = 0

    def showBalance(self):
        print("Current Bal:", self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance-amt
            print("Withraw of ₹{} successful".format(amt))

    def deposit(self, amt):
        if amt == 0:
            print("Must Be Non Zero")
        else:
            self.balance = self.balance+amt
            print("Deposite of ₹{} successful".format(amt))

    def transfer(self, amt, ac2):
        if amt == 0:
            print("Must Be Non Zero")
        elif amt > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance-amt
            print("Transfer from {} to {} of ₹{} successful, current balance {}".format(
                self.acno, ac2, amt, self.balance))

    def getters(self):
        print(self.balance)
        print(self.acno)

    def setters(self, acno, balance):
        self.balance = balance
        self.acno = acno


print("OBJ 1")
ac1 = account()
ac1.setters(12345678910111, 5000)
ac1.deposit(5000)
ac1.withdraw(500)
ac1.showBalance()
ac1.transfer(5000, 12534258741230)

print("OBJ 2")
ac2 = account()
ac2.setters(52425784201203, 50000)
ac2.deposit(50000)
ac2.withdraw(5000)
ac2.showBalance()
ac2.transfer(40000, 12534258741230)
