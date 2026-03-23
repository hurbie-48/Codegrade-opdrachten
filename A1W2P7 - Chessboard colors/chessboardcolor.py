valid_positions = ["A","B","C","D","E","F","G","H"]
user_input = input("")
column = user_input[0].capitalize()
row = int(user_input[1])

def blackOrWhite(column:int, row:int) -> str:
    columnsum = 0
    rowsum = 0
    if (valid_positions.index(column)+1)%2 == 0:
        columnsum = 1
    if (row%2) == 0:
        rowsum = 1
    
    if (columnsum + rowsum)%2 == 0:
        return "Black"
    else:
        return "White"

print(blackOrWhite(column, row))