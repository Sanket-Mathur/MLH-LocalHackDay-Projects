import os

def print_grid(grid):
    """
    Printing the grid with blanks as underscores.
    Parameters:
        grid: The sudoku grid.
    """
    for row in grid:
        for col in row:
            print('{}'.format(col if col != 0 else '_'), end = ' ')
        print()

def is_valid(grid, row, col, i):
    """
    Checking is the move is valid at the given position.
    Parameters:
        grid: The sudoku grid.
        row: The row of the move.
        col: The column of the move.
        i: The value of the move.
    Returns:
        True if the move is valid, False otherwise.
    """
    # Checking if same element exists in the row.
    for x in range(9):
        if grid[row][x] == i:
            return False
    
    # Checking if same element exists in the column.
    for x in range(9):
        if grid[x][col] == i:
            return False
    
    # Checking if same element exists in the 3x3 box.
    for x in range(row - row % 3, row - row % 3 + 3):
        for y in range(col - col % 3, col - col % 3 + 3):
            if grid[x][y] == i:
                return False
    
    return True

def solve(grid, row = 0, col = 0, display = False):
    """
    Solves the given sudoku grid.
    Parameters:
        grid: The sudoku grid.
        row: The row of the move. Default is 0.
        col: The column of the move. Default is 0.
        display: If True, the grid will be printed after each move. Default is False.
    Returns:
        True if the puzzle is solved, False otherwise.
    
    NOTE: Displaying the grid after each move heavily effects the execution time.
    """
    # Solved successfully.
    if row == 8 and col == 9:
        return True
    
    # Jump to next row
    if col == 9:
        row += 1
        col = 0
    
    if grid[row][col] != 0:
        return solve(grid, row, col + 1)
    
    # Try to solve with each number from 1 to 9
    for i in range(1, 10):
        if is_valid(grid, row, col, i):
            grid[row][col] = i

            if display:
                os.system('cls')
                print_grid(grid)

            if solve(grid, row, col + 1):
                return True

        # Backtracking step
        grid[row][col] = 0
        
        if display:
            os.system('cls')
            print_grid(grid)
    
    return False

print('Enter your sudoku puzzle with spaces in between using _ as empty blocks:')
l = []
for i in range(9):
    l.append(list(map(int, input().replace('_', '0').split())))

if solve(l):
    print_grid(l)
else:
    print('No solution exists')