# A queen is standing on an  chessboard. The chess board's rows are numbered from  to , going from bottom to top. Its columns are numbered from  to , going from left to right. Each square is referenced by a tuple, , describing the row, , and column, , where the square is located.
#
# The queen is standing at position . In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from :

# queensAttack has the following parameters:
# - n: an integer, the number of rows and columns in the board
# - k: an integer, the number of obstacles on the board
# - r_q: integer, the row number of the queen's position
# - c_q: integer, the column number of the queen's position
# - obstacles: a two dimensional array of integers where each element is an array of  integers, the row and column of an obstacle
#
# Sample Input 0
#
# 4 0
# 4 4
# Sample Output 0
#
# 9

def checkValid( x1 , y1, arr) :
    for (x, y) in arr :
        if x == x1 + 1 and y == y1 + 1 :
            return False
    return True

def checkSafe( x , y, N) :
    return True if (x < N and x >= 0 and y < N and y >= 0) else False

def findValidPaths(boardMatrix , numOfBrd , qRow , qCol , obsArr, numOfPossibleMoves, indicator) :
    if not (checkValid(qRow , qCol , obsArr) and checkSafe(qRow , qCol , numOfBrd) ) :
        return 0
    elif (qRow , qCol) in numOfPossibleMoves :
        return 0

    print(qRow , '--',qCol)
    num = 1
    numOfPossibleMoves.append((qRow , qCol))

    if indicator == 'L' :
        num += findValidPaths(boardMatrix , numOfBrd , qRow - 1 , qCol , obsArr,numOfPossibleMoves, 'L')
    elif indicator == 'R' :
        num += findValidPaths(boardMatrix , numOfBrd , qRow + 1 , qCol , obsArr,numOfPossibleMoves, 'R')
    elif indicator == 'U' :
        num += findValidPaths(boardMatrix , numOfBrd , qRow , qCol  - 1, obsArr,numOfPossibleMoves, 'U')
    elif indicator == 'D' :
        num += findValidPaths(boardMatrix , numOfBrd , qRow , qCol + 1 , obsArr,numOfPossibleMoves, 'D')
    elif indicator == 'LU' :
        num += findValidPaths(boardMatrix , numOfBrd , qRow - 1 , qCol - 1, obsArr,numOfPossibleMoves, 'LU')
    elif indicator == 'RU' :
        num += findValidPaths(boardMatrix , numOfBrd , qRow + 1 , qCol -1, obsArr,numOfPossibleMoves, 'RU')
    elif indicator == 'LD' :
        num += findValidPaths(boardMatrix , numOfBrd , qRow - 1 , qCol + 1, obsArr,numOfPossibleMoves, 'LD')
    elif indicator == 'RD' :
        num += findValidPaths(boardMatrix , numOfBrd , qRow + 1 , qCol + 1, obsArr,numOfPossibleMoves, 'RD')
    else :
        num = 0

    return num



def findValidPathScroller(boardMatrix , numOfBrd , qRow , qCol , i , j , obsArr, numOfPossibleMoves) :
    if not (checkValid(qRow , qCol , obsArr) and checkSafe(qRow , qCol , numOfBrd) ) :
        return 0
    elif (qRow , qCol) in numOfPossibleMoves :
        return 0

    num = 1
    numOfPossibleMoves.append((qRow, qCol))
    return num + findValidPathScroller(boardMatrix , numOfBrd , qRow + i , qCol + j , i , j , obsArr, numOfPossibleMoves)


def QueenAttack (numOfBrd , qRow , qCol , obsArr = []) :
    boardMatrix = [[0 for _ in range(numOfBrd)] for _ in range(numOfBrd)]
    qRow = qRow-1
    qCol = qCol -1

    boardMatrix[qRow][qCol] = 1
    numOfPossibleMoves = []
    # num = findValidPaths(boardMatrix , numOfBrd , qRow - 1, qCol - 1, obsArr, numOfPossibleMoves,)
    # return numOfPossibleMoves , num
    num = 0
    for (i , j) in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1), (1,-1),(-1,1)] :
        num += findValidPathScroller(boardMatrix , numOfBrd , qRow + i , qCol + j , i , j , obsArr, numOfPossibleMoves)
    print(numOfPossibleMoves)
    return num

print(QueenAttack (8 , 4 , 4 , [(3,5), (2,3)]))
