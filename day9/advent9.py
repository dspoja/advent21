def exists(matrix: list, row: int, col: int, row_next: int, col_next: int) -> bool:
    global rows_num, columns_num
    if row_next < 0 or col_next < 0 or row_next > rows_num or col_next > columns_num:
        return True
    if matrix[row][col] < matrix[row_next][col_next]:
        return True
    return False


def find_low(row: int, col: int, matrix: list) -> list:
    '''
        right i,j+1
        left i,j-1
        up: i-1, j
        down: i+1, j
    '''
    lows = []
    if (exists(matrix, row, col, row, col+1) and
        exists(matrix, row, col, row, col-1) and
        exists(matrix, row, col, row-1, col) and
        exists(matrix, row, col, row+1, col)):
        lows.append(matrix[row][col])

    return lows


def part1() -> int:
    global rows_num, columns_num
    with open("input9-sample", "rb") as data:
        matrix = [list(map(int,line.decode("utf8").split()[0])) for line in data]
    #scan through each row and find low points
    rows_num = len(matrix) - 1
    columns_num = len(matrix[0]) - 1
    lows = []
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            lows.extend(find_low(i, j, matrix))

    sum = 0
    for low in lows:
        sum = sum + low + 1
    return sum


rows_num = 0
columns_num = 0
print(part1())
