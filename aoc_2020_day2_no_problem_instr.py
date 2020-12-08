# ------ Advent of Code - 2020
# ------ Day 2: Password Philosophy
# ------ Frannie Richert
# ------ December 2, 2020

"""
-------------------------------- Part 1
"""



# --- OPEN file of numbers
f = open("aoc_2020_day2_input1.txt", "r")

# --- CREATE five arrays
lineArr = []
minArr = []
maxArr = []
letterArr = []
passwordArr = []

# --- ADD items to arrys
# loop through lines in file until no more lines
# add items to array, make sure they are int items
while True:
    currline = f.readline().strip()  # strip removes newline char
    if not currline:  # if empty, i.e. reached end of file
        break
    else:  # non-empty line, contains data

        lineArr.append(currline)

        # -- 1) first look for dash, which separates numbers
        dashPos = currline.find('-')
        spacePos = currline.find(' ')
        colonPos = currline.find(':')
        
        # -- 2) fill in arrays based on positions above
        minArr.append(int(currline[0:dashPos]))
        maxArr.append(int(currline[(dashPos+1):spacePos]))
        letterArr.append(currline[(spacePos+1):colonPos])
        passwordArr.append(currline[(colonPos+2):len(currline)])

f.close()

# --- CREATE variable to hold valid password counds
validPasswordCount = 0

# --- LOOP through each password to see if it is valid given char. above
for i in range(len(passwordArr)):
    currpw = passwordArr[i]
    currcount = currpw.count(letterArr[i])
    if currcount >= minArr[i] and currcount <= maxArr[i]:
        validPasswordCount += 1
        print("Iteration: %i, Curr Line: %s, Curr Count: %i" % (i, lineArr[i], validPasswordCount))


print("Part 1: Count Valid Passwords ---> %i" % validPasswordCount)

"""
-------------------------------- Part 2
"""

# reset valid password count
validPasswordCount = 0

# --- LOOP through each password to see if it is valid given char. above
for i in range(len(passwordArr)):
    currpw = passwordArr[i]
    currpos1 = minArr[i]
    currpos2 = maxArr[i]
    currletter = letterArr[i]

    # -- Check if char is in first position and not second
    if currpw[(currpos1-1)] == currletter and currpw[(currpos2-1)] != currletter:
        validPasswordCount += 1
        print("Iter: %i, Currline: %s" % (i,lineArr[i]))
    # -- Check if char is in second position and not first
    elif currpw[(currpos1-1)] != currletter and currpw[(currpos2-1)] == currletter:
        validPasswordCount += 1
        print("Iter: %i, Currline: %s" % (i,lineArr[i]))





print("Part 2: Count Valid Passwords ---> %i" % validPasswordCount)
