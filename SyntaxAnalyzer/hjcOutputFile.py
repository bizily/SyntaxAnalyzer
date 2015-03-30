class OutputFile(object):

	def __init__(self, outputFileName):
		self.f = open(outputFileName, 'w')

	def Close(self):
		self.f.close()

	def Write(self, str):
		self.f.write(str)

	def WriteXml(self, tag, value):
		if tag == 'keyword':
			self.f.write("<keyword> " + value + " </keyword>\n")

		# Replace HTML reserved symbols with character entities
		elif tag == 'symbol':
			if value == '<':
				self.f.write("<symbol> &lt; </symbol>\n")
			elif value == '>':
				self.f.write("<symbol> &gt; </symbol>\n")
			elif value == '&':
				self.f.write("<symbol> &amp; </symbol>\n")
			elif value == '"':
				self.f.write("<symbol> &quot; </symbol>\n")
			else:
				self.f.write("<symbol> " + value + " </symbol>\n")

		elif tag == 'integerConstant':
			self.f.write("<integerConstant> " + value + " </integerConstant>\n")

		elif tag == 'stringConstant':
			self.f.write("<stringConstant> " + value + " </stringConstant>\n")

		elif tag == 'identifier':
			self.f.write("<identifier> " + value + " </identifier>\n")
