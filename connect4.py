#ASSIGNMENT 3
#Name: Priyal Gulati
#Student ID: 101185010

def makeGrid(nRows,nCols):
    '''takes 2 integers(number of rows and columns) as input and returns a 
        2-dimensional list that is an empty game consisting of nRows and
        nCols. All nCol strings are the string 'empty'
    '''
    grid = []
    for i in range(nRows):
        col = []
        col.append('empty')
        grid.append(col*nCols)
        
    return grid

def play(grid, column, checker):
    '''plays the checker (either ‘red’ or ‘black’) in the specified column of
       the grid. If column is valid and there is room to play another checker
       in that column of the grid, modifies the grid to add the checker in the
       given column and returns True. Otherwise, it returns False.
    '''
    nRows = len(grid)
    nCols = len(grid[0])
    if column< nCols and column >= 0:
        for i in range(nRows-1,-1,-1):
            if grid[i][column] == 'empty':
                grid[i].pop(column)
                grid[i].insert(column,checker)
                return True
            
        return False
    else:
        return False

def win(grid, column):
    '''checks if the player has won the game(four checkers in the same row, column
       or diagonally) or not. Returns a string, "black" or "red" if the player won,
       otherwise "empty". Also returns "empty" if player entered invalid column.
    '''
    nRows = len(grid)
    nCols = len(grid[0])
    #checking for valid 4x4 grid
    if nRows<4 or nCols<4:
        return 'empty'
    #finding exact location of checker
    row = 0
    while row<nRows:
        if grid[row][column]=='empty':
            row+=1
        else:
            break
      
    currentPos = grid[row][column]
    count = 1
    tempRow = row
    #checking vertical win
    while tempRow < nRows - 1:
        if grid[tempRow+1][column] == currentPos:
            count += 1
        tempRow += 1
        if count==4:
            return f'{currentPos}'

    #checking horizontal win
    tempCol = 0
    count = 0
    color = currentPos
    while tempCol < nCols:
        if color != grid[row][tempCol]:
            count = 0
        else:
            count += 1
        tempCol+=1
        if count == 4:
            return f'{currentPos}'
    
    #upper left - bottom right
    tempCol = column
    tempRow = row
    count = 1
    while tempRow > 0 and tempCol > 0:
        if(currentPos == grid[tempRow-1][tempCol-1]):
            count += 1
            tempCol -= 1
            tempRow -= 1
            if(count == 4):
                return currentPos
        else:
            break

    tempCol = column
    tempRow = row
    
    while tempCol<(nCols-1) and tempRow<(nRows-1):
        if(currentPos == grid[tempRow+1][tempCol+1]):
            count+=1
            tempCol+=1
            tempRow+=1
            if(count == 4):
                return currentPos
        else:
            break   

    #bottom left upper right
    tempCol=column
    tempRow=row
    count=1
    while tempCol>0 and tempRow<(nRows-1):
        if grid[tempRow+1][tempCol-1]==currentPos:
            count+=1
            tempCol-=1
            tempRow+=1
            if count==4:
                return f'{currentPos}'
           
        else:
            break
    
    tempCol=column
    tempRow=row
    while tempCol<(nCols-1) and tempRow>0:
        if grid[tempRow-1][tempCol+1]==currentPos:
            count+=1
            tempCol+=1
            tempRow-=1
            if count==4:
                return f'{currentPos}'
           
        else:
            break 

    return 'empty'



def toString(grid):
   '''returns string representation of the game'''
   nRows = len(grid)
   nCols = len(grid[0])
   game = ''
   for row in range(nRows):  
       game += '|'
       for col in range(nCols):
           value = grid[row][col]
           if value.lower()=='red':
               value = "X"
           elif value.lower()=='black':
               value = "O"
           else:
               value = " "
           game+= f'{value}'
       game+= f'|{str(row)}'
       game += '\n'
   game+= "+" + nCols*'-' + '+' + '\n '
   for col in range(nCols):
       game+=  str(col)
   return game
  
