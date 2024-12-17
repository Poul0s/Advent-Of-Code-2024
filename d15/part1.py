from numpy import array

def load_input():
	map = {
		"size": [0, 0],
		"walls": set(),
		"boxes": set(),
		"robot": None,
		"moves": ""
	}

	with open("input.txt") as f:
		line = f.readline()
		map["size"][0] = len(line) - 1
		while line != "\n":
			map["size"][1] += 1
			x = 0
			y = map["size"][1] - 1
			while line[x] != '\n':
				if line[x] == 'O':
					map["boxes"].add((x, y))
				elif line[x] == '#':
					map["walls"].add((x, y))
				elif line[x] == '@':
					map["robot"] = array([x, y])
				x += 1
			line = f.readline()
		line = f.readline()
		while len(line) != 0:
			if line[len(line) - 1] == '\n':
				line = line[:len(line) - 1]
			map["moves"] += line
			line = f.readline()
	return map

def move_robot(map, move):
	new_pos = map["robot"] + move
	empty_pos = new_pos.copy()
	while tuple(empty_pos) not in map["walls"] and tuple(empty_pos) in map["boxes"]:
		empty_pos += move

	if tuple(empty_pos) not in map["walls"]:
		if not (empty_pos == new_pos).all():
			map["boxes"].remove(tuple(new_pos))
			map["boxes"].add(tuple(empty_pos))
		map["robot"] = new_pos


map = load_input()
for move in map["moves"]:
	if move == '^':
		move_robot(map, array((0, -1)))
	if move == 'v':
		move_robot(map, array((0, 1)))
	if move == '<':
		move_robot(map, array((-1, 0)))
	if move == '>':
		move_robot(map, array((1, 0)))
sum = 0
for boxe in map["boxes"]:
	sum += boxe[0] + boxe[1] * 100
print(sum)