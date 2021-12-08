from typing import List

def construct_draws_and_boards():
    with open("input4", "rb") as data:
        first_row = True
        boards = []
        for line in data:
            line = line.decode("utf-8").strip()
            if first_row:
                draws = line.split(",")
                first_row = False
                board = []
                continue
            if len(line.strip()) == 0:
                if board:
                    boards.append(board)
                board = []
                continue
            else:
                board.append(line.split())
        if board:
            boards.append(board)
    return draws, boards


def check_board(number: int, board_num: int, board: List, board_counter: List) -> bool:
    for i, row in enumerate(board):
        try:
            index = row.index(number)
            row[index] = int(row[index])
            # update row counter and check for wins
            board_counter[board_num]["rows"][i] = board_counter[board_num]["rows"][i] + 1
            if board_counter[board_num]["rows"][i] == len(row):
                return True
            # update column counter and check for wins
            board_counter[board_num]["columns"][index] = board_counter[board_num]["columns"][index] + 1
            if board_counter[board_num]["columns"][index] == len(board_counter[board_num]["columns"]):
                return True
        except ValueError:
            # so it is not in the list, move to the next number
            pass

def compute_winning_score(board: List, number: int) -> int:
    sum = 0
    for row in board:
        for num in row:
            if type(num) is str:
                sum+= int(num)
    return int(number) * sum


def play_bingo(let_the_squid_win: bool) -> int:
    draws, boards = construct_draws_and_boards()
    #initialize board_counter
    board_counter = []
    for board in boards:
        rows = [0] * len(board[0])
        columns = [0] * len(board)
        board_counter.append(
            {"rows": rows, "columns": columns})

    # draw numbers and check boards for winners
    winners = []
    have_winner = False
    for number in draws:
        for board_num, board in enumerate(boards):
            #check the numbers against the board
            if check_board(number, board_num, board, board_counter):
                winnig_score = compute_winning_score(board, number)
                if let_the_squid_win:
                    if board_num not in winners:
                        winners.append(board_num)
                        if len(winners) == len(boards):
                            have_winner = True
                            break
                else:
                    have_winner = True
                    break
        if have_winner:
             break

    return winnig_score

print(f"Part 1 Bingo: {play_bingo(False)}")

print(f"Part 1 Bingo: {play_bingo(True)}")
