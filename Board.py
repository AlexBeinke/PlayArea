
WIDTH = 2
HEIGHT = WIDTH
SPACE = [-1,0,1]

class Board:

    def __init__(self):
        self.contents = []
        width_counter = 0
        while width_counter < WIDTH:
            height_counter = 0
            column = []
            while height_counter < HEIGHT:
                column.append(height_counter % len(SPACE))
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
    rowCounters = []
    for i in range(HEIGHT):
        rowCounters.append(0)
    columnCounters = []
    for i in range(WIDTH):
        columnCounters.append(0)
    bestRow = rowCounters.copy()
    bestColumn = columnCounters.copy()
    print(rowCounters)
    print(columnCounters)




    print(bestRow)
    print(bestColumn)

