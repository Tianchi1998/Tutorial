def save_input_lines_to_a_file():
    file_name = input("Save to what file: ")
    with open(file_name,"w") as f :
        times = 0
        while True:
            line = input("> ")
            if line == ".":
                print("Saving file "+file_name+"\n%d lines saved"%(times))
                break
            f.write(line+"\n")
            times = times + 1

save_input_lines_to_a_file()
