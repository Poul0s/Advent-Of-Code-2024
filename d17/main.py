def get_combo(registers, number):
	if number >= 4:
		return registers[number - 4]
	return number 

def adv(registers, operand, ptr):
	registers[0] = int(registers[0] / (2 ** get_combo(registers, operand)))
	return 0

def blx(registers, operand, ptr):
	registers[1] = registers[1] ^ operand
	return 0

def bst(registers, operand, ptr):
	registers[1] = get_combo(registers, operand) % 8
	return 0

def jnz(registers, operand, ptr):
	if registers[0] != 0:
		return -ptr + operand - 2
	return 0

def bxc(registers, operand, ptr):
	registers[1] = registers[1] ^ registers[2]
	return 0

def out(registers, operand, ptr):
	print(get_combo(registers, operand) % 8, end=",")
	return 0

def bdv(registers, operand, ptr):
	registers[1] = int(registers[0] / (2 ** get_combo(registers, operand)))
	return 0

def cdv(registers, operand, ptr):
	registers[2] = int(registers[0] / (2 ** get_combo(registers, operand)))
	return 0


instructions = [
adv,
blx,
bst,
jnz,
bxc,
out,
bdv,
cdv,
]

def load_input():
	nbs = []
	registers = [0, 0, 0]
	with open("input.txt") as f:
		for i in range(3):
			registers[i] = int(f.readline()[12:])
		f.readline()
		nbs = [int(e) for e in f.readline()[9:].split(',')]
	return nbs, registers

def test_program(nbs, registers):
	ptr = 0
	while ptr < len(nbs):
		nb = nbs[ptr]
		operand = nbs[ptr + 1]
		ptr += instructions[nb](registers, operand, ptr) + 2


def part1():
	nbs, registers = load_input()
	test_program(nbs, registers)
	print()
	
def part2():
	nbs, registers = load_input()
	out_nbs = []

	def out(registers, operand, ptr):
		out_nbs.append(get_combo(registers, operand) % 8)
		return 0
	instructions[5] = out

	def resolve(nb=0, depth=0):
		for i in range(8):
			tmp = (nb << 3) | i
			registers[0] = tmp
			registers[1] = 0
			registers[2] = 0
			out_nbs.clear()
			test_program(nbs, registers)
			min_len = min(len(out_nbs), len(nbs))
			if len(out_nbs) == depth + 1 and out_nbs[-min_len:] == nbs[-min_len:]:
				if (depth == len(nbs)):
					return nb
				res = resolve(tmp, depth + 1)
				if (res):
					return res
		return 0
	print(resolve())


part1()
part2()