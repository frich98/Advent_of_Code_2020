# ------ Advent of Code - 2020
# ------ Day 11: Seating System
# ------ Frannie Richert
# ------ December 18, 2020


from copy import deepcopy


class AOC_DAY11():

    def __init__(self, filename):
        self.filename = filename
        self.rows = 0
        self.cols = 0
        self.mtx = []
        self.mtxList = []

    def readFile(self):
        # open/close file, read all lines into variable list
        f = open(self.filename, "r")
        fLines = f.readlines()
        f.close()
        # set matrix details
        self.rows = len(fLines)
        self.cols = len(fLines[0].strip())
        #print("Rows: %i, Cols: %i" % (self.rows, self.cols))
        # loop through lines putting values into list of lists
        for i in range(self.rows):
            self.mtx.append([])
            currLine = fLines[i].strip()
            for j in range(self.cols):
                self.mtx[i].append(currLine[j])

    def getTopLeft_Part1(self, currMtx, i, j):
        if i >= 1 and j >= 1:
            return currMtx[i-1][j-1]
        else:
            return -1

    def getTopMiddle_Part1(self, currMtx, i, j):
        if i >= 1:
            return currMtx[i-1][j]
        else:
            return -1

    def getTopRight_Part1(self, currMtx, i, j):
        if i >= 1 and j <= (self.cols - 2):
            return currMtx[i-1][j+1]
        else:
            return -1

    def getLeft_Part1(self, currMtx, i, j):
        if j >= 1:
            return currMtx[i][j-1]
        else:
            return -1

    def getRight_Part1(self, currMtx, i, j):
        if j <= (self.cols - 2):
            return currMtx[i][j+1]
        else:
            return -1

    def getBottomLeft_Part1(self, currMtx, i, j):
        if i <= (self.rows - 2) and j >= 1:
            return currMtx[i+1][j-1]
        else:
            return -1

    def getBottomMiddle_Part1(self, currMtx, i, j):
        if i <= (self.rows - 2):
            return currMtx[i+1][j]
        else:
            return -1

    def getBottomRight_Part1(self, currMtx, i, j):
        if i <= (self.rows - 2) and j <= (self.cols - 2):
            return currMtx[i+1][j+1]
        else:
            return -1

    # floor = '.', empty seat = 'L', occupied seat = '#'
    # all decisions based on # of occupied seats adjacent to given seat
    # adjacent meaning 8 surrounding seats
    # Rules:
    # 1) if seat is L, and NO occupied seats adj to it, seat becomes #
    # 2) if seat is # and >= 4 seats adj to it are #, then seat becomes L
    # 3) otherwise, seat's state does not change
    # CHANGES ARE APPLIED TO EVERY SEAT SIMULTANEOUSLY
    # so am using a copied mtx for new values and old mtx for decisions

    def getNewCellValue_Part1(self, currMtx, currVal, i, j):
        adjCellVals = []
        adjCellVals.append(self.getTopLeft_Part1(currMtx, i, j))
        adjCellVals.append(self.getTopMiddle_Part1(currMtx, i, j))
        adjCellVals.append(self.getTopRight_Part1(currMtx, i, j))
        adjCellVals.append(self.getLeft_Part1(currMtx, i, j))
        adjCellVals.append(self.getRight_Part1(currMtx, i, j))
        adjCellVals.append(self.getBottomLeft_Part1(currMtx, i, j))
        adjCellVals.append(self.getBottomMiddle_Part1(currMtx, i, j))
        adjCellVals.append(self.getBottomRight_Part1(currMtx, i, j))
        countOccupiedAdjSeats = adjCellVals.count('#')
        if currVal == 'L' and countOccupiedAdjSeats == 0:
            newVal = '#'
        elif currVal == '#' and countOccupiedAdjSeats >= 4:
            newVal = 'L'
        else:
            newVal = currVal
        return newVal

    def changeStates_Part1(self, currMtx):
        newMtx = deepcopy(currMtx)
        for i in range(self.rows):
            for j in range(self.cols):
                currVal = currMtx[i][j]
                newVal = self.getNewCellValue_Part1(currMtx, currVal, i, j)
                newMtx[i][j] = newVal
        return newMtx

    def compareMtx(self, mtx1, mtx2):
        countDiff = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if mtx1[i][j] != mtx2[i][j]:
                    countDiff += 1
        return countDiff

    def printMtx(self, mtx):
        print("\n")
        for i in range(self.rows):
            print(mtx[i])

    def getNumOccupiedSeats(self, mtx):
        count = 0
        for i in range(self.rows):
            count += mtx[i].count('#')
        return count

    def printAnswer_Part1(self, result):
        print("Part 1 Answer: Num Occupied Seas --> %i" % result)

    def getAnswer_Part1(self):
        print("\nPart 1 - Calculations Starting Now!")
        iteration = 0
        currMtx = deepcopy(self.mtx)
        newMtx = self.changeStates_Part1(currMtx)
        iteration += 1
        while self.compareMtx(currMtx, newMtx) > 0:
            currMtx = deepcopy(newMtx)
            newMtx = self.changeStates_Part1(currMtx)
            iteration += 1
        result = self.getNumOccupiedSeats(newMtx)
        self.printAnswer_Part1(result)

# -------------------------------------------------------------------------

    def getTopLeft_Part2(self, currMtx, i, j):
        curri = i
        currj = j
        if curri < 1 or currj < 1:
            return -1
        curri -= 1
        currj -= 1
        while curri >= 1 and currj >= 1 and currMtx[curri][currj] == '.':
            curri -= 1
            currj -= 1
        return currMtx[curri][currj]

    def getTopMiddle_Part2(self, currMtx, i, j):
        curri = i
        currj = j
        if curri < 1:
            return -1
        curri -= 1
        while curri >= 1 and currMtx[curri][currj] == '.':
            curri -= 1
        return currMtx[curri][currj]

    def getTopRight_Part2(self, currMtx, i, j):
        curri = i
        currj = j
        if curri < 1 or currj > (self.cols - 2):
            return -1
        curri -= 1
        currj += 1
        while curri >= 1 and currj <= (self.cols - 2) and currMtx[curri][currj] == '.':
            curri -= 1
            currj += 1
        return currMtx[curri][currj]

    def getLeft_Part2(self, currMtx, i, j):
        curri = i
        currj = j
        if currj < 1:
            return -1
        currj -= 1
        while currj >= 1 and currMtx[curri][currj] == '.':
            currj -= 1
        return currMtx[curri][currj]

    def getRight_Part2(self, currMtx, i, j):
        curri = i
        currj = j
        if currj > (self.cols - 2):
            return -1
        currj += 1
        while currj <= (self.cols - 2) and currMtx[curri][currj] == '.':
            currj += 1
        return currMtx[curri][currj]

    def getBottomLeft_Part2(self, currMtx, i, j):
        curri = i
        currj = j
        if curri > (self.rows - 2) or currj < 1:
            return -1
        currj -= 1
        curri += 1
        while curri <= (self.rows - 2) and currj >= 1 and currMtx[curri][currj] == '.':
            currj -= 1
            curri += 1
        return currMtx[curri][currj]

    def getBottomMiddle_Part2(self, currMtx, i, j):
        curri = i
        currj = j
        if curri > (self.rows - 2):  # if we can't move anywhere
            return -1
        curri += 1
        while curri <= (self.rows - 2) and currMtx[curri][currj] == '.':
            curri += 1
        return currMtx[curri][currj]

    def getBottomRight_Part2(self, currMtx, i, j):
        curri = i
        currj = j
        if curri > (self.rows - 2) or currj > (self.cols - 2):
            return -1
        curri += 1
        currj += 1
        while curri <= (self.rows - 2) and currj <= (self.cols - 2) and currMtx[curri][currj] == '.':
            curri += 1
            currj += 1
        return currMtx[curri][currj]

    def getNewCellValue_Part2(self, currMtx, currVal, i, j):
        adjCellVals = []
        adjCellVals.append(self.getTopLeft_Part2(currMtx, i, j))
        adjCellVals.append(self.getTopMiddle_Part2(currMtx, i, j))
        adjCellVals.append(self.getTopRight_Part2(currMtx, i, j))
        adjCellVals.append(self.getLeft_Part2(currMtx, i, j))
        adjCellVals.append(self.getRight_Part2(currMtx, i, j))
        adjCellVals.append(self.getBottomLeft_Part2(currMtx, i, j))
        adjCellVals.append(self.getBottomMiddle_Part2(currMtx, i, j))
        adjCellVals.append(self.getBottomRight_Part2(currMtx, i, j))
        countOccupiedAdjSeats = adjCellVals.count('#')
        if currVal == 'L' and countOccupiedAdjSeats == 0:
            newVal = '#'
        elif currVal == '#' and countOccupiedAdjSeats >= 5: # changed for part2
            newVal = 'L'
        else:
            newVal = currVal
        return newVal

    def changeStates_Part2(self, currMtx):
        newMtx = deepcopy(currMtx)
        for i in range(self.rows):
            for j in range(self.cols):
                currVal = currMtx[i][j]
                newVal = self.getNewCellValue_Part2(currMtx, currVal, i, j)
                newMtx[i][j] = newVal
        return newMtx

    def printAnswer_Part2(self, result):
        print("Part 2 Answer: Num Occupied Seas --> %i\n" % result)

    def getAnswer_Part2(self):
        print("\nPart 2 - Calculations Starting Now!")
        iteration = 0
        currMtx = deepcopy(self.mtx)
        newMtx = self.changeStates_Part2(currMtx)
        iteration += 1
        test = self.compareMtx(currMtx, newMtx)
        while self.compareMtx(currMtx, newMtx) > 0:
            currMtx = deepcopy(newMtx)
            newMtx = self.changeStates_Part2(currMtx)
            iteration += 1
        result = self.getNumOccupiedSeats(newMtx)
        self.printAnswer_Part2(result)


sol = AOC_DAY11("aoc_2020_day11_input1.txt")
sol.readFile()
sol.getAnswer_Part1()
sol.getAnswer_Part2()
