def load_input():
	input = []
	with open("input.txt") as f:
		for line in f:
			if line[len(line) - 1] == '\n':
				line = line[:len(line) - 1]
			input.append(line)
	return input

def start_hikingtrail(input, start, mult_path = False):
	pos_stack = [start]
	trail_ends = [] if mult_path else set()
	while (len(pos_stack) != 0):
		curr_pos = pos_stack.pop()
		if (input[curr_pos[1]][curr_pos[0]] == '9'):
			if mult_path:
				trail_ends.append(curr_pos)
			else:
				trail_ends.add(curr_pos)
		else:
			expect_chr = chr(ord(input[curr_pos[1]][curr_pos[0]]) + 1)

			if curr_pos[1] > 0 and input[curr_pos[1] - 1][curr_pos[0]] == expect_chr:
				pos_stack.append((curr_pos[0], curr_pos[1] - 1))

			if curr_pos[0] > 0 and input[curr_pos[1]][curr_pos[0] - 1] == expect_chr:
				pos_stack.append((curr_pos[0] - 1, curr_pos[1]))

			if curr_pos[1] < len(input) - 1 and input[curr_pos[1] + 1][curr_pos[0]] == expect_chr:
				pos_stack.append((curr_pos[0], curr_pos[1] + 1))

			if curr_pos[0] < len(input[0]) - 1 and input[curr_pos[1]][curr_pos[0] + 1] == expect_chr:
				pos_stack.append((curr_pos[0] + 1, curr_pos[1]))

	return len(trail_ends)

def part1():
	res = 0
	input = load_input()
	for y in range(len(input)):
		for x in range(len(input[y])):
			if input[y][x] == '0':
				res += start_hikingtrail(input, (x, y))
	print(res)

def part2():
	res = 0
	input = load_input()
	for y in range(len(input)):
		for x in range(len(input[y])):
			if input[y][x] == '0':
				res += start_hikingtrail(input, (x, y), True)
	print(res)

part1()
part2()