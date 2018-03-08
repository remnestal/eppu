
import re
import sys
import curses
import binascii

def binarystringtoascii(binstring):
	# Convert from string to int and then to the corresponding ascii
	byteregex = re.compile("[01]{8}")
	if (not byteregex.match(binstring)):
		raise ValueError("String does not match [01]{8}")

	return str(chr(int(binstring, base=2)))



def main():
	print(binarystringtoascii(sys.argv[1]))

if __name__ == "__main__":
    main()