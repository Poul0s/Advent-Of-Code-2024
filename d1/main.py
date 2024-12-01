

def load_input(part2):
	input = [
		[],
		[]
	]
	with open('input.txt') as f:
		for line in f:
			elems = line.split()
			if (not part2 or elems[0] not in input[0]):
				input[0].append(int(elems[0]))
			input[1].append(int(elems[1]))
	return input

def part1():
	input = load_input(False)
	res = 0
	for i in range(len(input[0])):
		min_left = min(input[0])
		min_right = min(input[1])
		input[0].remove(min_left)
		input[1].remove(min_right)
		res += max(min_left, min_right) - min(min_left, min_right)
	print(res)

def part2():
	input = load_input(True)
	res = 0
	for i in range(len(input[0])):
		elem = input[0][i]
		nb_occ = input[1].count(elem)
		res += elem * nb_occ
	print(res)

part1()
part2()