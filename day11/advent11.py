from copy import deepcopy
# define needed data and data structs
neighbors = [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1,), (1, 0), (1, 1)]
flashed_octos = []
flash_count = 0


def check_octo(octos: list, i: int, j: int, flashed_octos: list) -> None:
    global flash_count
    if octos[i][j] > 9 and (i, j) not in flashed_octos:
        octos[i][j] = 0
        flash_count = flash_count + 1
        flashed_octos.append((i, j))
        # go through the neighbors and check uf they flash or not
        for neighbor in neighbors:
            next_i = i + neighbor[0]
            next_j = j + neighbor[1]
            if -1 < next_i < len(octos) and -1 < next_j < len(octos):
                if (next_i, next_j) not in flashed_octos:
                    octos[next_i][next_j] = octos[next_i][next_j] + 1
                if octos[next_i][next_j] > 9 and (next_i, next_j) not in flashed_octos:
                    check_octo(octos, next_i, next_j, flashed_octos)


def print_octos(octos: list) -> None:
    for i, row in enumerate(octos):
        print(row)


def detect_all_zeros(octos: list) -> bool:
    for i, row in enumerate(octos):
        for j, _ in enumerate(row):
            # check if flashed
            if octos[i][j] != 0:
                return False
    return True


def navigate_cave(part: int) -> list:
    if part == 1:
        steps = 101
    else:
        steps = 1001
    for step in range(1, steps):
        # increase energy levels for all octos
        for i, row in enumerate(octos):
            for j, _ in enumerate(row):
                octos[i][j] = octos[i][j] + 1

        # check if octos can flash
        for i, row in enumerate(octos):
            for j, _ in enumerate(octos):
                check_octo(octos, i, j, flashed_octos)

        # reset flashed octos list at the end of the step
        flashed_octos.clear()

        if part == 2 and detect_all_zeros(octos):
            print(f"Step {step} has all zeros")
            break
    return octos


with open("input11", "rb") as data:
    source_octos = [list(map(int, line.decode("utf8").split()[0])) for line in data]

# Part 1
octos = deepcopy(source_octos)
octos = navigate_cave(1)
print(f"There are {flash_count} after 100 steps")
# Part 2
octos = source_octos.copy()
octos = navigate_cave(2)

