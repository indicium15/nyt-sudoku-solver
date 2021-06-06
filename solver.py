from scraper import *

def print_board(board):
    for i in range(len(board)): #Iterate thorugh rows
        if i % 3 == 0 and i != 0: 
            print('----------------------') #Print separator after every three rows
        for j in range(len(board[0])): #Iterate through columns
            if j % 3 == 0 and j != 0:
                print(" | ",end="") #Print separator after every three columns
            if j == 8:
                print(board[i][j]) #Last entry for row
            else:
                print(str(board[i][j]) + ' ', end ="") #Print entry with space

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])): #for j in range of length of a row
            if board[i][j] == 0:
                #print(i,j) Debugging
                return(i,j)
    return None

def is_valid(board, number, position): #position is a tuple, using 0 = x value of position and 1 = y value of position
    #Check all rows
    for i in range(len(board[0])): #for i in range of length of a row
        if board[position[0]][i] == number and position[1] != i:
            return False
    #Check all columns        
    for i in range(len(board[0])):
        if board[i][position[1]] == number and position[0] != i:
            return False
    #Check box
    x_box = position[1] // 3
    y_box = position[0] // 3

    for i in range(y_box *3, y_box*3 + 3):
        for j in range(x_box * 3, x_box * 3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True        

def solve_board(board):
    empty = find_empty(board)
    if not empty:
        return True #There are no more empty cells in the sodoku - it has been solved
    else:
        x_board, y_board = empty
    for i in range(1,10):
        if is_valid(board, i, (x_board, y_board)):
            board[x_board][y_board] = i
            if solve_board(board):
                return True #Correct value in the cell - move on
            board[x_board][y_board] = 0 #Wrong value
    return False

def main(url):
    test_board = get_board(url)
    print_board(test_board)
    solve_board(test_board)
    print('*************************')
    print_board(test_board)

main('https://www.nytimes.com/puzzles/sudoku/hard') #sample