dictionary_list = []


def getDetails():
    dictionary = {}
    item_title = input("The item title you want: ")
    if item_title == "quit":
        for item in dictionary_list:
            print("%-15s%-15s"%(item["title"],item["cost"]))
        return None
    elif item_title == "print":
        print(dictionary_list)
        exit()
    cost = input("The cost of this item is: ")
    dictionary["title"] = item_title
    dictionary["cost"] = cost
    return dictionary


def main():
    details = getDetails()
    if details == None:
        return dictionary_list
    dictionary_list.append(details)
    main()


main()


def fixCosts(d):
    for item in d:
        previous_cost = item['cost']
        item['cost'] = float(previous_cost)

print(dictionary_list)

fixCosts(dictionary_list)

print(dictionary_list)

sum = 0
for dictionary in dictionary_list:
    sum = sum + dictionary["cost"]
print("The total cost of all the items is %0.2f"%(sum))