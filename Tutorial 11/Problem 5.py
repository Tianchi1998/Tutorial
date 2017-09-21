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
        exit()
    dictionary_list.append(details)
    main()


main()

