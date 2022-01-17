def exists(matrix: list, row: int, col: int, row_next: int, col_next: int) -> bool:
    if row_next < 0 or col_next < 0 or row_next > (len(matrix) - 1) or col_next > (len(matrix[0]) - 1):
        return True
    if matrix[row][col] < matrix[row_next][col_next]:
        return True
    return False


def find_low(row: int, col: int, matrix: list) -> int:
    '''
        right i,j+1
        left i,j-1
        up: i-1, j
        down: i+1, j
    '''
    if (exists(matrix, row, col, row, col+1) and
        exists(matrix, row, col, row, col-1) and
        exists(matrix, row, col, row-1, col) and
        exists(matrix, row, col, row+1, col)):
        return matrix[row][col]

    return None


def part1() -> int:
    with open("input9", "rb") as data:
        matrix = [list(map(int,line.decode("utf8").split()[0])) for line in data]
    # scan through each row and find low points
    lows = []
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            low = find_low(i, j, matrix)
            if low is not None:
                lows.append(low)

    low_sum = 0
    for low in lows:
        low_sum = low_sum + low + 1
    return low_sum


print(part1())
