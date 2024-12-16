def load_input():
	machines = []
	def get_btn(line):
		x, y = line.split(',')
		x = int(x[12:])
		y = int(y[3:])
		return (x, y)
	
	with open("input.txt") as f:
		line = f.readline()
		while len(line) > 0:
			if line != "\n":
				btn1 = get_btn(line)
				btn2 = get_btn(f.readline())
				prize = f.readline().split(',')
				prize = int(prize[0][9:]), int(prize[1][3:])
				machines.append((btn1, btn2, prize))
			line = f.readline()
	return machines

def part1():
	machines = load_input()
	total = 0
	for machine in machines:
		btn1 = machine[0]
		btn2 = machine[1]
		p = machine[2]
		a = ((p[1] * btn2[0]) - (p[0] * btn2[1])) / ((btn1[1] * btn2[0]) - (btn1[0] * btn2[1]))
		b = (-btn1[0] * a + p[0]) / btn2[0]
		if int(a) != a or int(b) != b or a < 0 or b < 0:
			continue
		cost = a * 3 + b
		total += cost
	print(total)


def part2():
	machines = load_input()
	total = 0
	for machine in machines:
		btn1 = machine[0]
		btn2 = machine[1]
		p = (machine[2][0] + 10000000000000, machine[2][1] + 10000000000000)
		a = ((p[1] * btn2[0]) - (p[0] * btn2[1])) / ((btn1[1] * btn2[0]) - (btn1[0] * btn2[1]))
		b = (-btn1[0] * a + p[0]) / btn2[0]
		if int(a) != a or int(b) != b or a < 0 or b < 0:
			continue
		cost = a * 3 + b
		total += cost
	print(total)

part1()
part2()