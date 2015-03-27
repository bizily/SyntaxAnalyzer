class OutputFile(object):

	def __init__(self, outputFileName):
		self.f = open(outputFileName, 'w')

	def Close(self):
		self.f.close()

	def Write(self, str):
		self.f.write(str)

	def WriteXml(self, tag, value):
		if tag == 'symbol':
			self.f.write("<symbol>")
		elif tag == 'keyword':
			self.f.write("<keyword>")
		elif tag == 'identifier':
			self.f.write("<identifier>")
