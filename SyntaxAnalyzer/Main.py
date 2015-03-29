import sys

from hjcCompile import *

def main(argv):
	if len(argv) == 1:
		print("Usage: Main.py <inputfile>")
		return

	inputFilePath = sys.path[0] + '\\' + argv[1]

	compiler = CompileEngine(inputFilePath, 'MyProgramT.txt')

	compiler.CompileClass()

if __name__ == "__main__":
	main(sys.argv)
