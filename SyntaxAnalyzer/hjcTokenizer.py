from hjcTokens import *
from hjcOutputFile import *

class Tokenizer(object):

	def __init__(self, filename, outputFile, source):
		try:
			file = open(filename)
			self.tokens = self._getTokens(file.readlines())
			self.index = 0
			file.close()
		except:
			print("Error opening file " + filename)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.tokens):
			raise StopIteration
		token = self.tokens[self.index]
		self.index += 1
		return token

	def _getTokens(self, lines):
		tokens = []
		for line in lines:
			tokensInLine = line.split()
			for token in tokensInLine:
				tokens.append(token)
		return tokens

	def Advance(self):
		if self.index >= len(self.tokens):
			raise StopIteration
		self.token = self.tokens[self.index]
		self.index += 1
		return self.token

	def TokenType(self):
		if self.token in Keywords:
			return TK_KEYWORD
		elif self.token in Symbols:
			return TK_SYMBOL
		elif self.token[0] in Numbers:
			return TK_INT_CONST
		elif self.token[0] == '"':
			return TK_STRING_CONST
		else:
			return TK_IDENTIFIER

	def Keyword(self):
		return Keywords.index(self.token)

	def KeywordStr(self, keyword):
		if not keyword:
			return Keywords[self.token]
		else:
			return Keywords[keyword]

	def Symbol(self):
		return self.token

	def IntVal(self):
		return int(self.token)

	def StringVal(self):
		return self.token

	def Identifier(self):
		return self.token

