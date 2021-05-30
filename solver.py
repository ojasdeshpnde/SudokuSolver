
def gridPrint(grid):
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            print(grid[i][j],end=" ")
        print()

    print()
    print()

def isFull(grid):
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if grid[i][j] == 0:
                return False

    return True

def findNext(grid):
    row = -1
    col = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                row = i
                col = j
                break
        else:
            continue
        break
    if(row >= 0):
        for i in range(1,10):
            if doesWork(grid,row,col,i):
                grid[row][col] = i
                findNext(grid)
                if not isFull(grid):
                    grid[row][col] = 0
    return grid





def doesWork(grid, row, col, num):
    for i in range(0,len(grid)):
        if grid[row][i] == num:
            return False
    for i in range(0,len(grid)):
        if grid[i][col] == num:
            return False
    gRow = int(row/3)*3
    gCol = int(col/3)*3
    for i in range(gRow,gRow+3):
        for j in range(gCol,gCol+3):
            if grid[i][j] == num:
                return False

    return True






#put your own sudoku grid here
grid = [[0,4,0,5,9,2,0,0,0],[3,0,0,0,4,8,0,1,9],[0,6,9,7,0,0,0,4,0],[0,2,4,1,6,5,9,7,0],[0,5,3,2,7,4,0,0,0],[0,1,0,0,0,0,4,0,0],[0,3,1,9,5,0,0,0,4],[6,0,0,0,0,1,3,0,5],[4,0,5,3,0,0,1,2,7]]
gridPrint(grid)
print("Solution:")
gridPrint(findNext(grid))


