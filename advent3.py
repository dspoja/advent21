from typing import List, Tuple


def compute_gamma_and_epsilon(input_data: List) -> Tuple[str, str, List]:
    gamma_bits = []
    epsilon_bits = []
    bin_data = []
    first_pass = True
    for data in input_data:
        if type(data) is not str:
            data_point = data.decode("utf-8").strip()
        else:
            data_point = data
        if first_pass:
            one_counts = [0] * len(data_point)
            zero_counts = [0] * len(data_point)
            first_pass = False
        for i in range(len(data_point)):
            if data_point[i] == "1":
                one_counts[i] += 1
            else:
                zero_counts[i] += 1
        bin_data.append(data_point)

    for i in range(len(one_counts)):
        if zero_counts[i] > one_counts[i]:
            gamma_bits.append("0")
            epsilon_bits.append("1")
        else:
            gamma_bits.append("1")
            epsilon_bits.append("0")

    return gamma_bits, epsilon_bits, bin_data


def compute_power_consumption_part1():
    with open("input3", "rb") as data_points:
        gamma_bits, epsilon_bits, _ = compute_gamma_and_epsilon(data_points)
        # now figure out the gamma and epsilon rates
        gamma_rate_binary = "".join(gamma_bits)
        epsilon_rate_binary = "".join(epsilon_bits)
        # convert binary string to int
        gamma_rate_int = int(gamma_rate_binary, base=2)
        epsilon_rate_int = int(epsilon_rate_binary, base=2)

        print(f"power consumption: {gamma_rate_int * epsilon_rate_int}")


def compute_power_consumption_part2():
    with open("input3", "rb") as data_points:
        gamma_bits, epsilon_bits , bin_data = compute_gamma_and_epsilon(data_points)

    # now loop through the data again to discard unneeded data
    gamma_dict = {data:int(data, base=2) for data in bin_data}
    epsilon_dict = {data: int(data, base=2) for data in bin_data}
    gamma_data = [data for data in gamma_dict.keys()]
    epsilon_data = [data for data in epsilon_dict.keys()]
    data_length = len(gamma_bits)
    for i in range(data_length):
        gamma_bits, _, _ = compute_gamma_and_epsilon(gamma_data)
        _, epsilon_bits, _ = compute_gamma_and_epsilon(epsilon_data)
        for data_point in gamma_data:
            if data_point[i] != gamma_bits[i] and len(gamma_dict) > 2:
                gamma_dict.pop(data_point, None)
        for data_point in epsilon_data:
            if data_point[i] != epsilon_bits[i] and len(epsilon_dict) > 2:
                epsilon_dict.pop(data_point, None)
        gamma_data = [data for data in gamma_dict.keys()]
        epsilon_data = [data for data in epsilon_dict.keys()]

    # decide on the last candidate
    gammas = [gamma for gamma in gamma_dict.keys()]
    if len(gammas) == 2:
        if int(gammas[0][data_length-1]) > int(gammas[1][data_length-1]):
            oxygen_rate = gammas[0]
        else:
            oxygen_rate = gammas[1]
    else:
        oxygen_rate = gammas[0]

    epsilons = [epsilon for epsilon in epsilon_dict.keys()]
    if len(epsilons) == 2:
        if int(epsilons[0][data_length-1]) < int(epsilons[1][data_length-1]):
            co2_rate = epsilons[0]
        else:
            co2_rate = epsilons[1]
    else:
        co2_rate = epsilons[0]

    oxygen_rate = int(oxygen_rate, base=2)
    co2_rate = int(co2_rate, base=2)

    print(f"life support rating {oxygen_rate} * {co2_rate}: {oxygen_rate * co2_rate}")


compute_power_consumption_part1()
compute_power_consumption_part2()

