# sudoku_solver_smart.py

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()
    print()

def is_valid(board, num, row, col):
    # Row
    for j in range(9):
        if board[row][j] == num:
            return False
    # Column
    for i in range(9):
        if board[i][col] == num:
            return False
    # 3x3 box
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def find_candidates(board, row, col):
    """Return a list of possible numbers for (row,col)."""
    candidates = []
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            candidates.append(num)
    return candidates

def find_best_cell(board):
    """Find empty cell with fewest candidates (MRV heuristic)."""
    best_cell = None
    best_candidates = None

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                candidates = find_candidates(board, i, j)
                if best_candidates is None or len(candidates) < len(best_candidates):
                    best_candidates = candidates
                    best_cell = (i, j)
                if len(best_candidates) == 1:  # best possible
                    return best_cell, best_candidates
    return best_cell, best_candidates

def solve(board):
    cell, candidates = find_best_cell(board)
    if not cell:  # no empty cells left
        return True
    row, col = cell

    for num in candidates:  # try only valid candidates
        board[row][col] = num
        if solve(board):
            return True
        board[row][col] = 0
    return False

# Example Sudoku (harder one)
sudoku_board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

print("Sudoku Puzzle:")
print_board(sudoku_board)

if solve(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
