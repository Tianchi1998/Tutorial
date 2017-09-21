def copy_a_file(old_file,new_file):
    file = open(new_file, "w")
    try:
        f = open(old_file,"r")
    except:
        print("Couldn't open the file: "+old_file+"\nOutput file NOT written.")
        exit()
    print(" *** Truncating File Copy *** ")
    omitStartCount = input("Omit how many lines from the start: ")
    omitEndCount = input("Omit how many lines from the end: ")
    times = 0
    contents = f.readlines()
    length = len(contents)
    for line in contents:
        if length <= (int(omitEndCount)+int(omitStartCount)):
            print("The input file is too short.")
            break
        times = times + 1
        line = line.strip()
        if times <= int(omitStartCount):
            continue
        if times > length-int(omitEndCount):
            continue
        file.write(line+"\n")
    file.close()
    f.close()

copy_a_file("the file needed to be copied.txt","test1.txt")
