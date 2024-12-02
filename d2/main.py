

def load_input():
	input = []
	with open('input.txt') as f:
		for line in f:
			elems = line.split()
			input.append([int(elems[i]) for i in range(len(elems))])
	return input

def is_report_good(line):
	incr = line[1] > line[0]
	for i in range(1, len(line)):
		if (line[i] < line[i - 1] if incr else line[i] > line[i - 1]):
			return (False, i)
		diff = abs(line[i] - line[i - 1])
		if (diff == 0 or diff > 3):
			return (False, i)
	return (True, -1)


def part2():
	res = 0
	input = load_input()
	for line in input:
		good, bad_i = is_report_good(line)
		if (not good):
			good = is_report_good(line[:bad_i - 1] + line[bad_i:])[0]
		if (not good):
			good = is_report_good(line[:bad_i] + line[bad_i + 1:])[0]
		if (not good and bad_i + 1 < len(line)):
			good = is_report_good(line[:bad_i + 1] + line[bad_i + 2:])[0]
		res += good
	print(res)


def part1():
	res = 0
	input = load_input()
	for line in input:
		res += is_report_good(line)[0]
	print(res)


part1()
part2()