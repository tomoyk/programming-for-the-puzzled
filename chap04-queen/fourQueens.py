from noConflicts import *

def FourQueens(n=4):
    board = [ [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0] ]
    for i in range(n):
        board[i][0] = 1
        for j in range(n):
            board[j][1] = 1
            if noConflicts(board, 1, j, n):
                for k in range(n):
                    board[k][2] = 1
                    if noConflicts(board, 2, k, n):
                        for m in range(n):
                            board[m][3] = 1
                            if noConflicts(board, 3, m, n):
                                print(board)
                            board[m][3] = 0
                    board[k][2] = 0
            board[j][1] = 0
        board[i][0] = 0
    return

if __name__ == '__main__':
    FourQueens()
