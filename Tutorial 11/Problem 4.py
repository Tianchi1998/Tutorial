def getDetails():
    dictionary = {}
    item_title = input("The item title you want: ")
    if item_title == "quit":
        return None
    cost = input("The cost of this item is: ")
    dictionary["title"] = item_title
    dictionary["cost"] = cost
    return dictionary


def main():
    details = getDetails()
    if details == None:
        exit()
    print("The dict returned was : ", details)
    print("The %s was $%s"%(details["title"],details["cost"]))
    main()


main()
