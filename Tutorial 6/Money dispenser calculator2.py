notes=[100,50,20,10,5,2,1]

def money_dispenser_calculator():
    amount=int(input("The initial amount is: "))
    for note in notes:
        times=amount//note
        amount=amount%note
        if times != 0:
           print("%d x $%d"%(times,note))

money_dispenser_calculator()