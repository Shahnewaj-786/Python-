size = 4


def printBoard(board):
    for i in range(size):
        for j in range(size):
            print(board[i][j], end=" "),
        print()


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, size, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQ(board, col):
    if col >= size:
        return True

    for i in range(size):
        if isSafe(board, i, col):
            board[i][col] = 1

            if solveNQ(board, col + 1) == True:
                return True
            board[i][col] = 0

    return False


def solve():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if solveNQ(board, 0) == False:
        return False

    printBoard(board)


solve()