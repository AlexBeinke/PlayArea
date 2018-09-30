import random

WIDTH = 6
HEIGHT = WIDTH
SPACE = [-1, 0, 1]

class Board:

    def __init__(self):
        self.contents = []
        width_counter = 0
        while width_counter < WIDTH:
            height_counter = 0
            column = []
            while height_counter < HEIGHT:
                column.append(random.randint(0, len(SPACE) - 1))
                height_counter += 1

            self.contents.append(column)
            width_counter += 1

    def __str__(self):
        res = ""
        for row in self.contents:
            for value in row:
                res = res + str(SPACE[value]) + ", "
            res = res + "\n"
        return res

    def addToRow(self, key):
        myRow = self.contents[key]
        iterator = 0
        while iterator < WIDTH:
            myRow[iterator] = (myRow[iterator] + 1) % len(SPACE)
            iterator += 1

    def addToColumn(self, key):
        for row in self.contents:
            row[key] = (row[key] + 1) % len(SPACE)

    def score(self):
        total = 0
        for row in self.contents:
            for value in row:
                total += SPACE[value]
        return total


if __name__ =="__main__":
    myBoard = Board()
    stateBoard = Board()
    stateBoard.contents = []
    print(str(myBoard))
    for row in myBoard.contents:
        stateBoard.contents.append(row.copy())

    rowCounters = []
    for i in range(HEIGHT):
        rowCounters.append(0)
    columnCounters = []
    for i in range(WIDTH):
        columnCounters.append(0)
    bestScore = myBoard.score()
    bestRow = rowCounters.copy()
    bestColumn = columnCounters.copy()

    startRow = rowCounters.copy()
    startColumn = columnCounters.copy()

    rowCounters[0] = 1
    myBoard.addToRow(0)


    while startRow != rowCounters or startColumn != columnCounters:
        # we haven't tried everything yet
        thisBoardScore = myBoard.score()
        if thisBoardScore > bestScore:
            bestRow = rowCounters.copy()
            bestColumn = columnCounters.copy()
            bestScore = thisBoardScore
        carry = False
        if rowCounters[0] == len(SPACE) - 1:
            carry = True
        myBoard.addToRow(0)
        rowCounters[0] = (rowCounters[0] + 1) % len(SPACE)
        for i in range(1, HEIGHT):
            if carry:
                if rowCounters[i] != len(SPACE) - 1:
                    carry = False
                myBoard.addToRow(i)
                rowCounters[i] = (rowCounters[i] + 1) % len(SPACE)
        for i in range(WIDTH):
            if carry:
                if columnCounters[i] != len(SPACE) - 1:
                    carry = False
                myBoard.addToColumn(i)
                columnCounters[i] = (columnCounters[i] + 1) % len(SPACE)

    print(bestRow)
    print(bestColumn)

    for i in range(len(bestRow)):
        for j in range(bestRow[i]):
            stateBoard.addToRow(i)
            print("rolling row " + str(i))
    for i in range(len(bestColumn)):
        for j in range(bestColumn[i]):
            stateBoard.addToColumn(i)
            print("rolling column " + str(i))
    print('best solution:')
    print(str(stateBoard))
    print('best score: ' + str(stateBoard.score()))
