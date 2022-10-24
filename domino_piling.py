def dominoPiling(m, n):
    board_squares = m * n
    max_no_of_dominoes = board_squares//2
    return max_no_of_dominoes
	
print(dominoPiling(7,3))