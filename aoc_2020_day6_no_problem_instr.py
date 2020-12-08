# ------ Advent of Code - 2020
# ------ Day 6: Custom Customs
# ------ Frannie Richert
# ------ December 6, 2020

"""
-------------------------------- Part 1
"""


# ------ Let's make a class!

class AOC_DAY6():

    # --- Initializer function
    def __init__(self, filename):
        self.filename = filename
        self.groupStrArr = []
        self.numGroups = 0
        self.yesArr = []

        # --- part 2
        self.groupListArr = []
        self.groupListYesArr = []

    # --- Open and read file
    def readFilePart1(self):
        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()
        # creating an arry of string values
        currstr = ''
        countBlankLines = 0
        for i in range(len(lines)):
            if lines[i].strip() == '':
                self.groupStrArr.append(currstr)
                currstr = ''
                self.numGroups += 1
                countBlankLines += 1
            elif i == (len(lines)-1):
                currstr += lines[i].strip()
                self.groupStrArr.append(currstr)
                currstr = ''
                self.numGroups += 1
                countBlankLines += 1
            else:
                currstr += lines[i].strip()

    # --- PART 2 -- Open and read file, need to keep individuals from group
    def readFilePart2(self):
        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()

        # -- add a blank list for each group 
        for i in range(self.numGroups):
            self.groupListArr.append([])

        i = 0 
        group = 0
        while i < len(lines):
            if lines[i].strip() == '':
                group += 1
            else:
                self.groupListArr[group].append(lines[i].strip())
            i += 1


    # --- PART 2 - EVERY person in group has to answer or else do not count
    def tallySharedAnswers(self):
        
        for i in range(self.numGroups):

            currgroup = self.groupListArr[i]
            numGroupMembers = len(currgroup)
            uniqueAnswers = list(set(list(self.groupStrArr[i])))
            numUniqueAnswers = len(uniqueAnswers)

            """print("--- Group Members: %i" % numGroupMembers )
            print(currgroup)"""

            countList = [0 for i in range(numUniqueAnswers)]

            for j in range(numUniqueAnswers):
                currCount = 0
                for k in range(numGroupMembers):
                    currChar = uniqueAnswers[j]                
                    currStr = currgroup[k]
                    if currChar in currStr:
                        currCount += 1
                countList[j] = currCount

            for i in range(numUniqueAnswers):
                if countList[i] < numGroupMembers:
                    countList[i] = 0

            # Need to divide by # of group members to get # of questions shared.
            self.groupListYesArr.append(sum(countList)/numGroupMembers)


    # --- Return count for part 2
    def getSharedAnswerSum(self):
        total = 0
        for i in self.groupListYesArr:
            total += i
        return total

    # --- For each group (i.e. string) in arr, convert to list, then set
    # and count unique answers
    def tallyAtleastOneYesAnswers(self):
        for i in range(self.numGroups):
            # print("\n-------------")
            currstr = self.groupStrArr[i]
            currlist = list(self.groupStrArr[i])
            currset = set(list(self.groupStrArr[i]))
            """print("Count Chars: %i" % len(self.groupStrArr[i]))
            print(currstr)
            print(currlist)
            print(currset)
            print("Count Unique Chars: %i" % len(currset))"""
            self.yesArr.append(len(set(list(self.groupStrArr[i]))))

    # -- Get yes count
    def getAtleastOneYesSum(self):
        total = 0
        for i in range(self.numGroups):
            total += self.yesArr[i]
        return total

sol = AOC_DAY6("aoc_2020_day6_input1.txt")
sol.readFilePart1()
sol.tallyAtleastOneYesAnswers()
print("Part 1 Answer: Yes Sum Counts --> %i" % sol.getAtleastOneYesSum())


sol.readFilePart2()
sol.tallySharedAnswers()
print("Part 2 Answer: Yes Sum Counts --> %i" % sol.getSharedAnswerSum())

