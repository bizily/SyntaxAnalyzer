class OutputFile(object):

	def __init__(self, outputFileName):
		self.f = open(outputFileName, 'w')

	def Close(self):
		self.f.close()

	def Write(self, str):
		self.f.write(str)

	def WriteXml(self, tag, value):
		if tag == 'keyword':
			self.f.write("<keyword> " + value)
		elif tag == 'symbol':
			self.f.write("<symbol> " + value )
		elif tag == 'integerConstant':
			self.f.write("<integerConstant> " + value )
		elif tag == 'stringConstant':
			self.f.write("<stringConstant> " + value )
		elif tag == 'identifier':
			self.f.write("<identifier> " + value)
