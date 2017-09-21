#It's part A.
# def print_number(Limit,Copies):
#     for i in range(Copies):
#         for a in range(Limit):
#             print(a+1,end=" ")
#         print()
#
#
# Limit=int(input("The limit you want: "))
# Copies=int(input("The copy times you want: "))
# print_number(Limit,Copies)



#It's part B.
def printRow(startValue,limit):
    for i in  range(startValue,limit+1):
        print(i,end="\t")

startValue=int(input("The startvalue you want: "))
limit=int(input("The last number you want: "))
printRow(startValue,limit)



#It's part C.
# def printNumberBlock(startVal,limitVal,numcopies):
#     for i in range(numcopies):
#         printRow(startVal,limitVal)
#         print()
#
# startValue=int(input("The startvalue you want:　"))
# limitVal=int(input("The limit you want: "))
# numcopies=int(input("The copy times you want: "))
#
# printNumberBlock(startValue,limitVal,numcopies)