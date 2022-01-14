pegStartingPosition = [0,0]
pegMove =[0,0]
forPegNextToSelected = [0,0]
gameMatrix = [
    ['X','X',1,1,1,'X','X'],
    ['X','X',1,1,1,'X','X'],
        [1,1,1,1,1,1,1],
        [1,1,1,0,1,1,1],
        [1,1,1,1,1,1,1],
    ['X','X',1,1,1,'X','X'],
    ['X','X',1,1,1,'X','X'],
]


# Function - Draw Game Board #
def drawGameBoard():
    gameBoard = f"""
    1 2 3 4 5 6 7

A       {gameMatrix[0][2]} {gameMatrix[0][3]} {gameMatrix[0][4]} 
B       {gameMatrix[1][2]} {gameMatrix[1][3]} {gameMatrix[1][4]}
C   {gameMatrix[2][0]} {gameMatrix[2][1]} {gameMatrix[2][2]} {gameMatrix[2][3]} {gameMatrix[2][4]} {gameMatrix[2][5]} {gameMatrix[2][6]}
D   {gameMatrix[3][0]} {gameMatrix[3][1]} {gameMatrix[3][2]} {gameMatrix[3][3]} {gameMatrix[3][4]} {gameMatrix[3][5]} {gameMatrix[3][6]}
E   {gameMatrix[4][0]} {gameMatrix[4][1]} {gameMatrix[4][2]} {gameMatrix[4][3]} {gameMatrix[4][4]} {gameMatrix[4][5]} {gameMatrix[4][6]}
F       {gameMatrix[5][2]} {gameMatrix[5][3]} {gameMatrix[5][4]}
G       {gameMatrix[6][2]} {gameMatrix[6][3]} {gameMatrix[6][4]}
"""
    print(gameBoard)


# Function - Move Up on Board #
def moveUpOnBoard(pegMove,forPegNextToSelected):
    pegMove[0] = -2
    pegMove[1] = 0
    forPegNextToSelected[0] = pegMove[0] + 1
    forPegNextToSelected[1] = pegMove[1]


# Function - Move Down on Board
def moveDownOnBoard(pegMove,forPegNextToSelected):
    pegMove[0] = 2
    pegMove[1] = 0
    forPegNextToSelected[0] = pegMove[0] - 1
    forPegNextToSelected[1] = pegMove[1] 


# Function - Move Right on Board #
def moveRightOnBoard(pegMove,forPegNextToSelected):
    pegMove[0] = 0
    pegMove[1] = 2
    forPegNextToSelected[0] = pegMove[0]
    forPegNextToSelected[1] = pegMove[1] - 1


# Function - Move Left on Board #
def moveLeftOnBoard(pegMove,forPegNextToSelected):
    pegMove[0] = 0
    pegMove[1] = -2
    forPegNextToSelected[0] = pegMove[0]
    forPegNextToSelected[1] = pegMove[1] + 1


# Function - Check if the Move is Valid or Not #
def isTheMoveValid(pegStartingPosition,pegMove,forPegNextToSelected):
    if gameMatrix[pegStartingPosition[0]][pegStartingPosition[1]] == 'X':
        print("Given peg position is out of board!")
        return "Invalid Move"
    elif gameMatrix[pegStartingPosition[0]][pegStartingPosition[1]] == 0:
        print("Given position does not have a peg!")
        return "Invalid Move"
    elif (pegStartingPosition[0] + pegMove[0]) < 0:
        print("Moving peg will fall out of bounds!")
        return "Invalid Move"
    elif (pegStartingPosition[1] + pegMove[1]) < 0:
        print("Moving peg will fall out of bounds!")
        return "Invalid Move"
    elif (pegStartingPosition[0] + pegMove[0]) > 6:
        print("Moving peg will fall out of bounds!")
        return "Invalid Move"
    elif (pegStartingPosition[1] + pegMove[1]) > 6:
        print("Moving peg will fall out of bounds!")
        return "Invalid Move"
    elif gameMatrix[pegMove[0] + pegStartingPosition[0]][pegMove[1] + pegStartingPosition[1]] == 'X':
        print("Moving peg will fall out of bounds!")
        return "Invalid Move"
    elif gameMatrix[pegMove[0] + pegStartingPosition[0]][pegMove[1] + pegStartingPosition[1]] == 1:
        print("Landing position is occupied")
        return "Invalid Move"
    elif gameMatrix[pegStartingPosition[0] + forPegNextToSelected[0]][pegStartingPosition[1] + forPegNextToSelected[1]] == 0:
        print("No peg at next position to jump over!")
        return "Invalid Move"
    else:
        return "Valid Move"


# Function - If the Move is Valid, Update Game Matrix #
def ifMoveValid(pegStartingPosition,pegMove,forPegNextToSelected):
    gameMatrix[pegStartingPosition[0]][pegStartingPosition[1]] = 0
    gameMatrix[pegStartingPosition[0] + forPegNextToSelected[0]][pegStartingPosition[1] + forPegNextToSelected[1]] = 0
    gameMatrix[pegStartingPosition[0] + pegMove[0]][pegStartingPosition[1] + pegMove[1]] = 1


# Function - Check if Game is Over #
def isGameOver():
    pegsThatCanMove = 0
    for i in range(len(gameMatrix)):
        for j in range(len(gameMatrix)):
            if gameMatrix[i][j] == 0:
                if (i == 0 and j == 2) or (i == 1 and j == 2): # For A3,B3
                    if (gameMatrix[i][j+1] == 1 and gameMatrix[i][j+2] == 1) or (gameMatrix[i+1][j] == 1 and gameMatrix[i+2][j] == 1):
                        pegsThatCanMove +=1
                elif (i == 0 and j == 3) or (i == 1 and j == 3):# For A4,B4
                    if gameMatrix[i+1][j] == 1 and gameMatrix[i+2][j] == 1:
                        pegsThatCanMove += 1
                elif (i == 0 and j == 4) or (i == 1 and j == 4):# For A5,B5
                    if (gameMatrix[i][j-1] == 1 and gameMatrix[i][j-2] == 1) or (gameMatrix[i+1][j] == 1 and gameMatrix[i+2][j] == 1):
                        pegsThatCanMove += 1
                elif (i == 2 and j == 0) or (i == 2 and j == 1): # For C1,C2
                    if (gameMatrix[i][j+1] == 1 and gameMatrix[i][j+2] == 1) or (gameMatrix[i+1][j] == 1 and gameMatrix[i+2][j] == 1):
                        pegsThatCanMove += 1
                elif (i == 3 and j == 0) or (i == 3 and j == 1):# For D1,D2
                    if gameMatrix[i][j+1] == 1 and gameMatrix[i][j+2] == 1:
                        pegsThatCanMove += 1
                elif (i == 4 and j == 0) or (i == 4 and j == 1):# For E1,E2
                    if (gameMatrix[i][j+1] == 1 and gameMatrix[i][j+2] == 1) or (gameMatrix[i-1][j] == 1 and gameMatrix[i-2][j] == 1):
                        pegsThatCanMove += 1
                elif (i == 6 and j == 2) or (i == 5 and j == 2):# For F3,G3
                    if (gameMatrix[i-1][j] == 1 and gameMatrix[i-2][j] == 1) or (gameMatrix[i][j+1] == 1 and gameMatrix[i][j+2] == 1):
                        pegsThatCanMove += 1
                elif (i == 6 and j == 3) or (i == 5 and j == 3):# For F4,G4
                    if gameMatrix[i-1][j] == 1 and gameMatrix[i-2][j] == 1:
                        pegsThatCanMove += 1
                elif (i == 6 and j == 4) or (i == 5 and j == 4):# For F5,G5
                    if (gameMatrix[i][j-1] == 1 and gameMatrix[i][j-2] == 1) or (gameMatrix[i-1][j] == 1 and gameMatrix[i-2][j] == 1):
                        pegsThatCanMove += 1
                elif (i == 4 and j == 6) or (i == 4 and j == 5):# For E7,E6
                    if (gameMatrix[i][j-1] == 1 and gameMatrix[i][j-2] == 1) or (gameMatrix[i-1][j] == 1 and gameMatrix[i-2][j] == 1):
                        pegsThatCanMove += 1
                elif (i == 3 and j == 6) or (i == 3 and j == 5):# For D7,D6
                    if gameMatrix[i][j-1] == 1 and gameMatrix[i][j-2] == 1:
                        pegsThatCanMove += 1
                elif (i == 2 and j == 6) or (i == 2 and j == 5):# For C7,C6
                    if (gameMatrix[i+1][j] == 1 and gameMatrix[i+2][j] == 1) or (gameMatrix[i][j-1] == 1 and gameMatrix[i][j-2] == 1):
                        pegsThatCanMove += 1
                elif i-1>=0 and i-2>=0 and i+1<=6 and i+2<=6 and j-1>=0 and j-2>=0 and j+1<=6 and j+2<=6:# For the Rest
                    if (gameMatrix[i][j+1] == 1 and gameMatrix[i][j+2] == 1) or (gameMatrix[i][j-1] == 1 and gameMatrix[i][j-2] == 1) or (gameMatrix[i-1][j] == 1 and gameMatrix[i-2][j] == 1) or (gameMatrix[i+1][j] == 1 and gameMatrix[i+2][j] == 1):
                        pegsThatCanMove += 1
    if pegsThatCanMove == 0:
        return True
    else:
        return False


# Function - Gameplay #
def gamePlay():
    availableMoves = True
    while availableMoves:
        if isGameOver() == False:
            drawGameBoard()
            pegStartingPosition = [0,0]
            pegMove = [0,0]
            forPegNextToSelected = [0,0]
            matrixRows = ['A','B','C','D','E','F','G']
            userInput = input("Enter peg position followed by move (L, R, U, or D): ")
            if len(userInput) != 3:
                print("Something wrong with your input!")
            elif userInput[0].upper() not in matrixRows:
                print("Select valid row (A,B,C,D,E,F,G)")
            elif int(userInput[1]) > 7 or int(userInput[1]) < 1:
                print("Select valid column (1,2,3,4,5,6,7)")
            else:
                inputTuple = tuple(userInput)
                pegStartingPosition[0] = matrixRows.index(inputTuple[0].upper())
                pegStartingPosition[1] = int(inputTuple[1]) - 1 
                if inputTuple[2].upper() != 'U' and inputTuple[2].upper() != 'D' and inputTuple[2].upper() != 'R' and inputTuple[2].upper() != 'L':
                    print("Direction is not L or R or U or D!")   
                else:       
                    if inputTuple[2].upper() == 'U':
                        moveUpOnBoard(pegMove,forPegNextToSelected)
                    elif inputTuple[2].upper() == 'D':
                        moveDownOnBoard(pegMove,forPegNextToSelected)
                    elif inputTuple[2].upper() == 'R':
                        moveRightOnBoard(pegMove,forPegNextToSelected)
                    elif inputTuple[2].upper() == 'L':
                        moveLeftOnBoard(pegMove,forPegNextToSelected)
                    if isTheMoveValid(pegStartingPosition,pegMove,forPegNextToSelected) == "Valid Move":
                        ifMoveValid(pegStartingPosition,pegMove,forPegNextToSelected)
        else:
            drawGameBoard()
            pegsLeftOnBoard = 0
            for row in gameMatrix:
                pegsLeftOnBoard += row.count(1)
            if pegsLeftOnBoard == 1:
                print(f"You win! Congratulations! {pegsLeftOnBoard} peg left!")
            else:
                print(f"No more moves. The number of remaining pegs is {pegsLeftOnBoard}")
            availableMoves = False


gamePlay()
