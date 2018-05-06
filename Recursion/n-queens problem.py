

def is_attacked(board, x, y, N):
	
	# for row
	for i in xrange(0, N):
		if board[x][i] == 1:
			return True

	# for column
	for j in xrange(0, N):
		if board[i][y] == 1:
			return True

	# for diagonals
	for i in xrange(0, N):
		for j in xrange(0,N):
			if ((i-j)==(x-y)) and board[i][j] == 1:
				return True

			if (i+j)==(x+y) and board[i][j] == 1:
				return True

	return False


def N_Queens(board, N):

	if N == 0:
		return True

	l = len(board[0])

	for i in range(0, l):
		for j in range(0, l):

			if not is_attacked(board, i, j, l):
				board[i][j] = 1

				if N_Queens(board, N-1):
					return True

				board[i][j] = 0

	return False

N = 4
board = [[0 for i in range(N)] for j in range(N+1)]
N_Queens(board, N)
print board
