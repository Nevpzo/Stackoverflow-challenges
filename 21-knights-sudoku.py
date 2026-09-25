# --- Parameters
PRINT_MODE = "BLOCK" # "PRETTY" or "BLOCK"

board = [
    [1,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,0,8,0,0,0,0,6,0],
    [2,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,0,0,0,0,0],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

l_sum_min = 19

l_paths = [
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 8), (0, 7), (0, 6), (1, 6)],
    [(8, 0), (8, 1), (8, 2), (7, 2)],
    [(8, 8), (7, 8), (6, 8), (6, 7)],
]

# --- Helper printing functions
def printslice(slice, row, start_col, l_paths):
    colors = ['\033[94m', '\033[92m', '\033[93m', '\033[91m']
    s = " "

    for col in range(start_col, start_col + len(slice)):
        value = slice[col - start_col]

        color = None

        for i, path in enumerate(l_paths):
            if (row, col) in path:
                color = colors[i]
                break

        if color:
            s += color + str(value) + '\033[0m' + " "
        else:
            s += str(value) + " "

    return s

def sudokprint(board, l_paths, print_mode="PRETTY"):
    if print_mode == "BLOCK":
        for row in board:
            print("".join(str(number) for number in row))
        return

    if print_mode != "PRETTY":
        raise ValueError("print_mode must be 'PRETTY' or 'BLOCK'")

    for row in range(9):
        print(
            f"{printslice(board[row][:3], row, 0, l_paths)}|"
            f"{printslice(board[row][3:6], row, 3, l_paths)}|"
            f"{printslice(board[row][6:9], row, 6, l_paths)}"
        )

        if row == 2 or row == 5:
            print('-------+-------+------')

def print_solutions(solutions, l_paths, print_mode="PRETTY"):
    for i, solution in enumerate(solutions):
        sudokprint(solution, l_paths, print_mode)

        if i < len(solutions) - 1:
            print()

# --- Solver
def is_valid(row_index, column_index, number):
    # --- Classic constraints
    # Row
    for n in range(9):
        if board[row_index][n] == number:
            return False

    # Column
    for n in range(9):
        if board[n][column_index] == number:
            return False

    # 3x3 square
    square_col = (column_index // 3) * 3
    square_row = (row_index // 3) * 3

    for n in range(3):
        for m in range(3):
            if board[square_row + n][square_col + m] == number:
                return False

    # --- L-path constraints
    for path in l_paths:
        if (row_index, column_index) in path:

            current_sum = 0
            empty_cells = 0

            for row, col in path:
                value = board[row][col]

                if (row, col) == (row_index, column_index):
                    value = number

                if value == 0:
                    empty_cells += 1
                else:
                    current_sum += value

            if current_sum >= l_sum_min:
                continue

            used = set()

            for row, col in path:
                value = board[row][col]
                if value != 0:
                    used.add(value)

            used.discard(number)

            possible = [
                n for n in range(1, 10)
                if n not in used
            ]

            possible.sort(reverse=True)
            max_possible_sum = current_sum + sum(
                possible[:empty_cells]
            )

            if max_possible_sum < l_sum_min:
                return False
    return True

solutions = []

def solve():
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                for number in range(1, 10):
                    if is_valid(row, column, number):
                        board[row][column] = number
                        solve()
                        board[row][column] = 0
                return

    solutions.append([row[:] for row in board])


# --- Printing solutions
solve()
print(f"\nFound {len(solutions)} solution(s).\n")
print_solutions(solutions, l_paths, PRINT_MODE)