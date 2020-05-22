def dump(file_name):
    "Dump file to terminal"
    f = open(file_name,"r")
    for line in f:
        print(line[:-1])
    f.close()
