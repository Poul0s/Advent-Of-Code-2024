def load_input():
	input = []
	with open("input.txt") as f:
		for line in f:
			if line[len(line) - 1] == '\n':
				line = line[:len(line) - 1]
			input.append(line)

	def propagate_plot(plot):
		stack = [plot[0]]
		def add_pos(pos):
			if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(input[0]) or pos[1] >= len(input) \
				or pos in plot \
				or input[pos[1]][pos[0]] != input[plot[0][1]][plot[0][0]]:
				return
			plot.append(pos)
			stack.append(pos)

		while (len(stack) > 0):
			curr_pos = stack.pop()
			add_pos((curr_pos[0] - 1, curr_pos[1]))
			add_pos((curr_pos[0] + 1, curr_pos[1]))
			add_pos((curr_pos[0], curr_pos[1] - 1))
			add_pos((curr_pos[0], curr_pos[1] + 1))
			

	garden = []
	for y in range(len(input)):
		for x in range(len(input[y])):
			already_in = False
			for plot in garden:
				if (x, y) in plot:
					already_in = True
					break
			if not already_in:
				plot = [(x, y)]
				propagate_plot(plot)
				garden.append(plot)
	return garden

def get_perimeter(plot):
	perimeter = 0
	for pos in plot:
		if (pos[0] - 1, pos[1]) not in plot:
			perimeter += 1
		if (pos[0] + 1, pos[1]) not in plot:
			perimeter += 1
		if (pos[0], pos[1] - 1) not in plot:
			perimeter += 1
		if (pos[0], pos[1] + 1) not in plot:
			perimeter += 1
	return perimeter

def get_sides(plot):
	# perim_end = []
	# for pos in plot:
	# 	if (pos[0] - 1, pos[1]) not in plot:
	# 		perim_end.append((pos[0] - 1, pos[1]))
	# 	if (pos[0] + 1, pos[1]) not in plot:
	# 		perim_end.append((pos[0] + 1, pos[1]))
	# 	if (pos[0], pos[1] - 1) not in plot:
	# 		perim_end.append((pos[0], pos[1] - 1))
	# 	if (pos[0], pos[1] + 1) not in plot:
	# 		perim_end.append((pos[0], pos[1] + 1))
	
	# sides = 0
	# while len(perim_end):
	# 	sides += 1
	# 	stack = [perim_end.pop()]
	# 	while len(stack):
	# 		pos = stack.pop()
	# 		if 

	# return len(sides)

	sides = []
	for pos in plot:
		for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
			if (pos[0] + dir[0], pos[1] + dir[1]) not in plot:
				sides.append((pos[0] + dir[0], pos[1] + dir[1], dir))

	i = 0
	while (i < len(sides)):
		side = sides[i]
		dir = (side[2][1], side[2][0])
		pad = 1
		found_l = 1
		found_r = 1
		while found_l == pad or found_r == pad:
			if found_l == pad and (side[0] + dir[0] * pad, side[1] + dir[1] * pad, side[2]) in sides:
				found_l += 1
				sides.remove((side[0] + dir[0] * pad, side[1] + dir[1] * pad, side[2]))
			if found_r == pad and (side[0] - dir[0] * pad, side[1] - dir[1] * pad, side[2]) in sides:
				found_r += 1
				sides.remove((side[0] - dir[0] * pad, side[1] - dir[1] * pad, side[2]))
			pad += 1
		i += 1
	return len(sides)


def part1():
	garden = load_input()
	res = 0
	for plot in garden:
		res += len(plot) * get_perimeter(plot)
	print(res)

def part2():
	garden = load_input()
	res = 0
	for plot in garden:
		res += len(plot) * get_sides(plot)
	print(res)

part1()
part2()


