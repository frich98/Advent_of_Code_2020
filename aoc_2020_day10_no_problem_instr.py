# ------ Advent of Code - 2020
# ------ Day 10: Adapter Array
# ------ Frannie Richert
# ------ December 10, 2020


from copy import deepcopy


class AOC_DAY10():

    def __init__(self, filename):
        self.filename = filename
        self.arr = []
        self.arrSorted = []
        self.part1Deltas = [0, 0, 0]
        self.part2CountWays = 0

    def readFile(self):
        f = open(self.filename, "r")
        fLines = f.readlines()
        f.close()
        self.arrLen = len(fLines)
        for i in range(self.arrLen):
            self.arr.append(int(fLines[i].strip()))

    def sortArr(self):
        self.arrSorted = sorted(self.arr)

    def countDeltasPart1(self):
        self.sortArr()
        currJoltage = 0
        currIdx = 0
        # 1, 2, 3
        maxJoltage = max(self.arrSorted) + 3
        while currJoltage < maxJoltage:
            # see if +1 exists in list
            if (currJoltage + 1) in self.arrSorted or \
               (currJoltage + 1) == maxJoltage:
                currJoltage += 1
                self.part1Deltas[0] += 1
                currIdx += 1
                continue
            elif (currJoltage + 2) in self.arrSorted or \
                 (currJoltage + 2) == maxJoltage:
                currJoltage += 2
                self.part1Deltas[1] += 1
                currIdx += 1
                continue
            elif (currJoltage + 3) in self.arrSorted or \
                 (currJoltage + 3) == maxJoltage:
                currJoltage += 3
                self.part1Deltas[2] += 1
                currIdx += 1
                continue
            else:
                print("ADAPTER NOT HERE")
                currIdx += 1

    def printPart1Answer(self):
        answer = self.part1Deltas[0] * self.part1Deltas[2]
        print("Part 1 Answer: 1-Jolt * 3-Jolt = %i" % answer)

    def getDistinctArrangementsPart2(self):
        countWays = 1
        countConsec = 0
        arr=[]
        for j in range(1 + len(self.arrSorted) + 1):
            if j == 0:
                arr.append(0)
            elif j <= len(self.arrSorted):
                arr.append(self.arrSorted[j-1])
            else:
                arr.append(max(self.arrSorted) + 3)
        for i in range(len(arr)):
            if i > 0 and arr[i] == (arr[i-1]+1):
                countConsec+=1
            else:
                if countConsec == 1:
                    countWays *= 1
                elif countConsec == 2:
                    countWays *= 2
                elif countConsec == 3:
                    countWays *= 4
                elif countConsec == 4:
                    countWays *= 7
                countConsec = 0
        self.part2CountWays = countWays

    def printPart2Answer(self):
        print("Part 2 Answer: Count Distinct Ways --> %i" % self.part2CountWays)


sol = AOC_DAY10("aoc_2020_day10_input1.txt")
sol.readFile()
sol.countDeltasPart1()
sol.printPart1Answer()
sol.getDistinctArrangementsPart2()
sol.printPart2Answer()
