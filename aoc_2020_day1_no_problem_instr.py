# ------ Advent of Code - 2020
# ------ Day 1: Report Repair
# ------ Frannie Richert
# ------ December 1, 2020

"""
-------------------------------- Part 1
"""

# --- OPEN file of numbers
f = open("aoc_2020_day1_input1.txt", "r")

# --- CREATE array to hold numbers
arr = []

# --- ADD items to arry
# loop through lines in file until no more lines
# add items to array, make sure they are int items
while True:
    currline = f.readline()
    if not currline:
        break
    else:
        arr.append(int(currline.strip()))

f.close()

# --- LOOP through i, j where i and j = len(arr)
answer = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == 2020:
            print("Answer (part 1): %i, arr[i] = %i, arr[j] = %i" % ( arr[i] * arr[j], arr[i], arr[j]))
            answer = arr[i] * arr[j]
            break
    if answer > 0:
        break

"""
-------------------------------- Part 2
"""

# --- LOOP through i, j where i and j = len(arr)
answer = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if (arr[i] + arr[j] + arr[k]) == 2020:
                print("Answer (part 2): %i, arr[i] = %i, arr[j] = %i, arr[k] %i" % (arr[i] * arr[j] * arr[k], arr[i], arr[j], arr[k]))
                answer = arr[i] * arr[j] * arr[k]
                break
        if answer > 0:
            break
    if answer > 0:
         break





