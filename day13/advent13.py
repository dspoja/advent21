
def build_blank_sheet(x: int, y: int) -> list:
    matrix = []
    for i in range(y+1):
        matrix.append([])
        for j in range(x+1):
            matrix[i].append([])
    for i in range(y+1):
        for j in range(x+1):
            matrix[i][j] = "."
    return matrix


def populate_with_dots(matrix: list, coordinates: list) -> list:
    for coordinate in coordinates:
        matrix[coordinate[1]][coordinate[0]] = "#"
    return matrix


def print_matrix(matrix: list) -> None:
    for i in range(len(matrix)):
        print(*matrix[i])


def fold_up_for_y(matrix: list, fold: int) -> list:
    # fold by y-axis
    for i in range(0, len(matrix[fold])):
        matrix[fold][i] = "-"
    # create a new matrix that has only items above the fold line
    new_matrix = []
    for i in range(fold):
        new_matrix.append(matrix[i])
    # Loop through items below the fold line and move them into the new matrix
    for i in range(fold+1, len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "#":
                # move this item to new matrix
                move_value = len(new_matrix) - (i-fold)
                new_matrix[move_value][j] = "#"
    return new_matrix


def fold_left_for_x(matrix: list, fold: int) -> list:
    # fold by x-axis
    for i in range(0, len(matrix)):
        matrix[i][fold] = "-"
    # create a new matrix that has only items to the left of the fold line
    new_matrix = []
    for i in range(0, len(matrix)):
        new_matrix.append(matrix[i][0:fold])
    # Loop through items below the fold line and move them into the new matrix
    for i in range(0, len(matrix)):
        for j in range(fold+1, len(matrix[i])):
            if matrix[i][j] == "#":
                # move this item to new matrix
                move_value = len(new_matrix[i]) - (j - fold)
                new_matrix[i][move_value] = "#"
    return new_matrix


def count_dots(matrix: list) -> int:
    count = 0
    for i in range(0, len(matrix)):
        for j in range (0, len(matrix[i])):
            if matrix[i][j] == "#":
                count += 1
    return count


dots = []
folding_instructions = []
max_x = 0
max_y = 0

# read in input data
with open("input13", "rb") as data:
    for line in data:
        line = line.strip().decode("utf8")
        if not line:
            continue
        if "fold along " in line:
            # get folding instructions
            folding_instructions.append(line.replace("fold along ", "").split("="))
        else:
            # get dots coordinates
            coordinates = list(map(lambda x: int(x), line.split(",")))
            if coordinates[0] > max_x:
                max_x = coordinates[0]
            if coordinates[1] > max_y:
                max_y = coordinates[1]
            dots.append(coordinates)

dots_matrix = build_blank_sheet(max_x, max_y)
dots_matrix = populate_with_dots(dots_matrix, dots)
for fold_value in folding_instructions:
    if fold_value[0] == 'y':
        dots_matrix = fold_up_for_y(dots_matrix, int(fold_value[1]))
    else:
        dots_matrix = fold_left_for_x(dots_matrix, int(fold_value[1]))

print_matrix(dots_matrix)
print(count_dots(dots_matrix))

