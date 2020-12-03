def decode(fileName):
    with open(fileName, "r") as file:
        lab = []
        # decode and get the column and row number
        first_line = file.readline()
        for line in file:
            data = line.replace('\n', '').split(",")
            data = [int(i) for i in data]
            lab.append(data)
    file.close()
    return lab
