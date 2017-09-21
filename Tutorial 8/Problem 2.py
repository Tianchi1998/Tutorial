def copy_a_file(old_file,new_file):
    file = open(new_file, "w")
    with open(old_file,"r") as f:
        for line in f:
            line = line.strip()
            file.write(line+"\n")
    file.close()

copy_a_file("the file needed to be copied.txt","the file I want.txt")
