# ------ Advent of Code - 2020
# ------ Day 3: Toboggan Trajectory
# ------ Frannie Richert
# ------ December 3, 2020

"""
-------------------------------- Part 1
"""

from math import ceil

# --- OPEN file of data
f = open("aoc_2020_day3_input1.txt", "r")

# --- CREATE array to hold data
arr = []

# --- ADD data to array
# loop through lines in file until no more lines
# add items to array, make sure they are int items
while True:
    currline = f.readline()
    if not currline:
        break
    else:
        currlist = []
        currline = currline.strip()  # removes newline char
        for char in currline:
            currlist.append(char)
    arr.append(currlist)

# --- Close file
f.close()

# --- Figure out how many times to duplicate columns
# if we have to move right 3 times, and only down once for each slop
# the column length needs to be at least 3 times the row length
numRows = len(arr)
numCols = len(arr[0])
numColRepeats = ceil(numRows*3/numCols)
print("Data Size, Num Rows: %i, Num Cols: %i, Num Col Repeats: %i" % 
      (numRows, numCols, numColRepeats))
newArrRight3 = []
for k in range(numRows):
    newArrRight3.append(arr[k]*numColRepeats)


# --- LOOP start at top left position, moving right 3, over 1 until bottom of
# arr is reached
iter = 1
row = 0
col = 0
countTrees = 0

while row < numRows:
    currChar = newArrRight3[row][col]
    print("Curr Iter: %i, Curr Char: %c, Row: %i, Col: %i" % (iter, currChar, row, col))
    if currChar == '#':
        countTrees += 1
    row += 1
    col += 3
    iter += 1

print("Part 1 Answer: Number of Trees ---> %i" % countTrees)


"""
-------------------------------- Part 2
"""

# --- Figure out how many times to duplicate columns
# if we have to move right a MAX OF SEVEN times, and'
# only down or two for each slope,
# the column length needs to be at least 7 times the row length
numRows = len(arr)
numCols = len(arr[0])
numColRepeats = ceil(numRows*7/numCols)
print("Data Size, Num Rows: %i, Num Cols: %i, Num Col Repeats: %i" % 
      (numRows, numCols, numColRepeats))
newArrRight7 = []
for k in range(numRows):
    newArrRight7.append(arr[k]*numColRepeats)


choices = [[1,1], [3,1], [5,1], [7,1], [1,2]]
treeCounts = []

for i in choices:

    colMvmt = i[0]
    rowMvmt = i[1]

    # --- LOOP start at top left position, moving right 3, over 1 until bottom of
    # arr is reached
    iter = 1
    row = 0
    col = 0
    countTrees = 0

    while row < numRows:
        currChar = newArrRight7[row][col]
        print("Curr Iter: %i, Curr Char: %c, Row: %i, Col: %i" % (iter, currChar, row, col))
        if currChar == '#':
            countTrees += 1
        row += rowMvmt
        col += colMvmt
        iter += 1

    treeCounts.append(countTrees)

print(treeCounts)

treeMult = 1
for j in range(len(treeCounts)):
    treeMult *= treeCounts[j]
print("Part 2 Answer: Multipy of Tree Counts ---> %i" % treeMult)