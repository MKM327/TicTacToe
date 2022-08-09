import random

arr = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
enemyNumber = 'O'
userNumber = 'X'
GameRunning = True
GameState = 'running'


def GameTable(gameTable):
    print('\n'.join(' '.join(str(x) for x in row) for row in gameTable))


def RemainingSpots(gameTable):
    spots = 0
    for i in range(3):
        for j in range(3):
            if gameTable[i][j] == ' ':
                spots += 1
    return spots


def CheckWin(arr, number):
    for i in range(3):
        rowUserCount = 0
        for j in range(3):
            gameValue = arr[i][j]
            if gameValue == number:
                rowUserCount += 1
        if rowUserCount == 3:
            return f'{number}/win'
    for i in range(3):
        columnUserCount = 0
        for j in range(3):
            gameValue = arr[j][i]
            if gameValue == number:
                columnUserCount += 1
        if columnUserCount == 3:
            return f'{number}/win'
    diagCount = 0
    for i in range(3):
        if arr[i][i] == number:
            diagCount += 1
        if diagCount == 3:
            return f'{number}/win'
    gameRow = 2
    gameColumn = 0
    revdiagCount = 0
    while gameColumn != 3:
        if arr[gameRow][gameColumn] == number:
            revdiagCount += 1
        gameRow -= 1
        gameColumn += 1
    if revdiagCount == 3:
        return f'{number}/win'


def computerMove(gameTable):
    compRow = random.randint(0, 2)
    compColumn = random.randint(0, 2)
    if gameTable[compRow][compColumn] == enemyNumber or gameTable[compRow][compColumn] == userNumber:
        computerMove(gameTable)
    else:
        gameTable[compRow][compColumn] = enemyNumber


while GameState == 'running':
    GameTable(arr)
    remainingSpots = RemainingSpots(arr)
    if remainingSpots == 0:
        GameState = 'draw'
        break

    row = int(input("which row"))
    column = int(input("which column "))
    if not 0 <= row < 3 or not 0 <= column < 3:
        print("Enter a legit value")
        continue
    if arr[row][column] == enemyNumber or arr[row][column] == userNumber:
        print("that place is occupied!")
        continue

    arr[row][column] = userNumber
    playerWinState = CheckWin(arr, userNumber)

    if playerWinState is not None :
        winner = playerWinState.split("/")[0]
        GameState = f"{winner} Wins"

    if remainingSpots != 1:
        computerMove(arr)
    enemyWinState = CheckWin(arr, enemyNumber)
    if enemyWinState is not None:
        winner = enemyWinState.split("/")[0]
        GameState = f"{winner} Wins"
if GameState == 'draw':
    print("Game ended in a draw")
if GameState == "X Wins":
    print("Player Won")
if GameState == "O Wins":
    print("Computer Won")
