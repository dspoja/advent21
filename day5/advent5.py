from typing import List

def compute_max(points: List, max_x: int, max_y: int) -> int:
    if points[0][0] > max_x: max_x = points[0][0]
    if points[1][0] > max_x: max_x = points[1][0]
    if points[0][1] > max_y: max_y = points[0][1]
    if points[1][1] > max_y: max_y = points[1][1]
    return max_x, max_y


def parse_points() -> List:
    with open("input5-sample", "rb") as coords:
        max_x = 0
        max_y = 0
        coordinates = []
        for coord in coords:
            coord = coord.decode("utf-8").strip()
            #parse the coordinates
            points = [list(map(int, line.strip().split(","))) for line in coord.split("->")]
            max_x, max_y = compute_max(points, max_x, max_y)
            coordinates.extend([points])

    print(f"max_x:{max_x}")
    print(f"max_y:{max_y}")
    print(f"coordinates: {coordinates}")
    return coordinates, max_x+1, max_y+1


def construct_matrix(max_x: int, max_y: int) -> List:
    matrix = []
    for i in range(max_y):
        matrix.append([0] * max_x)
    return matrix


def print_matrix(matrix: List):
    for row in matrix:
        print(row)


def mark_lines(row: List, from_pos: int, to_pos: int) -> (List, int):
    for i in range(from_pos, to_pos+1):
        row[i] += 1
    return row


def populate_matrix(matrix: List, coordinates: List) -> int:
    for point in coordinates:
        start_x = point[0][0]
        start_y = point[0][1]
        end_x = point[1][0]
        end_y = point[1][1]
        if start_y == end_y:
            if start_x > end_x:
                matrix[start_y] = mark_lines(matrix[start_y], end_x, start_x)
            else:
                matrix[start_y] = mark_lines(matrix[start_y], start_x, end_x)
        elif start_x == end_x:
            if start_y <= end_y:
                for i in range(start_y, end_y+1):
                    matrix[i] = mark_lines(matrix[i], start_x, end_x)
            else:
                for i in range(end_y, start_y+1):
                    matrix[i] = mark_lines(matrix[i], start_x, end_x)

    print_matrix(matrix)
    return matrix


def count_points(matrix: List) -> int:
    points = 0
    for i, row in enumerate(matrix):
        for column in matrix[i]:
            if column > 1: points += 1
    return points


coordinates, max_x, max_y = parse_points()
matrix = construct_matrix(max_x, max_y)
matrix = populate_matrix(matrix, coordinates)
points = count_points(matrix)
print(f"Total points: {points}")
