def money_dispenser_calculator():
    initial_amount=int(input("The initial amount is: "))
    if initial_amount>=100:
        times_100=initial_amount//100
        initial_amount=initial_amount%100
        times_50=initial_amount//50
        initial_amount=initial_amount%50
        times_20=initial_amount//20
        initial_amount=initial_amount%20
        times_10=initial_amount//10
        initial_amount=initial_amount%10
        times_5=initial_amount//5
        initial_amount=initial_amount%5
        times_2=initial_amount//2
        initial_amount=initial_amount%2
        times_1=initial_amount
        print("%d x $100"%(times_100))
        print("%d x $50"%(times_50))
        print("%d x $20"%(times_20))
        print("%d x $10"%(times_10))
        print("%d x $5"%(times_5))
        print("%d x $2"%(times_2))
        print("%d x $1"%(times_1))
    elif initial_amount>=50:
        times_50=initial_amount//50
        initial_amount=initial_amount%50
        times_20=initial_amount//20
        initial_amount=initial_amount%20
        times_10=initial_amount//10
        initial_amount=initial_amount%10
        times_5=initial_amount//5
        initial_amount=initial_amount%5
        times_2=initial_amount//2
        initial_amount=initial_amount%2
        times_1=initial_amount
        print("%d x $50"%(times_50))
        print("%d x $20"%(times_20))
        print("%d x $10"%(times_10))
        print("%d x $5"%(times_5))
        print("%d x $2"%(times_2))
        print("%d x $1"%(times_1))
    elif initial_amount>=20:
        times_20=initial_amount//20
        initial_amount=initial_amount%20
        times_10=initial_amount//10
        initial_amount=initial_amount%10
        times_5=initial_amount//5
        initial_amount=initial_amount%5
        times_2=initial_amount//2
        initial_amount=initial_amount%2
        times_1=initial_amount
        print("%d x $20"%(times_20))
        print("%d x $10"%(times_10))
        print("%d x $5"%(times_5))
        print("%d x $2"%(times_2))
        print("%d x $1"%(times_1))
    elif initial_amount>=10:
        times_10=initial_amount//10
        initial_amount=initial_amount%10
        times_5=initial_amount//5
        initial_amount=initial_amount%5
        times_2=initial_amount//2
        initial_amount=initial_amount%2
        times_1=initial_amount
        print("%d x $10"%(times_10))
        print("%d x $5"%(times_5))
        print("%d x $2"%(times_2))
        print("%d x $1"%(times_1))
    elif initial_amount>=5:
        times_5=initial_amount//5
        initial_amount=initial_amount%5
        times_2=initial_amount//2
        initial_amount=initial_amount%2
        times_1=initial_amount
        print("%d x $5"%(times_5))
        print("%d x $2"%(times_2))
        print("%d x $1"%(times_1))
    elif initial_amount>=2:
        times_2=initial_amount//2
        initial_amount=initial_amount%2
        times_1=initial_amount
        print("%d x $2"%(times_2))
        print("%d x $1"%(times_1))
    else:
        times_1=1
        print("%d x $1"%(times_1))

money_dispenser_calculator()
