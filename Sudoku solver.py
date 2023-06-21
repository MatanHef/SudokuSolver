import math
import numpy as np

class sudoku_solver:
    def __init__(self,board):
        self.board = board
        self.board_size = len(self.board)
        self.nums = list(range(1,self.board_size+1))
        self.mini_board = int(math.sqrt(self.board_size))
        self.stack= {} #containe current attempt
        self.counter_stack = 0
        self.cursor= (0,0) #point to last square that changed
    def solve(self):
        '''
        scan the board until square contain 0
        try to add a number
        if succeeded start scan again, else go to change
        '''
        row=0
        while row < (self.board_size):
            col=0
            while col < (self.board_size):
                if self.board[row][col] == 0:
                    for num in self.nums:
                        if self.check_rc(row, col, num) and self.check_miniboard(row, col, num) and self.check_fail_attemps(
                                row, col, num):
                            self.add_number(row, col, num)
                            col=-1
                            row=0
                            break
                    if col !=-1:
                        self.change()
                        col = -1
                        row = 0
                col+=1
            row+=1
        return (self.board)
    def change(self):
        '''
        take the last number added,
        try a bigger number
        else delete him
        repeat
        '''
        row= self.stack[self.counter_stack][0][0]
        col = self.stack[self.counter_stack][0][1]
        for num in range (self.stack[self.counter_stack][1]+1, self.nums[-1]+1):
            if self.check_rc(row, col, num) and self.check_miniboard(row, col, num) and self.check_fail_attemps(row, col, num):
                self.add_number(row, col, num)
                return
        del self.stack[self.counter_stack]
        self.board[row][col] = 0
        self.counter_stack -= 1
        self.cursor = (row, col)
        self.flag = 0
        return (self.change())
    def add_number(self,row,col,num):
        '''add a number to the board'''
        self.board[row][col] = num
        self.counter_stack += 1
        self.stack[self.counter_stack] = ((row, col), num)
        self.cursor=(row,col)
        self.flag=1
        return
    def check_fail_attemps(self,row,col,num):
        '''check not to repeat failed attempts'''
        if (row,col) == self.cursor:
            if self.stack != {}:
                if self.flag==0:
                    return False
        return True
    def check_rc(self,row,col,num):
        '''check the number not in the same row or column'''
        for i in range (self.board_size):
            if self.board[row][i] == num:
                return False
            if self.board[i][col] == num:
                return False
        return True
    def check_miniboard(self,row,col,num):
        '''check the number not in the mini-board'''
        a = int(row // self.mini_board)
        b = int(col // self.mini_board)
        miniboard= board[a*(self.mini_board):(a+1)*(self.mini_board),b*(self.mini_board):(b+1)*(self.mini_board)]
        for i in range(self.mini_board):
            for j in range(self.mini_board):
                if int(miniboard[i][j]) == num:
                    return False
        return True

'''
example
board = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 0, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0]])
'''

example = sudoku_solver(board)
(print(sudoku_solver.solve(s)))
