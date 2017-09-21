def tax(tax_rate,amount):
     result=tax_rate*amount
     return result

rate_list=[0.05,0.1,0.15,0.20,0.25]
for rate in rate_list:
     tax1=tax(rate,17.50)
     tax2=float(tax1)
     print("%d%% tax on a Chocolate cake costing $17.50 is $%0.2f"%(int(rate*100),tax2))


