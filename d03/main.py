import re

def load_input():
	input = ""
	with open('input.txt') as f:
		input = f.read()
	return input

def part1(input):
	res = 0
	reg = "mul\(\d{1,3},\d{1,3}\)"
	instructions = re.findall(reg, input)
	for op in instructions:
		op = op.split(',')
		a = op[0][4:]
		b = op[1][:-1]
		res += int(a) * int(b)
	print(res)

def part2(input: str):
	new_input = ""
	do = True
	while len(input) > 0:
		if do:
			stop_idx = input.find("don't()")
			if (stop_idx == -1):
				stop_idx = len(input) - 1
			else:
				stop_idx += len("don't()")
			new_input += input[:stop_idx]
			input = input[stop_idx + 7:]
		else:
			stop_idx = input.find("do()")
			if (stop_idx == -1):
				input = ""
			else:
				input = input[stop_idx + 4:]
		do = not do
	part1(new_input)

input = load_input()
part1(input)
part2(input)

