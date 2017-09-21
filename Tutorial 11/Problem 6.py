items = [ {'title':'Toaster', 'cost':'79.95'},
  {'title':'Bread', 'cost':'3.75'},
  {'title':'Peas', 'cost':'2.5'}    ]


def fixCosts(d):
    for item in d:
        previous_cost = item['cost']
        item['cost'] = float(previous_cost)

print(items)

fixCosts(items)

print(items)

sum = 0
for dictionary in items:
    sum = sum + dictionary["cost"]
print("The total cost of all the items is %0.2f"%(sum))