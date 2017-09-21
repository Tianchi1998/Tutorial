dictionary = [   ['the', 'la'],['red', 'rosso'], ['is', "e'"], ['table', 'tavola'],['nihao','Hello'] ]


def load_a_file_as_initial_dictionary():
    global dictionary
    try:
        try:
            f = open("dictionary.txt","r")
        except:
            exit(-1)
        line_list = f.readlines()
        f.close()
        for line in line_list:
            line = line.strip()
            sublist = line.split("/")
            if [sublist[0],sublist[1]] in dictionary:
                continue
            else:
                dictionary.append([sublist[0],sublist[1]])
    except:
        f.close()
        exit(-1)


def displayDictionary():
    if dictionary == []:
        print("*** The dictionary is empty ***")
    else:
        print("\n*** Known words ***")
        for sublist in dictionary:
            print("%-15s%-15s"%(sublist[0],sublist[1]))


def lookup(word):
    global dictionary
    English_list = []
    for sublist in dictionary:
        English_list.append(sublist[0])
    if word in English_list:
        for item in dictionary:
            if item[0] == word:
                return item[1]
            else:
                continue
    else:
        translation = input("How do I translate %s: "%(word))
        dictionary.append([word,translation])
        return translation


def main():
    load_a_file_as_initial_dictionary()
    while True:
        reply = input("\nEng: > ")
        reply = reply.lower()
        if reply == "?":
            displayDictionary()
            main()
        if reply == "*quit":
            f = open("dictionary.txt", "r")
            line_list = f.readlines()
            old_dictionary = []
            for line in line_list:
                line = line.strip()
                line = line.split("/")
                old_dictionary.append(line)
            if old_dictionary == dictionary:
                exit(-1)
            else:
                file = open("dictionary.txt", "w")
                for i in dictionary:
                    file.write("%s/%s\n"%(i[0],i[1]))
                exit(-1)
        if reply == "*save":
            f = open("dictionary.txt", "w")
            for i in dictionary:
                f.write("%s/%s\n" % (i[0], i[1]))
            f.close()
            main()
        if "," in reply:
            reply = reply.replace(","," ")
        if "." in reply:
            reply = reply.replace("."," ")
        if "?" in reply:
            reply = reply.replace("?"," ")
        reply = reply.strip()
        words = reply.split()
        translatedReply = []
        for word in words:
            translation = lookup(word)
            translatedReply.append(translation)
        if None in translatedReply:
            index = translatedReply.index(None)
            translatedReply[index] = "None"
        final_string = " ".join(translatedReply)
        final_string = final_string.capitalize()
        final_string = final_string.replace("none","None")
        print(">>> "+final_string + ".")


main()