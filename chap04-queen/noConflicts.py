def noConflicts(board, current, qindex, n):
    """
    衝突がないか調べる
    board: 配列として盤面の状態を渡す
    current: 列を表す
    qindex: QueenIndex 行を表す
    n: 盤面の大きさ(N x N)
    """
    
    """
    行 qindex にクイーンがすでにあるかをチェック
    """
    for j in range(current):
        if board[qindex][j] == 1:
            return False

    """
    斜め左上方向の取り合いを盤面の端に向かってqindexとcurrentを
    減らしてチェック
    """
    k = 1
    while qindex - k >= 0 and current - k >= 0:
        if board[qindex - k][current - k] == 1:
            return False
        k += 1
    
    """
    斜め左下方向の取り合いを盤面の端になるまでcurrentを減らして
    qindexを増やしながらチェック
    """
    k = 1
    while qindex + k < n and current - k >= 0:
        if board[qindex + k][current - k] == 1:
            return False
        k += 1

    return True

if __name__ == '__main__':
    my_board = [
                [0, 0, 0, 1],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [1, 0, 1, 0],
            ]
    N = len(my_board)
    for i in range(len(my_board)):
        for j in range(len(my_board[i])):
            print('({}, {}) \t'.format(i, j), end='')
            if noConflicts(my_board, i, j, N):
                print("not conflicted")
            else:
                print("conflicted")
