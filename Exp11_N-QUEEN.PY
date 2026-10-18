N = int(input("Enter the value of N: "))

board = [0] * N

def IS_SAFE(row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def NQUEEN(row):
    if row == N:
        print("Solution:")
        for i in range(N):
            for j in range(N):
                if board[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()
        return

    for col in range(N):
        if IS_SAFE(row, col):
            board[row] = col
            NQUEEN(row + 1)
            board[row] = -1


NQUEEN(0)
