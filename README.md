# SudokuSolver
The Sudoku Solver is a Python program that solves Sudoku puzzles.

 The program takes an incomplete Sudoku puzzle as input and fills in the missing numbers to complete the puzzle. It uses an efficient backtracking algorithm to find the solution.
 
 Enter the Sudoku Puzzle as numpy array with any size (n x n), for example:
 
 board = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 0, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0]])
The program will solve the Sudoku puzzle and display the solved puzzle in the command-line interface.
