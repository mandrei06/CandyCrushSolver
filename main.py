import random
import numpy as np

# Initializing the number of lines and columns
# Any horizontal/vertical combination = 10 points
# Any combination in the shape of letter "L" = 20 points
# Any combination in the shape of letter "T" = 30 points
# Any cross-shaped combination = 50 points
columns = 11
lines = 11
score = 0
moves_nr = 0
antecedent = -1
# Random matrix generation - the number of elements can be changed in randint method, to be easier I choose 9
matrix = [[random.randint(1, 9) for j in range(columns)] for i in range(lines)]
# Matrix display
for line in range(0, columns * 5):
    print("-", end="")
print('\n', end="")
for i in range(0, columns):
    for j in range(0, lines):
        if j == lines - 1:
            print("|", matrix[i][j], "|")
        else:
            print("|", matrix[i][j], " ", end="")
    for l in range(0, columns * 5):
        print("-", end="")
    print('\n', end="")


# Matrix cleaning
def cleaningmatrix3horizontal(x, y):
    if x > 0:
        for j in range(x, 0, -1):
            for i in range(y, y + 3):
                matrix[j][i] = matrix[j - 1][i]
        for i in range(y, y + 3):
            matrix[0][i] = random.randint(1, 4)
    elif x == 0:
        for i in range(y, y + 3):
            matrix[0][i] = random.randint(1, 4)


def cleaningmatrix3vertical(x, y):
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)


def cleaningmatrixL(x, y):
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y + 1] = matrix[j - 1][y + 1]
    matrix[0][y + 1] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y + 2] = matrix[j - 1][y + 2]
    matrix[0][y + 2] = random.randint(1, 4)


def cleaningmatrixreverseL(x, y):
    for j in range(x, 0, -1):
        matrix[j][y + 2] = matrix[j - 1][y + 2]
    matrix[0][y + 2] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y + 2] = matrix[j - 1][y + 2]
    matrix[0][y + 2] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y + 2] = matrix[j - 1][y + 2]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y + 1] = matrix[j - 1][y + 1]
    matrix[0][y + 1] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)


def matrixdisplay():
    print('\n\n')
    for l in range(0, columns * 5):
        print("-", end="")
    print('\n', end="")
    for i in range(0, columns):
        for j in range(0, lines):
            if (j == lines - 1):
                print("|", matrix[i][j], "|")
            else:
                print("|", matrix[i][j], " ", end="")
        for l in range(0, columns * 5):
            print("-", end="")
        print('\n', end="")


def searching3horizontal():
    for x in range(lines - 1, -1, -1):
        for y in range(0, columns):
            if (y < columns - 2):
                if (matrix[x][y] == matrix[x][y + 1]):
                    if (matrix[x][y] == matrix[x][y + 2]):
                        cleaningmatrix3horizontal(x, y)
                        ok = 1
                        global score
                        score = score + 10
                        global modificare
                        modificare = 1
                        matrixdisplay()


def searching3vertical():
    for x in range(lines - 1, 0, -1):
        for y in range(0, columns):
            if (x >= 2):
                if (matrix[x][y] == matrix[x - 1][y]):
                    if (matrix[x][y] == matrix[x - 2][y]):
                        cleaningmatrix3vertical(x, y)
                        ok = 1
                        global score
                        score = score + 10
                        global modificare
                        modificare = 1
                        matrixdisplay()


def cleaningmatrixL180(x, y):
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x - 2, 0, -1):
        matrix[j][y - 1] = matrix[j - 1][y - 1]
    matrix[0][y - 1] = random.randint(1, 4)
    for j in range(x - 2, 0, -1):
        matrix[j][y - 2] = matrix[j - 1][y - 2]
    matrix[0][y - 2] = random.randint(1, 4)


def cleaningmatrixLupsidedown(x, y):
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x - 2, 0, -1):
        matrix[j][y + 1] = matrix[j - 1][y + 1]
    matrix[0][y + 1] = random.randint(1, 4)
    for j in range(x - 2, 0, -1):
        matrix[j][y + 2] = matrix[j - 1][y + 2]
    matrix[0][y + 2] = random.randint(1, 4)


def cleaningmatrixT(x, y):
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x - 2, 0, -1):
        matrix[j][y - 1] = matrix[j - 1][y - 1]
    matrix[0][y - 1] = random.randint(1, 4)
    for j in range(x - 2, 0, -1):
        matrix[j][y + 1] = matrix[j - 1][y + 1]
    matrix[0][y + 1] = random.randint(1, 4)


def cleaningmatrixX(x, y):
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x - 1, 0, -1):
        matrix[j][y - 1] = matrix[j - 1][y - 1]
    matrix[0][y - 1] = random.randint(1, 4)
    for j in range(x - 1, 0, -1):
        matrix[j][y + 1] = matrix[j - 1][y + 1]


def cleaningmatrixreversedT(x, y):
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y - 1] = matrix[j - 1][y - 1]
    matrix[0][y - 1] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y + 1] = matrix[j - 1][y + 1]
    matrix[0][y + 1] = random.randint(1, 4)


def cleaningmatrixT90(x, y):
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x - 1, 0, -1):
        matrix[j][y + 1] = matrix[j - 1][y + 1]
    matrix[0][y + 1] = random.randint(1, 4)
    for j in range(x - 1, 0, -1):
        matrix[j][y + 2] = matrix[j - 1][y + 2]
    matrix[0][y + 2] = random.randint(1, 4)


def cleaningmatrixT270(x, y):
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x, 0, -1):
        matrix[j][y] = matrix[j - 1][y]
    matrix[0][y] = random.randint(1, 4)
    for j in range(x - 1, 0, -1):
        matrix[j][y - 1] = matrix[j - 1][y - 1]
    matrix[0][y - 1] = random.randint(1, 4)
    for j in range(x - 1, 0, -1):
        matrix[j][y - 2] = matrix[j - 1][y - 2]
    matrix[0][y - 2] = random.randint(1, 4)


def searchingLform():
    for x in range(lines - 1, 0, -1):
        for y in range(0, columns - 2):
            if (x > 2):
                if (matrix[x][y] == matrix[x - 1][y]):
                    if (matrix[x][y] == matrix[x - 2][y]):
                        if (matrix[x][y] == matrix[x][y + 1]):
                            if (matrix[x][y] == matrix[x][y + 2]):
                                cleaningmatrixL(x, y)
                                ok = 1
                                global score
                                score = score + 20
                                global modificare
                                modificare = 1
                                matrixdisplay()


def searchingreversedL():
    for x in range(lines - 1, 0, -1):
        for y in range(0, columns - 2):
            if (x > 2):
                if (matrix[x][y + 2] == matrix[x - 1][y + 2]):
                    if (matrix[x][y + 2] == matrix[x - 2][y + 2]):
                        if (matrix[x][y] == matrix[x][y + 1]):
                            if (matrix[x][y] == matrix[x][y + 2]):
                                cleaningmatrixreverseL(x, y)
                                ok = 1
                                global score
                                score = score + 20
                                global modificare
                                modificare = 1
                                matrixdisplay()


def searchingL180():
    for x in range(lines - 1, 0, -1):
        for y in range(2, columns):
            if (x > 1):
                if (matrix[x][y] == matrix[x - 1][y]):
                    if (matrix[x][y] == matrix[x - 2][y]):
                        if (matrix[x][y] == matrix[x - 2][y - 1]):
                            if (matrix[x][y] == matrix[x - 2][y - 2]):
                                cleaningmatrixL180(x, y)
                                ok = 1
                                global score
                                score = score + 20
                                global modificare
                                modificare = 1
                                matrixdisplay()


def searchingLupsidedown():
    for x in range(lines - 1, 0, -1):
        for y in range(0, columns - 2):
            if (x > 1):
                if (matrix[x][y] == matrix[x - 1][y]):
                    if (matrix[x][y] == matrix[x - 2][y]):
                        if (matrix[x][y] == matrix[x - 2][y + 1]):
                            if (matrix[x][y] == matrix[x - 2][y + 2]):
                                cleaningmatrixLupsidedown(x, y)
                                ok = 1
                                global score
                                score = score + 20
                                global modificare
                                modificare = 1
                                matrixdisplay()


def searchingT():
    for x in range(lines - 1, 1, -1):
        for y in range(1, columns - 1):
            if (x >= 2):
                if (matrix[x][y] == matrix[x - 1][y]):
                    if (matrix[x][y] == matrix[x - 2][y]):
                        if (matrix[x][y] == matrix[x - 2][y - 1]):
                            if (matrix[x][y] == matrix[x - 2][y + 1]):
                                cleaningmatrixT(x, y)
                                ok = 1
                                global score
                                score = score + 30
                                global modificare
                                modificare = 1
                                matrixdisplay()


def searchingX():
    for x in range(lines - 2, 1, -1):
        for y in range(1, columns - 1):
            if (x > 0):
                if (matrix[x][y] == matrix[x - 1][y]):
                    if (matrix[x][y] == matrix[x - 1][y - 1]):
                        if (matrix[x][y] == matrix[x - 1][y + 1]):
                            if (matrix[x][y] == matrix[x - 2][y]):
                                cleaningmatrixX(x, y)
                                ok = 1
                                global score
                                score = score + 50
                                global modificare
                                modificare = 1
                                matrixdisplay()


def searchingreversedT():
    for x in range(lines - 1, 0, -1):
        for y in range(1, columns - 1):
            if (x >= 2):
                if (matrix[x][y] == matrix[x - 1][y]):
                    if (matrix[x][y] == matrix[x - 2][y]):
                        if (matrix[x][y] == matrix[x][y - 1]):
                            if (matrix[x][y] == matrix[x][y + 1]):
                                cleaningmatrixreversedT(x, y)
                                ok = 1
                                global score
                                score = score + 30
                                global modificare
                                modificare = 1
                                matrixdisplay()


def searchingT90():
    for x in range(lines - 1, 0, -1):
        for y in range(0, columns - 2):
            if (x > 1):
                if (matrix[x][y] == matrix[x - 1][y]):
                    if (matrix[x][y] == matrix[x - 2][y]):
                        if (matrix[x][y] == matrix[x - 1][y + 1]):
                            if (matrix[x][y] == matrix[x - 1][y + 2]):
                                cleaningmatrixT90(x, y)
                                ok = 1
                                global score
                                score = score + 30
                                global modificare
                                modificare = 1
                                matrixdisplay()


def searchingT270():
    for x in range(lines - 1, 0, -1):
        for y in range(2, columns):
            if (x > 1):
                if (matrix[x][y] == matrix[x - 1][y]):
                    if (matrix[x][y] == matrix[x - 2][y]):
                        if (matrix[x][y] == matrix[x - 1][y - 1]):
                            if (matrix[x][y] == matrix[x - 1][y - 2]):
                                cleaningmatrixT270(x, y)
                                ok = 1
                                global score
                                score = score + 30
                                global modificare
                                modificare = 1
                                matrixdisplay()


def movement():
    global matrix, noMoves, ok1
    noMoves = 0
    for i in range(lines - 1, -1, -1):
        for j in range(0, columns):
            global ok2
            ok2 = 0
            if (j < columns - 1 and matrix[i][j] == matrix[i][j + 1]):
                if (i < lines - 1 and j < columns - 2 and matrix[i][j] == matrix[i + 1][j + 2]):
                    if (ok2 == 0):
                        aux = matrix[i][j + 2]
                        matrix[i][j + 2] = matrix[i + 1][j + 2]
                        matrix[i + 1][j + 2] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0
            elif (j < columns - 1 and matrix[i][j] == matrix[i][j + 1]):
                if (j < columns - 2 and matrix[i][j] == matrix[i - 1][j + 2]):
                    if (ok2 == 0):
                        aux = matrix[i][j + 2]
                        matrix[i][j + 2] = matrix[i - 1][j + 2]
                        matrix[i - 1][j + 2] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0
            elif (i >= 1 and j < columns - 1 and matrix[i - 1][j] == matrix[i][j + 1]):
                if (j < columns - 2 and matrix[i - 1][j] == matrix[i][j + 2]):
                    if (ok2 == 0):
                        aux = matrix[i][j]
                        matrix[i][j] = matrix[i - 1][j]
                        matrix[i - 1][j] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0
            elif (i < lines - 1 and j < columns - 1 and matrix[i + 1][j] == matrix[i][j + 1]):
                if (j < columns - 2 and matrix[i + 1][j] == matrix[i][j + 2]):
                    if (ok2 == 0):
                        aux = matrix[i][j]
                        matrix[i][j] = matrix[i + 1][j]
                        matrix[i + 1][j] = aux
                        noMoves = noMoves + 1
                        ok2 = ok + 1
                        ok1 = 0
            elif (j < columns - 1 and i < lines - 1 and matrix[i][j + 1] == matrix[i + 1][j]):
                if (j < columns - 2 and matrix[i][j + 1] == matrix[i + 2][j]):
                    if (ok2 == 0):
                        aux = matrix[i][j]
                        matrix[i][j] = matrix[i][j + 1]
                        matrix[i][j + 1] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0
            elif (j >= 1 and i < lines - 1 and matrix[i][j - 1] == matrix[i + 1][j]):
                if (i < lines - 2 and matrix[i][j - 1] == matrix[i + 2][j]):
                    if (ok2 == 0):
                        aux = matrix[i][j]
                        matrix[i][j] = matrix[i][j - 1]
                        matrix[i][j - 1] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0
            elif (i < lines - 1 and matrix[i][j] == matrix[i + 1][j]):
                if (i < lines - 2 and j < columns - 1 and matrix[i][j] == matrix[i + 2][j + 1]):
                    if (ok2 == 0):
                        aux = matrix[i + 2][j]
                        matrix[i + 2][j] = matrix[i + 2][j + 1]
                        matrix[i + 2][j + 1] = aux
                        noMoves = noMoves + 1
                        ok2 = 1
                        ok1 = 0
            elif (i < lines - 1 and matrix[i][j] == matrix[i + 1][j]):
                if (i < lines - 2 and j > 1 and matrix[i][j] == matrix[i + 2][j - 1]):
                    if (ok2 == 0):
                        aux = matrix[i + 2][j]
                        matrix[i + 2][j] = matrix[i + 2][j - 1]
                        matrix[i + 2][j - 1] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0
            elif (i >= 1 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1]):
                if (i < lines - 1 and matrix[i][j] == matrix[i + 1][j - 1]):
                    if (ok2 == 0):
                        aux = matrix[i][j]
                        matrix[i][j] = matrix[i][j - 1]
                        matrix[i][j - 1] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0
            elif (i >= 1 and j < columns - 1 and matrix[i][j] == matrix[i - 1][j + 1]):
                if (i < lines - 1 and matrix[i][j] == matrix[i + 1][j + 1]):
                    if (ok2 == 0):
                        aux = matrix[i][j]
                        matrix[i][j] = matrix[i][j + 1]
                        matrix[i][j + 1] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0
            elif (j < columns - 2 and matrix[i][j] == matrix[i][j + 2]):
                if (i < lines - 1 and matrix[i][j] == matrix[i + 1][j + 1]):
                    if (ok2 == 0):
                        aux = matrix[i + 1][j + 1]
                        matrix[i + 1][j + 1] = matrix[i][j + 1]
                        matrix[i][j + 1] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0
            elif (j < columns - 2 and matrix[i][j] == matrix[i][j + 2]):
                if (i >= 1 and matrix[i][j] == matrix[i - 1][j + 1]):
                    if (ok2 == 0):
                        aux = matrix[i - 1][j + 1]
                        matrix[i - 1][j + 1] = matrix[i][j + 1]
                        matrix[i][j + 1] = aux
                        noMoves = noMoves + 1
                        ok2 = ok2 + 1
                        ok1 = 0


modificare = 1
while (modificare != 0):
    modificare = 0
    ok = 1
    while (ok == 1):
        ok = 0
        searchingX()
    ok = 1
    while (ok == 1):
        ok = 0
        searchingT90()
    ok = 1
    while (ok == 1):
        ok = 0
        searchingT270()
    ok = 1
    while (ok == 1):
        ok = 0
        searchingreversedT()
    ok = 1
    while (ok == 1):
        ok = 0
        searchingT()
    ok = 1
    while (ok == 1):
        ok = 0
        searchingLupsidedown()
    ok = 1
    while (ok == 1):
        ok = 0
        searchingL180()
    ok = 1
    while (ok == 1):
        ok = 0
        searchingreversedL()
    ok = 1
    while (ok == 1):
        ok = 0
        searchingLform()
    ok = 1
    while (ok == 1):
        ok = 0
        searching3horizontal()
    ok = 1
    while (ok == 1):
        ok = 0
        searching3vertical()
score = 0
while (antecedent != moves_nr):
    modificare = 1
    while (modificare != 0):
        modificare = 0
        ok = 1
        while (ok == 1):
            ok = 0
            searchingX()
        ok = 1
        while (ok == 1):
            ok = 0
            searchingT90()
        ok = 1
        while (ok == 1):
            ok = 0
            searchingT270()
        ok = 1
        while (ok == 1):
            ok = 0
            searchingreversedT()
        ok = 1
        while (ok == 1):
            ok = 0
            searchingT()
        ok = 1
        while (ok == 1):
            ok = 0
            searchingLupsidedown()
        ok = 1
        while (ok == 1):
            ok = 0
            searchingL180()
        ok = 1
        while (ok == 1):
            ok = 0
            searchingreversedL()
        ok = 1
        while (ok == 1):
            ok = 0
            searchingLform()
        ok = 1
        while (ok == 1):
            ok = 0
            searching3horizontal()
        ok = 1
        while (ok == 1):
            ok = 0
            searching3vertical()
    print("The score after the move: ", moves_nr, " is: ", score)
    movement()
    print('\nAfter ', moves_nr, " moves, the matrix look like this:")
    matrixdisplay()
    global noMoves
    antecedent = moves_nr
    if (noMoves):
        moves_nr = moves_nr + 1
print("\n\n")
