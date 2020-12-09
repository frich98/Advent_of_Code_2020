# ------ Advent of Code - 2020
# ------ Day 9: Encoding Error
# ------ Frannie Richert
# ------ December 9, 2020


class AOC_DAY9():

    def __init__(self, filename, preambleLen = 25):
        self.filename = filename
        self.countNums = 0
        self.numArr = []
        self.preambleLen = 25

    def readFile(self):
        f = open(self.filename, "r")
        fLines = f.readlines()
        f.close()
        self.countNums = len(fLines)
        for i in range(self.countNums):
            self.numArr.append(int(fLines[i].strip()))

    def checkForNonIdenticalPairSum(self, idx):
        num = self.numArr[idx]
        startIdx = idx-self.preambleLen
        endIdx = idx  # range endIdx is not included, that's why not subtr 1
        for i in range(startIdx, endIdx):
            for j in range(startIdx, endIdx):
                if (i != j) and (self.numArr[i] + self.numArr[j]) == num:
                    return 1
        return -1

    def findInvalidNumPart1(self):
        idx = self.preambleLen
        while idx < self.countNums:
            result = self.checkForNonIdenticalPairSum(idx)
            if result == -1:
                return self.numArr[idx]
            idx += 1

    def whileSumLoop(self, startIdx):
        invalidNum = self.findInvalidNumPart1()
        currIdx = startIdx
        currSum = 0
        while currSum < invalidNum:
            currSum += self.numArr[currIdx]
            currIdx += 1
        if currSum == invalidNum:
            # look at instructions carefully, it wants the smallest and largest
            # numbers in the range, NOT the startIdx number and endIdx number
            # which is what I first did (without reading carefully)
            minNumInRange = min(self.numArr[startIdx:currIdx])
            maxNumInRange = max(self.numArr[startIdx:currIdx])
            return (minNumInRange + maxNumInRange)
        else:
            return -1

    def findContiguousSumSetPart2(self):
        for i in range(self.countNums):
            result = self.whileSumLoop(i)
            if result > 0:
                return result

sol = AOC_DAY9("aoc_2020_day9_input1.txt", 25)
sol.readFile()
part1_answer = sol.findInvalidNumPart1()
print("Part 1 Answer: First Invalid Num --> %i" % part1_answer)
part2_answer = sol.findContiguousSumSetPart2()
print("Part 1 Answer: Sum Min & Max in Contiguous Range To Get Invalid Num --> %i" % part2_answer)
