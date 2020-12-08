# ------ Advent of Code - 2020
# ------ Day 8: Handheld Halting
# ------ Frannie Richert
# ------ December 8, 2020

from copy import deepcopy

class AOC_DAY8():

    def __init__(self, filename):
        self.filename = filename
        self.numInstr = 0
        self.instrArr = []
        self.execInstrList = []
        self.accumulatorPart1 = 0

    def readFile(self):
        f = open(self.filename, "r")
        fLines = f.readlines()
        f.close()
        self.numInstr = len(fLines)
        for i in range(len(fLines)):
            # will hold [full text, instruction only, - or +, number, index]
            self.instrArr.append(["","", "", 0, 0])
            currLine = fLines[i].strip()
            self.instrArr[i][0] = currLine
            self.instrArr[i][1] = currLine[:3]
            self.instrArr[i][2] = currLine[3:5].strip()
            self.instrArr[i][3] = int(currLine[5:])
            self.instrArr[i][4] = i
    
    def findAccumulatorValPart1(self):
        i = 0
        while True:
            currCommand = self.instrArr[i]
            """print("\n -------------------------- ")
            print(currCommand)
            print("Accumulator: %i" % self.accumulatorPart1)"""
            if currCommand in self.execInstrList:
                i = -1
                return self.accumulatorPart1
            # built in code #1 - acc
            elif currCommand[1] == "acc":
                if currCommand[2] == '+':
                    self.accumulatorPart1 += currCommand[3]
                else:
                    self.accumulatorPart1 -= currCommand[3]
                i += 1
            # built in code #2  - "jmp"
            elif currCommand[1] == "jmp":
                if currCommand[2] == '+':
                    i += currCommand[3]
                else:
                    i -= currCommand[3]
            # built in code #3 - "nop"
            elif currCommand[1] == "nop":
                i += 1
            # make sure to append current command in run command list
            self.execInstrList.append(currCommand)


    def listNopJmpInstr(self):
        listNopJmpInstrIdx = []
        for i in range(self.numInstr):
            if self.instrArr[i][1] == "jmp" or self.instrArr[i][1] == "nop":
                listNopJmpInstrIdx.append(i)
        return listNopJmpInstrIdx

    def swapNopJmpLoopPart2(self):
        listIdx = self.listNopJmpInstr()

        for i in range(len(listIdx)):
            # print("\n-------------------- Iter %i" % i)
            tempList = deepcopy(self.instrArr)
            currInstr = tempList[listIdx[i]]
            if currInstr[1] == "nop":
                newInstr = ["jmp " + currInstr[2] + str(currInstr[3]), "jmp", currInstr[2], currInstr[3], currInstr[4]]
            elif currInstr[1] == "jmp":
                newInstr = ["nop " + currInstr[2] + str(currInstr[3]), "nop", currInstr[2], currInstr[3], currInstr[4]]
            tempList[listIdx[i]] = newInstr
            """print(currInstr)
            print(newInstr)"""
            result = self.findAccumulatorValPart2(tempList)
            if result > 0:
                print("Part 2 Answer: Accumulator Value with Fixed Instruction --> %i" % result)
                # print(currInstr)
                break


    def findAccumulatorValPart2(self, tempList):
        i = 0
        execInstrList = []
        accumulator = 0
        while True:
            # IF WE HAVE MADE IT TO END OF LIST!!
            if i > (len(tempList)-1):
                # print("Curr accumulator value: %i" % accumulator)
                return accumulator
            currCommand = tempList[i]
            # print("\n -------------------------- ")
            # print(currCommand)
            # print("Accumulator: %i" % accumulator)
            if currCommand in execInstrList:
                i = -1
                # print("Curr accumulator value: %i" % accumulator)
                return 0  # not successful, i.e. infinite loop
            # built in code #1 - acc
            elif currCommand[1] == "acc":
                if currCommand[2] == '+':
                    accumulator += currCommand[3]
                else:
                    accumulator -= currCommand[3]
                i += 1
            # built in code #2  - "jmp"
            elif currCommand[1] == "jmp":
                if currCommand[2] == '+':
                    i += currCommand[3]
                else:
                    i -= currCommand[3]
            # built in code #3 - "nop"
            elif currCommand[1] == "nop":
                i += 1
            # make sure to append current command in run command list
            execInstrList.append(currCommand)
        return 1 # SUCCESSFUL

sol = AOC_DAY8("aoc_2020_day8_input1.txt")
sol.readFile()
part1_answer = sol.findAccumulatorValPart1()
print("Part 1 Answer: Accumulator before duplicate command --> %i" % part1_answer)
sol.swapNopJmpLoopPart2()
