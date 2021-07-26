
MASK_TEXT = "mask = "
TWOS = [2**x for x in range(36)]

class AOC_DAY14:

	def __init__(self, filename):
		self.filename = filename	
		self.data = {}
		self.maskedData = {}
		self.readFile()

	def isMaskLine(self, str):
		return str[:len(MASK_TEXT)] == MASK_TEXT

	def getBitMask(self, str):
		return str[len(MASK_TEXT):][::-1] ## need to reverse, doing everything LHS bit least significant

	def setBitmaskMemoryValues(self, values, bitmask):
		memdict = {}
		for val in values:
			currkey = val.split("]")[0][len("mem["):]
			currval = int(val.split("] = ")[1])
			memdict[currkey] = currval
		self.data[bitmask] = memdict

	def fillData(self, fileLines):
		i = 0
		while i < len(fileLines): 
			if self.isMaskLine(fileLines[i]):
				bitmask = self.getBitMask(fileLines[i])
				i += 1
				memspaces = []
				while i < len(fileLines) and not self.isMaskLine(fileLines[i]):
					memspaces.append(fileLines[i])
					i += 1
				self.setBitmaskMemoryValues(memspaces, bitmask)

	def readFile(self):
		with open(self.filename, "r") as f:
			self.fillData([line.strip("\n") for line in f.readlines()])
			f.close()

	def memorySpaceInfo(self):
		allkeys = []
		for key in self.data.keys():
  			print("\n")
  			print(key)
  			print(self.data[key])
  			keys = [int(k) for k in list(self.data[key].keys())]
  			allkeys.extend(keys)

		print("\n-------- Unique Key Info ------ \n")
		print("Number of Total Keys: " + str(len(allkeys)))
		allkeys.sort()
		print("\nAll Keys in Order: ")
		print(allkeys)
		print("\nDuplicates: ")
		dupes = list(set([x for x in allkeys if allkeys.count(x) > 1]))
		print(dupes)

	def get36BitRepr(self, int):
		bits = [0 for x in range(len(TWOS))]
		val = int
		while val > 1:
			position = sum([x - val <= 0 for x in TWOS]) - 1
			twosvalue = TWOS[position]
			bits[position] = 1
			val -= twosvalue
		bits[0] = 1 if val == 1 else 0
		#print("Number: " + str(int) + ", bits: " + ''.join([str(i) for i in bits]))
		return bits

	def getIntRepr(self, bitrepr36):
		multList = [int(TWOS[i]) * int(bitrepr36[i]) for i in range(len(bitrepr36))]
		return sum(multList)

	def getSingleBitRepr(self, currbit, singlebitmask):
		if singlebitmask == "X":
			return currbit
		elif singlebitmask == "1":
			return 1
		elif singlebitmask == "0":
			return 0

	def getMaskedRepr(self, currbits, bitmask):
		newbits = [0 for x in range(len(currbits))]
		bitmasklist = list(bitmask)
		for i in range(len(bitmasklist)):
			newbits[i] = self.getSingleBitRepr(currbits[i], bitmasklist[i])
		return newbits

	def maskAllDataPart1(self):
		for bitmask in self.data.keys():
			for memspace in self.data[bitmask].keys():
				currbits = self.get36BitRepr(self.data[bitmask][memspace])
				self.maskedData[memspace] = self.getMaskedRepr(currbits, bitmask)

	def getSumMaskedValuesPart1(self):
		sum = 0
		for val in self.maskedData.values():
			sum += self.getIntRepr(val)
		print("\n\nPart1: Sum of remaining values in memory after data is processed: " + str(sum) + "\n\n")

	def getPart1Answer(self):
		self.maskAllDataPart1()
		self.getSumMaskedValuesPart1()


	def getSingleBitReprMemory(self, currbit, singlebitmask):
		if singlebitmask == "0":
			return currbit
		elif singlebitmask == "1":
			return 1
		elif singlebitmask == "X":
			return 'X'

	def getBinaryPermutations(self, num_digits):
		binaryDict = {}
		counter = 1
		while counter <= num_digits:
			if counter == 1:
				binaryDict[str(counter)] = ['0','1']
			else:
				end_zero = [val + '0' for val in binaryDict[str(counter-1)]] 
				end_one = [val + '1' for val in binaryDict[str(counter-1)]]
				binaryDict[str(counter)] = end_zero + end_one
			counter += 1
		return binaryDict[str(num_digits)]


	def maskAllDataPart2(self):

		allAddresses = []
		
		self.memoryDictPart2 = {}

		for bitmask in list(self.data.keys()):
			for memspace in self.data[bitmask].keys():

				#0) Get value associated with memory space
				value = int(self.data[bitmask][memspace])

				# 1) get bit representation of memory space
				bits = self.get36BitRepr(int(memspace))

				# 2) Mask bits
				maskedbits = [self.getSingleBitReprMemory(bits[i], bitmask[i]) for i in range(len(bitmask))]
				x_positions = [i for i in range(len(maskedbits)) if maskedbits[i] == 'X']

				#3) Find all combinations of addresses based on # of X's
				x_replacements = self.getBinaryPermutations(maskedbits.count("X"))
				
				#4) Create list of new addresses 
				newAddresses = []
				for repl in x_replacements:
					repl = list(repl)
					newaddr = list(maskedbits)
					newaddr
					for i in range(len(repl)):
						newaddr[x_positions[i]] = repl[i]
					newaddrstr = ''
					for char in newaddr:
						newaddrstr += str(char)
					newAddresses.append(newaddrstr)

				#5) For each address, set the memory value to be the current memory value
				for addr in newAddresses:
					self.memoryDictPart2[addr] = value

	def getPart2Answer(self):
		self.maskAllDataPart2()

		all_values = self.memoryDictPart2.values()
		print("Part2: Sum of remaining values in memory after data is processed: %d\n\n" % sum(all_values))

				
# ---------------------------- Answers

solution = AOC_DAY14("aoc_2020_day14_input1.txt")
solution.getPart1Answer()
solution.getPart2Answer()