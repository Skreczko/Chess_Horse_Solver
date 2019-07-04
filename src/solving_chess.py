BOARD = []
POSSIBLE_MOVES = (
	(-2, -1),
	(-2, 1),
	(2, -1),
	(2, 1),
	(-1, -2),
	(-1, 2),
	(1, -2),
	(1, 2),)
SOLID = 0

def check_chess(x, y, movements=1):
	global SOLID, BOARD
	BOARD[x][y] = movements
	if SOLID == 0:
		if movements == len(BOARD)**2:
			SOLID = 1						#needed for interrupting recursion after finding first solutoin
		for item in POSSIBLE_MOVES:
			if possible_moves(item[0]+x, item[1]+y):
				check_chess(item[0]+x, item[1]+y, movements+1)
		if SOLID == 0 and movements < len(BOARD)**2:
			BOARD[x][y]=0

def possible_moves(x,y):
	return (x>=0 and x<len(BOARD)) and (y>=0 and y<len(BOARD)) and BOARD[x][y]==0

def get_chess_solution(x, y, board=8):
	global BOARD, SOLID
	BOARD = list([0] * board for x in range(board))
	check_chess(x, y)
	SOLID = 0
	return BOARD













