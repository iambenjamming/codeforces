def excel(row, col):
    excel_col = ''
    while col > 0:
        col, remainder = divmod(col - 1, 26)
        excel_col = chr(65 + remainder) + excel_col
    return excel_col + str(row)

def exceltorc(cell):
    col_letters = ''
    for char in cell:
        if char.isalpha():
            col_letters += char
        else:
            row = int(cell[len(col_letters):])
            break
    col = 0
    for char in col_letters:
        col = col * 26 + (ord(char) - 64)
    
    return 'R' + str(row) + 'C' + str(col)

n = int(input())
for _ in range(n):
    coordinates = input()
    if coordinates.startswith('R') and 'C' in coordinates:
        parts = coordinates[1:].split('C')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            row = int(parts[0])
            col = int(parts[1])
            print(excel(row, col))
        else:
            print(exceltorc(coordinates))
    else:
        print(exceltorc(coordinates))
        

