count = 0


def x():
    global count
    count = count + 1
    reply = input(">>> ")
    if reply == "x()":
        print("Called %d times" % count)
        x()
    else:
        exit()

x()
