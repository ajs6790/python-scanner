#Alex Sylvester			alexjsyl@louisiana.edu
#ajs6790
#cmps 450G


import sys

INT_LIT = 10
IDENT = 11

LETTER = 0
def letter(charClass):
	addChar(lexeme, nextChar)
	getChar()
	while charClass == LETTER or charClass == DIGIT:
		addChar(lexeme, nextChar)
		charClass = getChar()
	nextToken = IDENT

DIGIT = 1
def digit(charClass):
	addChar()
	getChar()
	while charClass == DIGIT:
		addChar()
		getChar()
	nextToken = INT_LIT

UNKNOWN = 99
def unknown(charClass):
	lookup(nextChar)
	getChar()

def addChar(lexeme, nextChar):
	#global lexeme
	#global nextChar
	lexeme += nextChar

def ADD_OP():
	addChar()
	nextToken = 21

def SUB_OP():
	addchar()
	nextToken = 22

def MULT_OP():
	addChar()
	nextToken = 23

def DIV_OP():
	addChar()
	nextToken = 24

def LEFT_PAREN():
	addChar()
	nextToken = 25

def RIGHT_PAREN():
	addChar()
	nextToken = 26

def EOF():
	addChar()
	#global nextToken
	nextToken = -1

def eof():
	#global nexToken
	nextToken = -1
	lexeme = "EOF"

def getChar():
	nextChar = in_fp.read(1)
	if nextChar is None:
		charClass = -1
	elif nextChar.isalpha():
		charClass = LETTER
	elif nextChar.isdigit():
		charClass = DIGIT
	else:
		charClass = UNKNOWN
		
	return charClass

def getNonBlank():
	#global nextChar
	#nextChar = ''
	while nextChar == ' ':
		getChar()


def lookup(ch):
	if ch == '(':
		LEFT_PAREN()
	elif ch == ')':
		RIGHT_PAREN()
	elif ch == '+':
		ADD_OP()
	elif ch == '-':
		DIV_OP()
	elif ch == '*':
		MULT_OP()
	elif ch == '/':
		DIV_OP()
	else:
		EOF()

	#return{
	#	'(': LEFT_PAREN,
	#	')': RIGHT_PAREN,
	#	'+': ADD_OP,
	#	'-': SUB_OP,
	#	'*': MULT_OP,
	#	'/': DIV_OP,
	#	')': RIGHT_PAREN,
	#	}.get(ch,EOF)

def foo(num):
	if num == LETTER:
		letter(num)
	elif num == DIGIT:
		digit(num)	
	elif num == UNKNOWN:
		unknown(num)
	else:
		eof()

	#return{
	#	LETTER: letter,
	#	DIGIT: digit,
	#	UNKNOWN: unknown,
	#	-1: eof,
	#}[num]		

def lex():
	getNonBlank()
	foo(charClass)
	print('Next Token is: ', nextToken, 'Next lexeme is: ', lexeme)
	return nextToken


if __name__ == '__main__':
	global charClass
	charClass = 0
	global lexeme
	lexeme = ""
	global nextChar
	nextChar = ''
	global nextToken
	nextToken = 0

	global in_fp
	parse = 0
	try:
		if len(sys.argv)==2:
			in_fp = open(sys.argv[1], 'r') #catch
			parse = 1
		elif len(sys.argv) == 1:
			in_fp = open('front.in','r')
			parse = 1
		else:
			print ('Usage in python front.py [file-to-parse (optimal, default = front.in)]')

	except IOError:
		if len(sys.argv)==2:
			print ('file not found', sys.argv[1])
		else:
			print ('file not found: front.in')
	
	except:
		print('Expected error: ', sys.exc_info()[0])
		raise
	
	if parse:
		getChar()
		lex()
		while nextToken != -1:
			lex()
		in_fp.close()



















