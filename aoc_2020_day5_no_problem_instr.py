# ------ Advent of Code - 2020
# ------ Day 5: Binary Boarding
# ------ Frannie Richert
# ------ December 5, 2020

"""
-------------------------------- Part 1
"""

# ------ Let's make a class!

class AOC_DAY5():

    # --- Initializer function
    def __init__(self, filename):
        self.filename = filename
        self.seatCount = 0
        self.seatArr = []
        self.fillSeatArr()
        self.rowArr = []
        self.colArr = []
        self.idArr = []
        self.maxID = 0

        # part 2
        self.rowColArr = []
        self.minRow = 0
        self.maxRow = 0

    # --- Fill array with file contents, each line is an element of array
    def fillSeatArr(self):
        # --- OPEN file of data
        f = open("aoc_2020_day5_input1.txt", "r")
        # --- GET all lines from file
        fLines = f.readlines()
        # --- CLOSE file
        f.close()
        # --- PUT each line of file into arr element
        for line in fLines:
            # DON'T FORGET TO STRIP OUT NEWLINE CHAR
            self.seatArr.append(line.strip())  
            self.seatCount += 1

    # --- Find ROW of seat
    def findSeatRow(self):
        for i in range(self.seatCount):
            currSeat = self.seatArr[i]
            # last 3 chars are for the column #
            # first 7 are for the row #
            currMin = 0
            currMax = 127
            for j in range(len(currSeat) - 3):
                
                # if at least number, f = take lower, b = take higher
                if j == (len(currSeat) - 4):
                    if currSeat[j] == 'F':
                        self.rowArr.append(int(currMin))
                    elif currSeat[j] == 'B':
                        self.rowArr.append(int(currMax))

                else:
                    # + 1 needed to get currect outcome
                    delta = (currMax+1 - currMin)
                    # if F, keep bottom half, i.e. min stays same, max is halved
                    if currSeat[j] == 'F':
                        currMax -= (delta/2)
                    elif currSeat[j] == 'B':
                        currMin += (delta/2) 

    # --- Find COLUMN of Seat
    def findSeatCol(self):
        for i in range(self.seatCount):
            currSeat = self.seatArr[i]
            # last 3 chars are for the column #
            # first 7 are for the row #
            currMin = 0
            currMax = 7
            for j in range((len(currSeat) - 3),len(currSeat)):
                
                # if L, keep lower half. if R, keep higher half
                if j == (len(currSeat) - 1):
                    if currSeat[j] == 'L':
                        self.colArr.append(int(currMin))
                    elif currSeat[j] == 'R':
                        self.colArr.append(int(currMax))

                else:
                    # + 1 needed to get currect outcome
                    delta = (currMax+1 - currMin)
                    # if L, keep lower half. if R, keep higher half
                    if currSeat[j] == 'L':
                        currMax -= (delta/2)
                    elif currSeat[j] == 'R':
                        currMin += (delta/2)

    # --- Find ID of seat = ROW * 8 + COL
    def findSeatID(self):
        for i in range(self.seatCount):
            self.idArr.append(self.rowArr[i]*8+self.colArr[i])

    # --- Find MAX ID
    def findMaxID(self):
        for i in range(self.seatCount):
            if self.idArr[i] > self.maxID:
                self.maxID = self.idArr[i]
        return self.maxID

    # -- Create an lists of row/seat lists
    def createRowSeatList(self):
        for i in range(self.seatCount):
            self.rowColArr.append([self.rowArr[i], self.colArr[i]])

    # --- Return whether or not a given ID is in the list
    def findSgeatID(self, id):
        try:
            pos = self.idArr.index(id)
            return(pos)
        except:
            return -1

    def getSeatCount(self):
        print(self.seatCount)

    def setMinMaxRow(self):
        # get unique rows and cols
        uniqueRows = set(self.rowArr)
        self.minRow = min(uniqueRows)
        self.maxRow = max(uniqueRows)




    def findMissingSeatID(self):
        
        self.createRowSeatList()
        self.setMinMaxRow()

        for i in range(self.minRow, self.maxRow+1):
            for j in range(max(self.colArr)):

                # if this particular value is not in our list of seats
                if [i,j] not in self.rowColArr:
                    # get seat ID
                    currCalcSeatID = i*8 + j
                    valLessOne = self.findSgeatID(currCalcSeatID-1)
                    valPlusOne = self.findSgeatID(currCalcSeatID+1)
                    
                    if valLessOne > 0 and valPlusOne > 0:
                        return currCalcSeatID

        return -1

                    


sol = AOC_DAY5("aoc_2020_day5_input1.txt")
sol.findSeatRow()
sol.findSeatCol()
sol.findSeatID()
print("Part 1 Answer: Max Seat Value ---> %i" % sol.findMaxID())

"""
-------------------------------- Part 2
"""

print("Part 2: Missing Seat ID ---> %i" % sol.findMissingSeatID())
