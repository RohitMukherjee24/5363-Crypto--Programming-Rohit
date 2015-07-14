###############################################
# Name: (Rohit Mukherjee)
# Class: CMPS 5363 Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
###############################################
import pprint
import re

class StringManip:
	"""
	Helper class to speed up simple string manipulation
	"""

	def generateAlphabet(self):
		#Create empty alphabet string
		alphabet = ""

		#Generate the alphabet
		for i in range(0,26):
			alphabet = alphabet + chr(i+65)

		return alphabet


	def cleanString(self,s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'_','spLetters':'X','alphanum':1}):
		"""
		Cleans message by doing the following:
		- up            - uppercase letters
		- spLetters     - split double letters with some char
		- reSpaces      - replace spaces with some char or '' for removing spaces
		- reNonAlphaNum - remove non alpha numeric
		- reDupes       - remove duplicate letters
		@param   string -- the message
		@returns string -- cleaned message
		"""
		if 'up' in options:
			s = s.upper()

		if 'reSpaces' in options:
			space = options['reSpaces']
			s = re.sub(r'[\s]', space, s)

		if 'reNonAlphaNum' in options:
			s = re.sub(r'[^\w]', '', s)

		if 'spLetters' in options:
			#replace 2 occurences of same letter with letter and 'X'
			s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)
		
		if 'reDupes' in options:
			s= ''.join(sorted(set(s), key=s.index))
		
		if 'alphanum' in options:
			s = re.sub(r'[^A-Za-z]', '', s)
		
		return s


class PlayFair:
	"""
	Class to encrypt via the PlayFair cipher method
	Methods:
	- generateSquare
	- transposeSquare
	-
	"""

	def __init__(self,key,message):
		self.Key = key
		self.Message = message
		self.Square = []
		self.Transposed = []
		self.StrMan = StringManip()
		self.Alphabet = ""
		
		self.generateSquare()
		self.transposeSquare()

	def generateSquare(self):
		"""
		Generates a play fair square with a given keyword.
		@param   string   -- the keyword
		@returns nxn list -- 5x5 matrix
		"""
		row = 0     #row index for sqaure
		col = 0     #col index for square

		#Create empty 5x5 matrix
		self.Square = [[0 for i in range(5)] for i in range(5)]

		self.Alphabet = self.StrMan.generateAlphabet()

		#uppercase key (it meay be read from stdin, so we need to be sure)
		self.Key = self.StrMan.cleanString(self.Key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1,'alphanum':1})

		#Load keyword into square
		for i in range(len(self.Key)):
			self.Square[row][col] = self.Key[i]
			self.Alphabet = self.Alphabet.replace(self.Key[i], "")
			col = col + 1
			if col >= 5:
				col = 0
				row = row + 1

		#Remove "J" from alphabet
		self.Alphabet = self.Alphabet.replace("J", "")

		#Load up remainder of playFair matrix with
		#remaining letters
		for i in range(len(self.Alphabet)):
			self.Square[row][col] = self.Alphabet[i]
			col = col + 1
			if col >= 5:
				col = 0
				row = row + 1

	def transposeSquare(self):
		"""
		Turns columns into rows of a cipher square
		@param   list2D -- playFair square
		@returns list2D -- square thats transposed
		"""
		#Create empty 5x5 matrix
		self.Transposed = [[0 for i in range(5)] for i in range(5)]

		for col in range(5):
			for row in range(5):
			   self.Transposed[col][row] = self.Square[row][col]


	def getCodedDigraph(self,digraph):
		"""
		Turns a given digraph into its encoded digraph whether its on
		the same row, col, or a square
		@param   list -- digraph
		@returns list -- encoded digraph
		"""
		newDigraph = ['','']
		#Check to see if digraph is in same row
		for row in self.Square:
			if digraph[0] in row and digraph[1] in row:
				newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
				newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
				return newDigraph

		#Check to see if digraph is in same column
		for row in self.Transposed:
			if digraph[0] in row and digraph[1] in row:
				newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
				newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
				return newDigraph


		#Digraph is in neither row nor column, so it's a square
		location1 = self.getLocation(digraph[0])
		location2 = self.getLocation(digraph[1])

		#print(location1)
		#print(location2)

		#print(self.Square[location1[0]][location2[1]])
		#print(self.Square[location2[0]][location1[1]])

		return [self.Square[location1[0]][location2[1]],self.Square[location2[0]][location1[1]]]

	def getDecoded(self,digraph):
		"""
		Turns a given digraph into its DECODED digraph whether its on
		the same row, col, or a square
		@param   list -- digraph
		@returns list -- DECODED digraph
		here  handled the array index 0 which is hard coded as points to array index 4.
		"""
		newDigraph = ['','']

		#check if the digraph has any negative values avoid it by hardcoding with index 4
		#otherwise proceed by moving left.
		for row in self.Square:
			if digraph[0] in row and digraph[1] in row:
				if (row.index(digraph[0])-1 < 0):
					newDigraph[0] = row[4]
				else :
					newDigraph[0] = row[row.index(digraph[0])-1]
				if (row.index(digraph[1])-1 < 0):
					newDigraph[1] = row[4]
				else :
					newDigraph[1] = row[row.index(digraph[1])-1]
				return newDigraph 

		#check if the digraph has any negative values avoid it by hardcoding with index 4
		#otherwise proceed by moving left
		for row in self.Transposed:
			if digraph[0] in row and digraph[1] in row:
				if (row.index(digraph[0])-1 < 0):
					newDigraph[0] = row[4]
				else :
					newDigraph[0] = row[row.index(digraph[0])-1]
				if (row.index(digraph[1])-1 < 0):
					newDigraph[1] = row[4]
				else :
					newDigraph[1] = row[row.index(digraph[1])-1]
				return newDigraph


		#Digraph is in neither row nor column, so it's a square
		location1 = self.getLocation(digraph[0])
		location2 = self.getLocation(digraph[1])

		#print(location1)
		#print(location2)

		#print(self.Square[location1[0]][location2[1]])
		#print(self.Square[location2[0]][location1[1]])

		return [self.Square[location1[0]][location2[1]],self.Square[location2[0]][location1[1]]]
	
	
	
	
	def getLocation(self,letter):
		row = 0
		col = 0

		count = 0
		for list in self.Square:
			if letter in list:
				row = count
			count += 1

		count = 0
		for list in self.Transposed:
			if letter in list:
				col = count
			count += 1
		return [row,col]

	#############################################
	# Helper methods just to see whats going on
	#############################################
	def printNewKey(self):
		print(self.Key)

	def printNewMessage(self):
		print(self.Message)

	def printSquare(self):
		for list in self.Square:
			print(list)
		print('')

	def printTransposedSquare(self):
		for list in self.Transposed:
			print(list)
		print('')

###########################################################################
"""
This block Handles the output console screen and asks for inputs.Here we implemented three user input options
to they are encipher which encodes the given plain text Decipher which Decodes the encripted text and exit option.
In the encoding block asked for message and key and then we cleaned the message and key by removing extra chracters,
spacses etc.chekcked if the lenght of the message is odd, if odd then append X at the end of message.using he while
loop we had called getcodeddigraph which is appended with 2 charactes each in the message.In the decoding block we had
used the method get decoded.
"""
if __name__ == "__main__":
	print("\nPlayfair Encryption Tool (P.E.T)\n  Written By: (Rohit Mukherjee)")
	print("*****************************")
	print("1. Encipher\n2. Decipher\n3. Quit\n")
	print("*****************************")
	#input variable inputval
	inputval = input("Enter your choise:\n" )
if(inputval == '1'):
	print("\nPlayfair Encryption Tool (P.E.T)\n  Written By: (Rohit Mukherjee)")
	print("*****************************")
	message = input("Please enter a message:\n ")
	print("*****************************")
	print("\n")
	print("\nPlayfair Encryption Tool (P.E.T)\n  Written By: (Rohit Mukherjee)")
	print("*****************************")
	key = input("Please enter a keyword:\n ")
	print("*****************************")
	myCipher = PlayFair(key,message)
	#cleaning Message 
	myCipher.Message = myCipher.StrMan.cleanString(myCipher.Message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'spLetters':'1','alphanum':1})
	#if Message is odd then append X to the message
	if len(myCipher.Message)%2==1:
		myCipher.Message += 'X'
	i= 0
	Text1 = ""
	Temp1 = ""
	# using getcodedDigraph we passing the message coordinate 2 alphabets at a time and looping it we cover the all the alphabets.
	while i < (len(myCipher.Message)-1):
		Temp1 = myCipher.getCodedDigraph([myCipher.Message[i],myCipher.Message[i+1]])
		Text1 =  Text1 + Temp1[0] + Temp1[1]
		i += 2
	print("\nPlayfair Encryption Tool (P.E.T)\n  Written By: (Rohit Mukherjee)")
	print("*****************************")
	print('Your encrypted message is:\n' + Text1)
	print("*****************************")
elif(inputval == "2"):
	print("\nPlayfair Encryption Tool (P.E.T)\n  Written By: (Rohit Mukherjee)")
	print("*****************************")
	message = input("Please enter a message:\n ")
	print("*****************************")
	print("\nPlayfair Encryption Tool (P.E.T)\n  Written By: (Rohit Mukherjee)")
	print("*****************************")
	key = input("Please enter a keyword:\n " )
	print("*****************************")
	myCipher = PlayFair(key,message)
	myCipher.Message = myCipher.StrMan.cleanString(myCipher.Message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'alphanum':1})
	Text1 = ""
	Temp1 = ""
	i = 0
	while i < (len(myCipher.Message)-1):
		Temp1 = myCipher.getDecoded([myCipher.Message[i],myCipher.Message[i+1]])
		Text1 = Text1 + Temp1[0] + Temp1[1]
		i += 2
	# used this for removing last letter X but if X is real message then its messedup,
	# cant able to figure out how to check X is real or not
	if len(Text1) % 2==0 and Text1.endswith('X'):
		Text1 = Text1[:-1]
	print("\nPlayfair Encryption Tool (P.E.T)\n  Written By: (Rohit Mukherjee)")
	print("*****************************")
	print('Your decrypted message is:\n' + Text1)
	print("*****************************")
elif(inputval == "3"):
	exit()