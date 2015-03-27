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
		if self.token in '+-*/&|<>=':
			return TK_SYMBOL
		elif self.token in ('class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this','let', 'do', 'if', 'else', 'while', 'return'):
			return TK_KEYWORD
		else:
			return NULL

'''
	def Keyword(self):

	def KeywordStr(self):

	def Identifier(self):

	def Symbol(self):
'''
