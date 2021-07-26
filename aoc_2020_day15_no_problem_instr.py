
import time 
START = time.time()

class AOC_DAY15:

    def __init__(self, filename):
        self.filename = filename
        self.readFile()

    def readFile(self):
        self.startNums = []
        with open(self.filename, "r") as input:
            raw = input.readline().strip("n").split(",")
            self.startNums  = [int(i) for i in raw]
            input.close()

    def playGamePart1(self, stopNum):
        turnVals = []
        i = 0
        
        #1) First, input the starting numbers
        turnVals.extend(self.startNums)
        i +=len(turnVals)

        #2) Second, start the game and continue until turnVals has 2,020 #'s
        while i < stopNum:
            print(i)
            prevNumber = turnVals[i-1]
            # --- if we've only seen the previous number 1 time before
            if turnVals.count(prevNumber) == 1:
                turnVals.append(0)
           # --- the # had been spoken > 1 time before, find most recent 2 times positions
           # and subtract them to get the new number
            else:
                posClosest1 = len(turnVals) - turnVals[::-1].index(prevNumber) -1
                posClosest2 = len(turnVals) - turnVals[::-1].index(prevNumber, turnVals[::-1].index(prevNumber)+1) -1
                turnVals.append(posClosest1 - posClosest2)
            i += 1
        return turnVals[stopNum-1]

    def updateDictionary(self, dict, key, pos):
        if key in dict: # major slowdown if using .keys()
            dict[key]['closest2'] = dict[key]['closest1']
            dict[key]['closest1'] = pos
        else:
            dict[key] = {'closest1' : pos, 'closest2' : None}

    def playGamePart2(self, stopNum):
        lastSeenDict = {}
        i = 0
        prevVal = None
        
        #1) First, input the starting numbers
        for val in self.startNums:
            lastSeenDict[str(val)] = {'closest1' : i+1, 'closest2' : None}
            prevVal = val
            i += 1

        #2) Second, start the game and continue until reach desired # of turns
        while i < stopNum:

            if i % 200000 == 0:
                print("i = " + str(i) +   ", elapsed time (sec): " + str(round(time.time() - START,4)))

            # if 2nd closest position is none of prev val, add/update zero
            if lastSeenDict[str(prevVal)]['closest2'] == None:
                val = 0
            else:
                val = lastSeenDict[str(prevVal)]['closest1'] - lastSeenDict[str(prevVal)]['closest2']
                
            self.updateDictionary(lastSeenDict, str(val), i+1)
            prevVal = val
            i += 1

        return val

    def getPart1Answer(self):
        pos2020 = self.playGamePart1(2020)
        print("\n\nPart 1 Answer: %i\n\n" % (pos2020))

    def getPart2Answer(self):
        pos30000000 = self.playGamePart2(30000000)
        print("\n\nPart 2 Answer: %i\n\n" % (pos30000000))

# ---------------------------- Answers

solution = AOC_DAY15("aoc_2020_day15_input1.txt")
solution.getPart1Answer()
solution.getPart2Answer()