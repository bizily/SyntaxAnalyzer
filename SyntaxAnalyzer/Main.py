import sys

from hjcCompile import *

def main():
	if len(sys.argv) == 1:
		print("Usage: Main.py input_file\n")
		return

	inputFilePath = sys.path[0] + sys.argv[1]

	compiler = CompileEngine(inputFilePath, 'MyProgramT.txt')

	'''
	compiler.CompileClass()
	'''

main()
