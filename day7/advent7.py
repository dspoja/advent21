
def part1():
    with open("input7", "rb") as data:
        initial_state = list(map(int, data.readline().decode("utf8").split()[0].split(",")))

        fuel_dict = {}
        minimum = 0
        first = True
        already_computed = []
        for start_position in initial_state:
            if start_position in already_computed:
                continue
            for end_position in initial_state:
                if start_position != end_position:
                    if fuel_dict.get(start_position, None):
                        fuel_dict[start_position] = fuel_dict[start_position] + abs(start_position - end_position)
                    else:
                        fuel_dict[start_position] = abs(start_position - end_position)
            if first:
                minimum = fuel_dict[start_position]
                first = False
            if fuel_dict[start_position] < minimum:
                minimum = fuel_dict[start_position]
            already_computed.append(start_position)

    print(f"part1 minimum fuel: {minimum}")


def sum_first_n(n: int):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def part2():
    with open("input7", "rb") as data:
        initial_state = list(map(int, data.readline().decode("utf8").split()[0].split(",")))

        minimum = 0
        first = True
        for point in range(min(initial_state), max(initial_state) + 1):
            distance = 0
            #compute distance for all the points in the initial state
            for start_position in initial_state:
                if start_position != point:
                    abs_value = abs(start_position-point)
                    distance = distance + (abs_value*(abs_value + 1))/2
            if first:
                minimum = distance
                first = False
            elif minimum > distance:
                minimum = distance

        print(f"part 2 minimum fuel: {minimum}")


part1()

part2()



