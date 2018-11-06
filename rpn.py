#!/usr/bin/env python3
from colored import fg, bg, attr

def calculate(arg):
	stack = []
	tokens = arg.split()

	for token in tokens:
		try:
			stack.append(int(token))
		except ValueError:
			val2 = stack.pop()
			val1 = stack.pop()
			if token == '+':
				result = val1 + val2
			elif token == '-':
				result = val1 - val2
			elif token == '*':
				result = val1 * val2
			elif token == '/':
				result = val1 / val2
			elif token == '^':
				result = val1**val2
			elif token == '%':
				result = val1 % val2;
			print(val1, end = " ")
			color = bg('indian_red_1a') + fg('white')
			reset = attr('reset')
			print(color + token + reset, end = " ")
			print(val2, end = " ")
			print("= ", end = " ")

			stack.append(result)

	if len(stack) > 1:
			raise ValueError('Too many arguments on the stack')

	return stack[0]

def main():
	while True:
		try:
			result = calculate(input('rpn calc> '))
			if result < 0 : 
				color = bg('indian_red_1a') + fg('white')
				reset = attr('reset')
				print(color + str(result) + reset)
			else:
				print(result)
		except ValueError:
			pass

if __name__ == '__main__':
	main()