# ---------------------------------------------------------------
# Suduko solver - takes input and calculates solution (easy
#   puzzles only
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Initialise libraries, functions and classes
# ---------------------------------------------------------------

import numpy as np

def midStr(s, c):
    return s[c:c+1]

class cell:
    def __init__(self, startValue, endValue, possibleValues):
        self.startValue = startValue
        self.endValue = endValue
        self.possibleValues = possibleValues

grid = np.empty((9, 9), dtype=object)


# ---------------------------------------------------------------
# Load grid - this should be a UI in which values can be type.
#   Coud be entered as series of values, values/grid position etc
#   eg rowOfValues = raw_input('Enter row %b' % row_no
#   But in this case loaded from strings
# ---------------------------------------------------------------

def loadGrid():

    for row in range(9):                    # load arrays with cell objects
        for col in range(9):
            grid[row, col] = cell(0,0,'')

    for col in range(9):                    # for each col, load each row with corresponding test data
        grid[0, col].startValue = int(midStr('003004010', col))
        grid[1, col].startValue = int(midStr('254301800', col))
        grid[2, col].startValue = int(midStr('001870400', col))
        grid[3, col].startValue = int(midStr('600008040', col))
        grid[4, col].startValue = int(midStr('005019008', col))
        grid[5, col].startValue = int(midStr('108427065', col))
        grid[6, col].startValue = int(midStr('020100580', col))
        grid[7, col].startValue = int(midStr('006090004', col))
        grid[8, col].startValue = int(midStr('019280370', col))

    for row in range(9):                    # preset final values to initial values (0 = not known)
        for col in range(9):
            grid[row, col].endValue = grid[row, col].startValue
            if grid[row, col].startValue != 0:
                grid[row, col].possibleValues = str(grid[row, col].startValue)
            else:
                grid[row, col].possibleValues = '123456789'


# ---------------------------------------------------------------
# Print grid - this should be a UI in which values are displayed
# ---------------------------------------------------------------

def printGrid():
    for row in range(9):
        printRow = ''
        for col in range(9):
            printRow = printRow + str(grid[row, col].endValue) + ' '
        print(printRow)


# ---------------------------------------------------------------
# SolveGrid - stage 1 - Print grid - this should be a UI in which values are displayed
#   Prepare gird with possible numbers reworking if any single numbers are found
# ---------------------------------------------------------------

def solveGridStage1(solved):

# For each cell in grid, establish whether there is already a single value.  If so, remove that number from all
# cells in row, col and square

    # Check that known values are removed from possible values
    for row in range(9):
        for col in range(9):
            if grid[row,col].endValue != 0:
                clearValueFromOtherCells(row, col, grid[row,col].endValue)

    # Go through all cells, where possible values are down to 1, set known value.  If no changes are found, stop.
    noChangesMade = True
    for row in range(9):
        for col in range(9):
            if grid[row,col].endValue == 0:
                if len(grid[row, col].possibleValues) == 1:
                    grid[row, col].endValue = int(grid[row, col].possibleValues)
                    noChangesMade = False

    return(noChangesMade)


# ---------------------------------------------------------------
# clearValuesFromOtherCells - if one cell in a row/column/square has a value, make sure that this is removed
# from all other squares.s
# ---------------------------------------------------------------

def clearValueFromOtherCells(aRow, aCol, aValue):

    # Check row
    for col in range (9):
        if col != aCol:       # Not the current column
            currentValues = grid[aRow, col].possibleValues
            if currentValues.find(str(aValue)) > -1:
                grid[aRow, col].possibleValues = currentValues.replace(str(aValue),"")


    # Check col
    for row in range(9):
        if row != aRow:      # Not the column being tested
            currentValues = grid[row, aCol].possibleValues
            if currentValues.find(str(aValue)) > -1:
                grid[row, aCol].possibleValues = currentValues.replace(str(aValue), "")


#    # Check square
    startCol = int(aCol/3) * 3
    startRow = int(aRow/3) * 3
    for row in range(startRow, startRow + 3):
        for col in range(startCol, startCol + 3):
            if row != aRow and col != aCol:  # Not the square being tested
                currentValues = grid[row, col].possibleValues
                if currentValues.find(str(aValue)) > -1:
                    grid[row, col].possibleValues = currentValues.replace(str(aValue), "")


# ---------------------------------------------------------------
# Main processing - initialise grid, run solver and display
#   results
# Initialise libraries, functions and classes
# ---------------------------------------------------------------

loadGrid()                                  # loads the Sudoku grid with initial values
print('Initial')
printGrid()

solved = False
while not solved:                          # iterates solving the grid (using simple method) until solved
    solved = solveGridStage1(solved)

# Other techniques can be added here...r

print(' ')
print('Final')
printGrid()                                 # prints the final answer

exit()
