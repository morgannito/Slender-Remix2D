import module.jeu.board as board

# decode the .csv file
def decode_csv(fileName):
    with open(fileName, "r") as file:
        # decode and get the column and row number
        first_line = file.readline()
        row_and_column = first_line.replace('\n', '').split(",")
        row_and_column = [int(i) for i in row_and_column]
        for line in file:
            data = line.replace('\n', '').split(",")
            data = [int(i) for i in data]
            board.lab.append(data)
        global row_number, column_number
        column_number = len(data)
        row_number = len(board.lab)
        end_position = [row_number - 2, column_number - 2]
    file.close()
