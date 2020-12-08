# ------ Advent of Code - 2020
# ------ Day 7: Handy Haversacks
# ------ Frannie Richert
# ------ December 7, 2020

from copy import deepcopy


class AOC_DAY7():

    # --- Initializer function
    def __init__(self, filename):
        
        self.filename = filename
        self.lineArr = []

        self.numRules = 0
        self.colorList = []
        self.shinyGoldBagColorList = []

        # --- part 2
        self.countShinyGoldBagContents = 1

    # --- Read file - contents will be : x bag contains  # y bag(s), z bag(s)..
    def readFile(self):
        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()
        self.numRules = len(lines)
        for i in range(self.numRules):
            # will contain : full line str, main color str, 
            # list of held colors, list of held numbers per color
            self.lineArr.append(["", "", [], []])

            # --- 1ST ITEM
            currLine = lines[i].strip()
            self.lineArr[i][0] = currLine

            # --- 2ND ITEM
            mainPos = currLine.index(" bags contain ")
            self.lineArr[i][1] = currLine[:mainPos]

            stringRestOf = currLine[(mainPos + len(" bags contain ")):]
            heldColors = stringRestOf.count(",") + 1

            # 3RD AND 4TH ITEMS WILL BE FILLED OUT HERE
            for j in range(heldColors):

                pos = stringRestOf.index(" bag")
                currString = stringRestOf[:pos].strip()
                if currString == "no other":
                    self.lineArr[i][2].append("no other")
                    self.lineArr[i][3].append("0")
                    continue

                spacePos = stringRestOf.index(" ")
                currNum = int(stringRestOf[:spacePos])
                currColor = stringRestOf[(spacePos + 1):pos]

                self.lineArr[i][2].append(currColor)
                self.lineArr[i][3].append(currNum)

                if currNum > 1:
                    stringRestOf = stringRestOf[(pos + len(" bags, ")):]
                else:
                    stringRestOf = stringRestOf[(pos + len(" bag, ")):]


    # --- Retrieve ALL BAG TYPES which will hold gold
    # there will be some "recursion" going on here.
    def findColorsWhichHoldShinyGoldColorBag(self):
        bagSearchColorList = ["shiny gold"]
        while len(bagSearchColorList) != 0:
            currSearchColor = bagSearchColorList.pop(0)
            for i in range(self.numRules):
                currColorSet = self.lineArr[i][2]
                if currSearchColor in currColorSet and \
                   self.lineArr[i][1] not in self.shinyGoldBagColorList:
                    self.shinyGoldBagColorList.append(self.lineArr[i][1])
                    bagSearchColorList.append(self.lineArr[i][1])

    # --- get num bags
    def getNumBagsWhichHoldShinyGoldBag(self):
        return len(self.shinyGoldBagColorList)


    # part 2 helper function
    def noOtherColorsTF(self, color):
        for i in range(self.numRules):
            if self.lineArr[i][1] == color:
                if self.lineArr[i][2][0] == "no other":
                    return True
                else:
                    return False

    # --- Part 2 - find how many bags are contained in a gold bag
    def part2Recursion(self, startColor = "shiny gold", iter = 0):
        for i in range(self.numRules):
            if self.lineArr[i][1] == startColor:
                currColorsList = self.lineArr[i][2]
                currColorNums = self.lineArr[i][3]
                break
        if currColorsList[0] == "no other":
            return 1
        else:
            evalStr = ''
            for j in range(len(currColorsList)):
                if iter == 0:
                    adder = str(0)
                else:
                    adder = str(1)
                if j == 0 and j < (len(currColorsList) - 1): 
                    evalStr += '(' + adder + ' + ' + str(currColorNums[j]) + ' * self.part2Recursion("' + currColorsList[j] + '", iter = 1)) + '
                elif j == 0:
                    evalStr += '(' + adder + ' + ' + str(currColorNums[j]) + ' * self.part2Recursion("' + currColorsList[j] + '", iter = 1))'
                elif j < (len(currColorsList) - 1):
                    evalStr += '(' + str(currColorNums[j]) + ' * self.part2Recursion("' + currColorsList[j] + '", iter = 1)) + '
                else:
                    evalStr += '(' + str(currColorNums[j]) + ' * self.part2Recursion("' + currColorsList[j] + '", iter = 1))'
            return eval(evalStr)


sol = AOC_DAY7("aoc_2020_day7_input1.txt")
sol.readFile()
sol.findColorsWhichHoldShinyGoldColorBag()
part1Answer = sol.getNumBagsWhichHoldShinyGoldBag()
print("Part 1 Answer: Number Bags Can Hold Shiny Gold Bag --> %i" % part1Answer)

part2Answer = sol.part2Recursion()
print("Part 2 Answer: Number Bags Shiny Gold Holds --> %i" % part2Answer)
