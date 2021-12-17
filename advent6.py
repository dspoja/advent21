import copy


def compute_size(state, day=0):
    size = 0
    for key in state.keys():
        size += state.get(key) if state.get(key) else 0
    print(f"after {day} size={size}")


def compute_state():
    with open("input6", "rb") as data:
        initial_state = list(map(int, data.readline().decode("utf8").split()[0].split(",")))
        print(f"starter fish: {initial_state}")

        #initilaize dict for storing counts
        current_state = {i: None for i in range(9)}
        new_state = {i: None for i in range(9)}
        #initalize current state
        for fish in initial_state:
            if current_state.get(fish, None):
                current_state[fish] +=1
            else:
                current_state[fish] = 1

        number_of_days = 256
        print(f"Initial state: {initial_state}")
        for day in range(1, number_of_days+1):
            for key in sorted(current_state.keys()):
                if key > 0 and current_state[key] is not None:
                    if key-1 != 6 and key-1 != 8:
                        new_state[key-1] = current_state[key]
                    else:
                        new_state[key-1] = new_state[key-1] + current_state[key] if new_state.get(key-1) is not None else current_state[key]
                    if key != 8 and key != 6:
                        new_state[key] = None
                elif key == 0:
                    if current_state[0] is not None:
                        new_state[6] = current_state[key]
                        new_state[8] = current_state[key]
                        new_state[0] = None
                    else:
                        new_state[6] = None
                        new_state[8] = None
            current_state = copy.deepcopy(new_state)
            compute_size(current_state, day)

compute_state()