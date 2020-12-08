# ------ Advent of Code - 2020
# ------ Day 4: Passport Processing
# ------ Frannie Richert
# ------ December 4, 2020

"""
-------------------------------- Part 1
"""

from copy import deepcopy

# --- OPEN file of data
f = open("aoc_2020_day4_input1.txt", "r")

# --- CREATE array to hold data
arr = []

# --- GET all lines from file
fLines = f.readlines()
 
# --- CLOSE file
f.close()

# --- PARSE lines into list of dictionaries

sampleDict = {
    "byr" : None,
    "iyr" : None,
    "eyr" : None,
    "hgt" : None,
    "hcl" : None, 
    "ecl" : None,
    "pid" : None,
    "cid" : None
}
 
# --- LOOP through lines in file, creading people dictionaries and adding to arr

test = "iyr:2010 byr:1934 eyr:2023 hgt:180cm hcl:#cfa07d ecl:gry"

idList = list(sampleDict.keys())
arr = []
countAdjLines = 0
personCount = -1
for line in fLines:
    currline = line.strip()
    if currline == "":
        countAdjLines = 0  # reset
    else:
        countAdjLines += 1
        # if we are starting over on a new person, create a new array person
        # and only then, increase # of people
        if countAdjLines == 1:
            personCount += 1
            arr.append(deepcopy(sampleDict))
        for id in idList:
            val = ''
            # return of 0 from currlind indicates ID not found
            if currline.find(id) < 0:
                continue
            # where in currline the ID field is
            i = currline.find(id) + len(id + ':')
            # if starting on 0, need to add 1, no space before 0th item
            if i == 0:
                i += 1
            while i < len(currline):
                if currline[i] == ' ':
                    break
                val += currline[i]
                i += 1
            arr[personCount][id] = val

# --- LOOP through arr, finding valid people
countValid = 0
for i in range(len(arr)):
    person = arr[i]
    if (person["cid"] == None and \
        sum([val is None for val in person.values()]) == 1) or \
        sum([val is None for val in person.values()]) == 0:
       arr[i]["valid_part1"] = True
       countValid += 1
    else:
        arr[i]["valid_part1"] = False

print("Count Total People: %i" % len(arr))
print("Part 1: Valid Passports ---> %i" % countValid)

"""
--- Part Two ---
"""

countValidPart2 = 0

for i in range(len(arr)):

    # Initial value, will change later
    arr[i]["valid_part2"] = False
    arr[i]["valid_part2_byr"] = False
    arr[i]["valid_part2_iyr"] = False
    arr[i]["valid_part2_eyr"] = False
    arr[i]["valid_part2_hgt"] = False
    arr[i]["valid_part2_hcl"] = False
    arr[i]["valid_part2_ecl"] = False
    arr[i]["valid_part2_pid"] = False
    arr[i]["valid_part2_cid"] = True  # this one doesn't matter
    
    # loop through keys
    for key in arr[i].keys():
        
        # ignore this key
        if key.find("valid_part1") > 0:
            continue

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if key == "byr":
            val = arr[i][key]
            if val == None:
                arr[i]["valid_part2_" + key] = False
                continue
            val = int(val)
            if val >= 1920 and val <= 2002:
                arr[i]["valid_part2_" + key] = True
                # print(key + ":True")
            else:
                arr[i]["valid_part2_" + key] = False

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if key == "iyr":
            val = arr[i][key]
            if val == None:
                arr[i]["valid_part2_" + key] = False
                continue
            val = int(val)
            if val >= 2010 and val <= 2020:
                arr[i]["valid_part2_" + key] = True
                # print(key + ":True")
            else:
                arr[i]["valid_part2_" + key] = False

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if key == "eyr":
            val = arr[i][key]
            if val == None:
                arr[i]["valid_part2_" + key] = False
                continue
            val = int(val)
            if val >= 2020 and val <= 2030:
                arr[i]["valid_part2_" + key] = True
                # print(key + ":True")
            else:
                arr[i]["valid_part2_" + key] = False

        """hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76."""

        if key == "hgt":
            val = arr[i][key]
            if val == None:
                arr[i]["valid_part2_" + key] = False
                continue

            if val.find("cm") > 0:
                val = int(val.strip("cm"))
                if val >= 150 and val <= 193:
                    arr[i]["valid_part2_" + key] = True
                    # print(key + ":True")
                else:
                    arr[i]["valid_part2_" + key] = False
            
            elif val.find("in") > 0:
                val = int(val.strip("in"))
                if val >= 59 and val <= 76:
                    arr[i]["valid_part2_" + key] = True
                    # print(key + ":True")
                else:
                    arr[i]["valid_part2_" + key] = False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.   

        if key == "hcl":

            val = arr[i][key]

            if val == None:
                arr[i]["valid_part2_" + key] = False
                continue

            if len(val) != 7:
                arr[i]["valid_part2_" + key] = False
                continue

            validNumList = list(range(0,10))
            validNumList = [str(i) for i in validNumList]
            validCharList = validNumList + ['a', 'b', 'c', 'd', 'e', 'f']
            
            sumValidChars = len(val)

            for k in range(len(val)):
                if k == 0 and val[k] != '#':
                    sumValidChars -= 1
                elif k > 0 and val[k] not in validCharList:
                    sumValidChars -= 1

            if sumValidChars == len(val):
                arr[i]["valid_part2_" + key] = True
                # print(key + ":True")
            else:
                arr[i]["valid_part2_" + key] = False

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.   

        if key == "ecl":

            val = arr[i][key]

            if val == None:
                arr[i]["valid_part2_" + key] = False
                continue

            validEyeColorList = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    
            if val in validEyeColorList:
                arr[i]["valid_part2_" + key] = True
                # print(key + ":True")
            else:
                arr[i]["valid_part2_" + key] = False

        # pid (Passport ID) - a nine-digit number, including leading zeroes.   

        if key == "pid":

            val = arr[i][key]

            if val == None:
                arr[i]["valid_part2_" + key] = False
                continue

            if len(val) != 9:
                arr[i]["valid_part2_" + key] = False
                continue

            validNumList = list(range(0,10))
            validNumList = [str(i) for i in validNumList]

            countDigits = 0
            for char in val:
                if char in validNumList:
                    countDigits += 1

            if countDigits == len(val):
                arr[i]["valid_part2_" + key] = True
                # print(key + ":True")
            else:
                arr[i]["valid_part2_" + key] = False

    # Ultimate count
    countValidValues = 0
    for key in sampleDict.keys():
        if arr[i]["valid_part2_" + key] == True:
            countValidValues += 1
    if countValidValues == len(sampleDict.keys()):
        arr[i]["valid_part2"] = True
        countValidPart2 += 1


print("Count Total People: %i" % len(arr))
print("Part 2: Valid Passports ---> %i" % countValidPart2)