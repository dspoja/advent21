from collections import deque


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


def find_basin_size(row: int, col: int, matrix: list) -> int:
    '''
    use floodfill technique
    '''
    stack=[(row, col)]
    basin_values = []
    while stack:
        i, j = stack.pop()
        if matrix[i][j] != 9:
            if (i, j) not in basin_values:
                basin_values.append((i, j))
            else:
                continue
            if i + 1 < len(matrix):
                stack.append((i + 1, j))
            if i - 1 >= 0:
                stack.append((i - 1, j))
            if j + 1 < len(matrix[0]):
                stack.append((i, j + 1))
            if j - 1 >= 0:
                stack.append((i, j - 1))
        else:
            pass
    return len(basin_values)


def compute_smoke_basins(compute_basin_size: bool=False) -> int:
    with open("input9", "rb") as data:
        matrix = [list(map(int,line.decode("utf8").split()[0])) for line in data]
    # scan through each row and find low points
    basins = []
    basin_sizes = deque()
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            low = find_low(i, j, matrix)
            if low is not None:
                basins.append(low)
                if compute_basin_size:
                    # compute basin for this point
                    basin_size = find_basin_size(i, j, matrix)
                    print(f"basin size={basin_size}")
                    basin_sizes.append(basin_size)
    if not compute_basin_size:
        low_sum = 0
        for low in basins:
            low_sum = low_sum + low + 1
        return low_sum
    else:
        basin_sizes = sorted(basin_sizes,reverse=True)
        total = 1
        end = 3 if len(basin_sizes) > 3 else len(basin_sizes)
        for i in range(0, end):
            total *= basin_sizes[i]
        return total


print(compute_smoke_basins())
print(compute_smoke_basins(compute_basin_size=True))
