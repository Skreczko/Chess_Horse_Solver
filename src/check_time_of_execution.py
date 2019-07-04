import time
import sys
BOARD = list(['ee']*5 for x in range(5))
POSSIBLE_MOVES = (
	(-2, -1),
	(-2, 1),
	(2, -1),
	(2, 1),
	(-1, -2),
	(-1, 2),
	(1, -2),
	(1, 2),)
movements = 1

start = time.time()



"""			69.02044939994812						"""

# def main():
# 	check_chess(0,0)
# 	print(BOARD)
#
# def possible_moves(x,y):
# 	ALLOWED_MOVES = []
# 	for item in POSSIBLE_MOVES:
# 		if (item[0]+x>=0 and item[0]+x<6) and (item[1]+y>=0 and item[1]+y<6) and (BOARD[item[0]+x][item[1]+y]=='ee'):
# 			ALLOWED_MOVES += [(item[0]+x,item[1]+y)]
# 	return ALLOWED_MOVES
#
#
# def check_chess(x, y):
# 	global BOARD, start
# 	global movements
# 	BOARD[x][y] = movements
# 	if movements == 36:
# 		end = time.time()
# 		print(BOARD)
# 		print(end - start)
# 		sys.exit()
# 	allowed_moves = possible_moves(x,y)
# 	if allowed_moves:
# 		for item in allowed_moves:
# 			movements += 1
# 			check_chess(item[0], item[1])
# 	BOARD[x][y]='ee'
# 	movements -= 1
#
# main()



""" 		66.73857593536377 		 """

# def check_chess(x, y, movements=1):
# 	global BOARD, start
# 	BOARD[x][y] = movements
# 	if movements == 25:
# 		end = time.time()
# 		print(BOARD)
# 		print(end - start)
# 		sys.exit()
# 	allowed_moves = possible_moves(x,y)
# 	if allowed_moves:
# 		for item in allowed_moves:
# 			check_chess(item[0], item[1], movements+1)
# 	BOARD[x][y]='ee'


# def check_chess(x, y, movements=1):
# 	global BOARD
# 	if movements < 16:
# 		BOARD[x][y] = movements
# 		print(BOARD)
# 		print(movements)
# 		moves = possible_moves(x,y)
# 		if moves:
# 			for item in moves:
# 				check_chess(item[0],item[1], movements+1)
# 		BOARD[x][y] = 'ee'
# 		# else:
# 		# 	if movements<16:
# 		# 		BOARD[x][y] = 'ee'
# 		# 	return BOARD
#
# def main():
# 	check_chess(0,0)
#
# def possible_moves(x,y):
# 	ALLOWED_MOVES = []
# 	for item in POSSIBLE_MOVES:
# 		if (item[0]+x>=0 and item[0]+x<4) and (item[1]+y>=0 and item[1]+y<4) and (BOARD[item[0]+x][item[1]+y]=='ee'):
# 			ALLOWED_MOVES += [(item[0]+x,item[1]+y)]
# 	return ALLOWED_MOVES
#
# main()


""" 		57.07637858390808 		 """

def check_chess(x, y, movements):
	global BOARD, start
	BOARD[x][y] = movements
	if movements == 25:
		end = time.time()
		print(BOARD)
		print(end - start)
	for item in POSSIBLE_MOVES:
		if possible_moves(item[0]+x, item[1]+y):
			check_chess(item[0]+x, item[1]+y, movements+1)
	BOARD[x][y]='ee'


def main():
	check_chess(0,0, 1)
	print(BOARD)

def possible_moves(x,y):
	return (x>=0 and x<5) and (y>=0 and y<5) and BOARD[x][y]=='ee'

main()

""" 	60.15519666671753 		 """

# def check_chess(x, y, movements):
# 	global BOARD, start
# 	BOARD[x][y] = movements
# 	if movements == 36:
# 		end = time.time()
# 		print(BOARD)
# 		print(end - start)
# 		sys.exit()
# 	for item in POSSIBLE_MOVES:
# 		if (item[0]+x>=0 and item[0]+x<6) and (item[1]+y>=0 and item[1]+y<6) and BOARD[item[0]+x][item[1]+y]=='ee':
# 			check_chess(item[0]+x, item[1]+y, movements+1)
# 	BOARD[x][y]='ee'
#
#
# def main():
# 	check_chess(0,0, 1)
# 	print(BOARD)
#
# main()