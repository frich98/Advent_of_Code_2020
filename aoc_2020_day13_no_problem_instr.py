# ------ Advent of Code - 2020
# ------ Day 13: Shuttle Search
# ------ Frannie Richert
# ------ December 23, 2020


from copy import deepcopy
from functools import reduce


class AOC_DAY13():

    def __init__(self, filename):
        self.filename = filename
        self.earliestDepartTime = 0
        self.fullBusList = []
        self.activeBusList = []
        self.activeBusOffsets = []
        self.activeBusRemainders = []
        self.part2List = []  # list of lists, [ai, ni]

    def setActiveBusList(self):
        for i in range(len(self.fullBusList)):
            if self.fullBusList[i] != 'x':
                self.activeBusList.append(self.fullBusList[i])

    def readFile(self):
        f = open(self.filename, "r")
        fLines = f.readlines()
        f.close()
        self.earliestDepartTime = int(fLines[0].strip())
        self.fullBusList = fLines[1].strip().split(',')
        for i in range(len(self.fullBusList)):
            if self.fullBusList[i] != 'x':
                self.fullBusList[i] = int(self.fullBusList[i])
        self.setActiveBusList()

    def setupTimeArr_Part1(self):
        arr = []
        for i in range(len(self.activeBusList)):
            currNum = self.activeBusList[i]
            currRemainder = self.earliestDepartTime % currNum
            currMultiple = int(self.earliestDepartTime / currNum)
            currDelta = currNum - currRemainder
            arr.append([currNum, currRemainder, currDelta, currMultiple])
        return arr

    def getEarliestBus_Part1(self):
        arr = self.setupTimeArr_Part1()
        minNum = 0
        minIdx = 0
        for i in range(len(arr)):
            if i == 0:
                minNum = arr[i][2]
                minIdx = i
            elif arr[i][2] < minNum:
                minNum = arr[i][2]
                minIdx = i
        answer = self.activeBusList[minIdx] * minNum
        print("Part 1 Answer: Minutes to Wait * Bus ID --> %i" % answer)

    def setData_Part2(self):
        # For part 2- using chinese remainder theorem
        # source: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
        # --- Setting offsets (raw)
        for i in range(len(self.activeBusList)):
            self.activeBusOffsets.append(self.fullBusList.index(self.activeBusList[i]))
        # --- Setting ai < ni
        for i in range(len(self.activeBusList)):
            self.activeBusRemainders.append(self.activeBusOffsets[i])
        # --- Creating a new list for use in part 2
        # ordering list by active bus #s (which are our moduli)
        # create new list, combo of two lists above
        for i in range(len(self.activeBusList)):
            self.part2List.append([self.activeBusList[i], self.activeBusRemainders[i]])

    """ ------- Sources for Part 2
    AOC Subreddit for day 13 gave me the idea for CRT
    Wikipedia for general info: 
        https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    Wikipedia for extended euclidean algo:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    Page for more detail and concrete example:
    http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/chinese_remainder.pdf
    mariothedog's github solution for this helped me out:
    https://github.com/mariothedog/Advent-of-Code-2020/blob/main/Day%2013/day_13.py
    """
    # Computes the gcd of given integers a and b as well as the
    # coefficients of Bezout's identity which are integers x and y
    # such that ax + by = gcd(a, b). Very useful when a, b are coprime
    def extEuclidAlgo(self, a, b):
        # Source: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
        b0 = b
        x0, x1 = 0, 1
        q = 0
        if b == 1: return 1
        while a > 1:
            q = a // b  # q is the quotient
            a, b = b, a%b  # b is the remainder of a/b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1

    def CRT_Part2(self):
        # N is the product of all bus ID's = moduli for CRT
        N = reduce(lambda a, b: a*b, self.activeBusList)
        # cumulative sum
        total = 0        
        for i in range(len(self.activeBusList)):
            # modulus = bus ID
            currMod = self.activeBusList[i]
            # remainder
            currRem = (currMod - self.activeBusOffsets[i]) % currMod
            # // is necessary to ensure currZ is correct integer
            # might be due to length of integer
            currZ = N // currMod 
            # calculate inverse using extended euclidean algorithm of z
            currY = self.extEuclidAlgo(currZ, currMod)
            #  accumulate
            total += (currRem * currY * currZ)
        print("Part 2 Answer: CRT --> %i" % (total % N))

sol = AOC_DAY13("aoc_2020_day13_input1.txt")
sol.readFile()
sol.getEarliestBus_Part1()
sol.setData_Part2()
sol.CRT_Part2()
