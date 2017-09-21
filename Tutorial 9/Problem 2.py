def setBalance(amt):
    global balance
    balance = amt


def printBalance():
    print("Current Balance is $%10.2f"%float(balance))


# def printLedgerLine(date,amount,details):


def deposit(date,details,amount):
    global balance
    print("%s      %-20s      $%10.2f         $%10.2f" % (date,details,float(amount),balance + float(amount)))
    balance = balance + float(amount)


def withdraw(date,details,amount):
    global balance
    print("%s      %-20s      $%10.2f         $%10.2f" % (date,details,float(amount),balance-float(amount)))
    balance  = balance - float(amount)


# We call the functions above.
setBalance(500)
printBalance()
withdraw("17-12-2012", "BP - petrol", 72.50)
withdraw("19-12-2012", "Countdown", 55.50)
withdraw("20-12-2012", "munchies", 1.99)
withdraw("22-12-2012", "Vodafone", 20)
deposit ("23-12-2012", "Income", 225)
withdraw("24-12-2012", "Presents", 99.02)
printBalance()