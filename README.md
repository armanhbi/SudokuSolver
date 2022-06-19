# SudokuSolver

An easy Sudoku Solver programmed in one night.
The solver works by recursively putting a number from 1-10 at any free spot and trying as long as all of the spots are filled. If one spot does not work for all numbers, the algorithm goes back to the last recursive step and tries with the next number and so on. isPossibleToPlace() checks every row, column and diagonal if the number is allowed there.
Later implemented a small animation in the terminal for visually seeing the recursive function and a basic timer to display the time it needed.
Instead of printSudoku(), I could have used the matrix library but whatever.
