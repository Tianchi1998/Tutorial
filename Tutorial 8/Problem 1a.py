def save_input_lines_to_a_file():
    filename = input("Save to what file: ")
    f = open(filename,"w")
    times = 0
    while True:
        line = input("> ")
        if line == ".":
            times = int(times)
            print("Saving file "+filename+"\n%d lines saved"%(times))
            break
        f.write(line+"\n")
        times = times + 1
    f.close()

save_input_lines_to_a_file()
