from typing import List, Tuple

illegal_char_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
incomplete_char_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
open_chars = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']
open_close_mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def part1(lines: List[str]) -> Tuple[List[str], List[str]]:
    illegals = []
    incomplete_lines = []
    for line in lines:
        char_stack = []
        has_illegal_char = False
        for char in line:
            if char in open_chars:
                # keep track of open chars
                char_stack.append(char)
            else:
                open_char = char_stack.pop()
                if open_close_mapping[open_char] != char:
                    illegals.append(char)
                    has_illegal_char = True
                    break
        if not has_illegal_char:
            incomplete_lines.append(line)
    return illegals, incomplete_lines


def part2(incompletes: List[str]) -> List[int]:
    scores = []
    for line in incompletes:
        char_stack = []
        for char in line:
            if char in open_chars:
                # keep track of open chars
                char_stack.append(char)
            else:
                open_char = char_stack.pop()
        # now complete the chars and compute the score
        score = 0
        char_stack.reverse()
        for char in char_stack:
            score = score*5 + incomplete_char_points[open_close_mapping[char]]
        scores.append(score)

    return scores


def compute_points(illegals: List[str]) -> int:
    points = 0
    for illegal in illegals:
        points += illegal_char_points[illegal]
    return points


with open("input10", "rb") as data:
    lines = [list(line.decode("utf8").split()[0]) for line in data]

illegal_list, incomplete_lines = part1(lines)
print(f"illegal character score: {compute_points(illegal_list)}")

incomplete_scores = part2(incomplete_lines)
print(f"all scores: {incomplete_scores}")
incomplete_scores.sort()
middle = len(incomplete_scores)//2
print(f"Middle score: {incomplete_scores[middle]}")

