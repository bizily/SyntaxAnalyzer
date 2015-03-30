from hjcTokens import *
from hjcOutputFile import *

class Tokenizer(object):

	def __init__(self, filename, outputFile, source=False):
		try:
			# Open the given file
			file = open(filename)

			# Get the tokens from the file
			self.tokens = self._getTokens(file.readlines())
			self.index = 0

			# Close the file
			file.close()
		except:
			print("Error opening file " + filename)

	def _getTokens(self, lines):

		tokens = []

		# Remove comments from lines
		nclines = self._removeComments(lines)

		# For each line
		for line in nclines:

			# Get the tokens in the line using whitespace as the delimiter
			tokensInLine = line.split()

			processingComment = False
			processingStringConst = False
			subtoken = ''

			# For each token
			for token in tokensInLine:

				# For each character in the token, look for subtokens
				for char in token:

					# If currently processing a string constant
					if processingStringConst:

						# If found the end, 
						if char == '"':
							subtoken += char
							processingStringConst = False

						# Else continue building the string constant
						else:
							subtoken += char

					# Else if found the beginning of a string constant
					elif char == '"':

						# Save the current subtoken
						if subtoken:
							tokens.append(subtoken)
							subtoken = ''

						# Start building a string constant subtoken
						subtoken += char
						processingStringConst = True

					# Else if found a symbol
					elif char in Symbols:

						# Save the current subtoken
						if subtoken:
							tokens.append(subtoken)
							subtoken = ''

						# Save the symbol token
						tokens.append(char)

					# Else continue building the subtoken
					else:
						subtoken += char

				# If processing a string constant, put the space back
				if processingStringConst:
					subtoken += ' '

				# Else save the subtoken
				elif subtoken:
					tokens.append(subtoken)
					subtoken = ''

		return tokens

	def _removeComments(self, lines):
		nclines = []
		state = 0

		# For each line
		for line in lines:
			ncline = ""

			for char in line:
				# state 0: initial state
				if state == 0:
					if char == '/':
						state = 1
					elif char == '*':
						ncline += char
					else:
						ncline += char

				# state 1: '/'
				elif state == 1:
					if char == '/':
						state = 0
						break
					elif char == '*':
						state = 2
					else:
						ncline += '/' + char
						state = 0

				# state 2: '/*'
				elif state == 2:
					if char == '/':
						state = 1
					elif char == '*':
						state = 3
					else:
						state = 2

				# state 3: '/**'
				else:
					if char == '/':
						state = 0
					elif char == '*':
						state = 3
					else:
						state = 2

			if ncline:
				nclines.append(ncline)

		return nclines

	def __iter__(self):
		return self

	def __next__(self):
		# If no more tokens
		if self.index >= len(self.tokens):
			raise StopIteration

		# Get the token and advance the index
		self.token = self.tokens[self.index]
		self.index += 1
		return self.token

	def Advance(self):
		# If no more tokens
		if self.index >= len(self.tokens):
			return None

		# Get the token and advance the index
		self.token = self.tokens[self.index]
		self.index += 1

		return self.token

	def TokenType(self):
		# If token is a keyword
		if self.token in Keywords:
			return TK_KEYWORD

		# If token is a symbol, but not a quote
		elif self.token in Symbols:
			return TK_SYMBOL

		# If token is a number
		elif self.token[0] in Numbers:
			return TK_INT_CONST

		# If token begins with a quote
		elif self.token[0] == '"':
			return TK_STRING_CONST

		# It must be an identifier
		else:
			return TK_IDENTIFIER

	def Keyword(self):
		return Keywords.index(self.token)

	def KeywordStr(self, keyword=None):
		if not keyword:
			return self.token
		else:
			return Keywords[keyword]

	def Symbol(self):
		return self.token

	def IntVal(self):
		return int(self.token)

	def StringVal(self):
		# Return the string constant with quotes removed
		return self.token.replace('"', '')

	def Identifier(self):
		return self.token
