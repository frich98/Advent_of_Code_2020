# ------ Advent of Code - 2020
# ------ Day 12: Rain Risk
# ------ Frannie Richert
# ------ December 19, 2020


from copy import deepcopy


class AOC_DAY12():

    def __init__(self, filename):
        self.filename = filename
        self.numInstr = 0
        self.arr = []  # list of lists, direction + int pairs
        self.startPt_part1 = [0,0]
        self.currPt_part1 = [0,0]
        self.currDir_part1 = 'E'  # the ship starts by facing East(E)
        self.moveList_part1 = []
        self.createMoveList_part1()

        # will be used to change direction given degrees
        self.dirs = ['N', 'E', 'S', 'W']

        # waypoint for part 2, position is relative to the ship
        # if ship moves, waypoint moves with it
        self.startWaypoint = [1, 10, 0, 0]  # NESW
        self.currWaypoint = [1, 10, 0, 0]
        self.moveList_part2 = []
        self.createMoveList_part2()
        self.startPt_part2 = [0,0,0,0]
        self.currPt_part2 = [0,0,0,0]
        self.currDir_part2 = 'E'  # the ship starts by facing East(E)

    def readFile(self):
        f = open(self.filename, "r")
        fLines = f.readlines()
        f.close()
        self.numInstr = len(fLines)
        for i in range(self.numInstr):
            self.arr.append([])
            currLine = fLines[i].strip()
            self.arr[i].append(currLine[0])
            self.arr[i].append(int(currLine[1:]))

    #source: https://en.wikipedia.org/wiki/Taxicab_geometry
    def calcManhattanDist(self, p1, q1):
        total = 0
        for i in range(len(p1)):
            total += abs(p1[i] - q1[i])
        return total

    def changeDir_part1(self, numDegrees, L_or_R):
        # change degrees into number 90 degree turns
        numRotations = int(numDegrees / 90) * (-1 if L_or_R == 'L' else 1)
        newDirIdx = (self.dirs.index(self.currDir_part1) + numRotations) % len(self.dirs)
        self.currDir_part1 = self.dirs[newDirIdx]

    def moveNorth_part1(self, numSpots):
        self.currPt_part1[1] += numSpots
    def moveSouth_part1(self, numSpots):
        self.currPt_part1[1] -= numSpots
    def moveWest_part1(self, numSpots):
        self.currPt_part1[0] -= numSpots
    def moveEast_part1(self, numSpots):
        self.currPt_part1[0] += numSpots
    def createMoveList_part1(self):
        self.moveList_part1 = [self.moveNorth_part1, self.moveEast_part1,
                         self.moveSouth_part1, self.moveWest_part1]
       
    def findEndPoint_Part1(self):
        for i in range(self.numInstr):
            currInstrDir = self.arr[i][0]
            currInstrInt = self.arr[i][1]
            if currInstrDir in self.dirs:
                idx = self.dirs.index(currInstrDir)
                self.moveList_part1[idx](currInstrInt)
            # if left or right, turn by int degrees
            elif currInstrDir == 'L' or currInstrDir == 'R':
                self.changeDir_part1(currInstrInt, currInstrDir)         
            # if forward, go in current direction
            elif currInstrDir == 'F':
                idx = self.dirs.index(self.currDir_part1)
                self.moveList_part1[idx](currInstrInt)  
        dist = self.calcManhattanDist(self.startPt_part1, self.currPt_part1)
        print("Part 1 Answer: Manhattan Distance --> %i" % dist)

# ------------------------------------------------------------------------

    def changeDir_part2_helper(self, numDegrees, L_or_R, currDir):
        numRotations = int(numDegrees / 90) * (-1 if L_or_R == 'L' else 1)
        newDirIdx = (self.dirs.index(currDir) + numRotations) % len(self.dirs)
        return self.dirs[newDirIdx]

    def changeDir_part2(self, numDegrees, L_or_R):
        # change degrees into number 90 degree turns
        currWP = deepcopy(self.currWaypoint)
        for i in range(len(self.dirs)):
            currDir = self.dirs[i]
            newDir = self.changeDir_part2_helper(numDegrees, L_or_R, currDir)
            self.currWaypoint[self.dirs.index(newDir)] = currWP[self.dirs.index(currDir)]

    def moveNorth_part2(self, numSpots):
        self.currWaypoint[0] += numSpots
    def moveSouth_part2(self, numSpots):
        self.currWaypoint[2] += numSpots
    def moveWest_part2(self, numSpots):
        self.currWaypoint[3] += numSpots
    def moveEast_part2(self, numSpots):
        self.currWaypoint[1] += numSpots
    def createMoveList_part2(self):
        self.moveList_part2 = [self.moveNorth_part2, self.moveEast_part2,
                         self.moveSouth_part2, self.moveWest_part2]

    def moveForward_part2(self, numSpots):

        waypointAdders = [numSpots * self.currWaypoint[i] for i in range(len(self.dirs))]

        # move north/south
        if waypointAdders[0] > 0 or waypointAdders[2] > 0:
            # positive indicates net north, negative indicates net south
            mvmt = waypointAdders[0] - waypointAdders[2]
            absMvmt = abs(mvmt)

            if mvmt < 0:  # SOUTH
                # if north position value is > 0 and <= movement needed
                # set north to zero and add any delta to south
                if self.currPt_part2[0] > 0 and self.currPt_part2[0] <= absMvmt:
                    absMvmt -= self.currPt_part2[0]
                    self.currPt_part2[0] = 0                    
                    if absMvmt > 0:
                        self.currPt_part2[2] += absMvmt
                # if north position value is > 0 and its value is > abs mvmt
                # subtract absolute movement from it, do not change south
                elif self.currPt_part2[0] > 0 and self.currPt_part2[0] > absMvmt:
                    self.currPt_part2[0] -= absMvmt
                    absMvmt = 0
                # no north value currently, add all to south
                else:
                    self.currPt_part2[2] += absMvmt
                    absMvmt = 0

            elif mvmt > 0:  # NORTH
                # if south position value is > 0 and <= movement needed
                # set south to zero and add any delta to north
                if self.currPt_part2[2] > 0 and self.currPt_part2[2] <= absMvmt:
                    absMvmt -= self.currPt_part2[2]
                    self.currPt_part2[2] = 0
                    if absMvmt > 0:
                        self.currPt_part2[0] += absMvmt
                # if south position value is > 0 and its value is > abs mvmt
                # subtract absolute movement from it, do not change north
                elif self.currPt_part2[2] > 0 and self.currPt_part2[2] > absMvmt:
                    self.currPt_part2[2] -= absMvmt
                    absMvmt = 0
                # no south value currently, add all to north
                else:
                    self.currPt_part2[0] += absMvmt
                    absMvmt = 0
        
        # move east/west
        if waypointAdders[1] > 0 or waypointAdders[3] > 0:
            # positive indicates net east, negative indicates net west
            mvmt = waypointAdders[1] - waypointAdders[3]
            absMvmt = abs(mvmt)

            if mvmt > 0:  # EAST
                # if west position value is > 0 and <= movement needed
                # set west to zero and add any delta to east
                if self.currPt_part2[3] > 0 and self.currPt_part2[3] <= absMvmt:
                    absMvmt -= self.currPt_part2[3]
                    self.currPt_part2[3] = 0                    
                    if absMvmt > 0:
                        self.currPt_part2[1] += absMvmt
                # if west position value is > 0 and its value is > abs mvmt
                # subtract absolute movement from it, do not change east
                elif self.currPt_part2[3] > 0 and self.currPt_part2[3] > absMvmt:
                    self.currPt_part2[3] -= absMvmt
                    absMvmt = 0
                # no west value currently, add all to east
                else:
                    self.currPt_part2[1] += absMvmt
                    absMvmt = 0

            elif mvmt < 0:  # WEST
                # if east position value is > 0 and <= movement needed
                # set east to zero and add any delta to west
                if self.currPt_part2[1] > 0 and self.currPt_part2[1] <= absMvmt:
                    absMvmt -= self.currPt_part2[1]
                    self.currPt_part2[1] = 0
                    if absMvmt > 0:
                        self.currPt_part2[3] += absMvmt
                # if east position value is > 0 and its value is > abs mvmt
                # subtract absolute movement from it, do not change west
                elif self.currPt_part2[1] > 0 and self.currPt_part2[1] > absMvmt:
                    self.currPt_part2[1] -= absMvmt
                    absMvmt = 0
                # no east value currently, add all to west
                else:
                    self.currPt_part2[3] += absMvmt
                    absMvmt = 0

    def findEndPoint_Part2(self):
        for i in range(self.numInstr):
            currInstrDir = self.arr[i][0]
            currInstrInt = self.arr[i][1]
            # if NESW, move waypoint 
            if currInstrDir in self.dirs:
                idx = self.dirs.index(currInstrDir)
                self.moveList_part2[idx](currInstrInt)
            # if left or right, turn waypoint left (counterclockwise) or
            # right (clockwise) around the ship
            elif currInstrDir == 'L' or currInstrDir == 'R':
                self.changeDir_part2(currInstrInt, currInstrDir) 
            # if forward, move ship forward to waypoint a number of times
            # equal to given value
            elif currInstrDir == 'F':
                self.moveForward_part2(currInstrInt)
        dist = self.calcManhattanDist(self.startPt_part2, self.currPt_part2)
        print("Part 2 Answer: Manhattan Distance --> %i" % dist)


sol = AOC_DAY12("aoc_2020_day12_input1.txt")
sol.readFile()
sol.findEndPoint_Part1()
sol.findEndPoint_Part2()
