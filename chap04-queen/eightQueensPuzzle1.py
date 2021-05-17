"""
衝突がないかチェック
"""
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current -i == abs(board[current] - board[i])):
            return False
    return True


"""
-1  =>  列にクイーンが無いことを意味する．
 0  =>  その列の1行目にクイーンがあることを意味する．
 3  =>  その列の4行目にクイーンがあることを意味する．
"""
def EightQueens(num_of_answers: int, n: int = 8):
    current_num_of_ans = 1
    board = [-1] * n
    for i in range(n):
        board[0] = i
        for j in range(n):
            board[1] = j
            if not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if not noConflicts(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if noConflicts(board, 7):
                                        current_num_of_ans += 1
                                        if current_num_of_ans >= num_of_answers:
                                            return
                                        print(board)
    return


if __name__ == "__main__":
    EightQueens(10, 8)