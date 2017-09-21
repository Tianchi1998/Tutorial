itemdict = {}


def getDetails():
    dictionary = {}
    item_title = input("The item title you want: ")
    if item_title == "print":
        print(itemdict)
        exit()
    cost = input("The cost of this item is: ")
    dictionary["title"] = item_title
    dictionary["cost"] = cost
    return dictionary


def main():
    dictionary = getDetails()
    itemdict[dictionary["title"]] = dictionary
    main()


main()
