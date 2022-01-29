from typing import List

illegal_char_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
open_chars = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']
open_close_mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def part1(lines: List[str]) -> List[str]:
    illegals = []

    for line in lines:
        char_stack = []
        for char in line:
            if char in open_chars:
                # keep track of open chars
                char_stack.append(char)
            else:
                open_char = char_stack.pop()
                if open_close_mapping[open_char] != char:
                    illegals.append(char)
                    break
    return illegals


def compute_points(illegals: List[str]) -> int:
    points = 0
    for illegal in illegals:
        points += illegal_char_points[illegal]
    return points


with open("input10-sample", "rb") as data:
    lines = [list(line.decode("utf8").split()[0]) for line in data]

illegal_list = part1(lines)
print(f"illegal character score: {compute_points(illegal_list)}")
