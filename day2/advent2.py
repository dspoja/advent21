def navigate_part1() -> int:
    with open('input2', "rb") as inputs:
        horizontal = 0
        vertical = 0
        for direction_input in inputs:
            direction = direction_input.split()
            name = direction[0].decode("utf-8")
            num_units = int(direction[1])
            if name == "forward":
                horizontal += num_units
            if name == "up":
                vertical -= num_units
            if name == "down":
                vertical += num_units
        return horizontal * vertical


def navigate_part2() -> int:
    with open('input2', "rb") as inputs:
        horizontal = 0
        vertical = 0
        aim = 0
        for direction_input in inputs:
            direction = direction_input.split()
            name = direction[0].decode("utf-8")
            num_units = int(direction[1])
            if name == "forward":
                horizontal += num_units
                vertical += aim * num_units
            if name == "up":
                aim -= num_units
            if name == "down":
                aim += num_units
        return horizontal * vertical

final_depth = navigate_part1()
print(f"Final depth 1 is {final_depth}")

final_depth = navigate_part2()
print(f"Final depth 2 is {final_depth}")
