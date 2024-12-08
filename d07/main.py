def load_input():
	input = []
	with open("input.txt") as f:
		for line in f:
			res, nbs = line.split(':')
			input.append([int(res)] + [int(nb) for nb in nbs[1:].split(' ')])
	return input

def make_op(nbs, ops):
	res = nbs[0]
	for i in range(1, len(nbs)):
		if ops[i - 1] == '+':
			res += nbs[i]
		elif ops[i - 1] == '*':
			res *= nbs[i]
		else:
			res = int(str(res) + str(nbs[i]))
	return res


def part1():
	input = load_input()
	res = 0
	for eq in input:
		nbs = eq[1:]
		if (make_op(nbs, '+' * (len(eq) - 2)) == eq[0]):
			res += eq[0]
		else:
			def bt(ops, nb_op):
				if nb_op == 0:
					return make_op(nbs, ops) == eq[0]
				else:
					nb_op -= 1
					ops.append('+')
					if (bt(ops, nb_op)):
						return True
					ops.pop()
					ops.append('*')
					if (bt(ops, nb_op)):
						return True
					ops.pop()
			if (bt([], len(eq) - 2)):
				res += eq[0]
	print(res)



def part2():
	input = load_input()
	res = 0
	for eq in input:
		nbs = eq[1:]
		if (make_op(nbs, '+' * (len(eq) - 2)) == eq[0]):
			res += eq[0]
		else:
			def bt(ops, nb_op):
				if nb_op == 0:
					return make_op(nbs, ops) == eq[0]
				else:
					nb_op -= 1
					ops.append('+')
					if (bt(ops, nb_op)):
						return True
					ops.pop()
					ops.append('*')
					if (bt(ops, nb_op)):
						return True
					ops.pop()
					ops.append('|')
					if (bt(ops, nb_op)):
						return True
					ops.pop()
			if (bt([], len(eq) - 2)):
				res += eq[0]
	print(res)

part1()
part2()