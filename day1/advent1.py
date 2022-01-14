
def simple_count():
    increase_count = 0
    with open('input1', "rb") as depths:
        current_depth = int(depths.readline())
        for depth in depths:
            if current_depth < int(depth):
                increase_count+=1
            current_depth = int(depth)

    print(f"Simple: Increase count is {increase_count}")

def advanced_count():
    increase_count = 0
    with open('input1', "rb") as depths:
        previous_sum = 0
        triplet = []
        for i, depth in enumerate(depths):
            if i < 3:
                triplet.append(int(depth))
                previous_sum = previous_sum + int(depth)
            else:
                current_sum = previous_sum - triplet[i%3] + int(depth)
                if previous_sum < current_sum:
                    increase_count += 1
                triplet[i%3] = int(depth)

    print(f"Advanced: Increase count is {increase_count}")

simple_count()
advanced_count()