import time

sudoku =[[5,3,0,0,7,0,0,0,0]
        ,[6,0,0,1,9,5,0,0,0]
        ,[0,9,8,0,0,0,0,6,0]
        ,[8,0,0,0,6,0,0,0,3]
        ,[4,0,0,8,0,3,0,0,1]
        ,[7,0,0,0,2,0,0,0,6]
        ,[0,6,0,0,0,0,2,8,0]
        ,[0,0,0,4,1,9,0,0,5]
        ,[0,0,0,0,8,0,0,7,9]]

def printSudoku():
    global sudoku
    print("#####################")
    for x in range(9):
        row = "# "
        if (x == 3 or x == 6):
            print("# _________________ #")
        for y in range(9):
            row += str(sudoku[x][y])
            if (y == 2 or y == 5):
                row += "|"
            elif (y != 8):
                row += ","
        print(row + " #")
    print("#####################")

def isPossibleToPlace(x,y,value):
    global sudoku
    #x is actually y and y is actually x
    for i in range(9): #row check
        if (sudoku[x][i] == value):
            return False
    for i in range(9): #column check
        if (sudoku[i][y] == value):
            return False
    x3x3grid = (x//3) * 3
    y3x3grid = (y//3) * 3
    for a in range(3): #diagonal check
        for b in range(3):
            if (sudoku[x3x3grid + a][y3x3grid + b] == value):
                return False
    return True

def solveRecursive():
    global sudoku
    for x in range(9):
        for y in range(9):
            if (sudoku[x][y] == 0):
                for value in range(1,10):
                    if (isPossibleToPlace(x,y,value)):
                        sudoku[x][y] = value
                        printSudoku()
                        solveRecursive()
                        sudoku[x][y] = 0
                return
    printSudoku()

print("\nTo Solve:")
printSudoku()
print("\nSolved:")
start = round(time.time() * 1000)
solveRecursive()
end = round(time.time() * 1000)
delta = end-start
print()
print("Time needed: " + str(delta) + "ms\n")
