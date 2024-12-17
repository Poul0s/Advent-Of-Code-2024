from numpy import array
from copy import deepcopy

def load_input():
	map = {
		"content": [],
		"robot": None,
		"moves": ""
	}

	with open("input.txt") as f:
		line = f.readline()
		while line != "\n":
			map_line = ""
			x = 0
			while line[x] != '\n':
				if line[x] == 'O':
					map_line += '[]'
				elif line[x] == '#':
					map_line += '##'
				else:
					if line[x] == '@':
						map["robot"] = array([x * 2, len(map["content"])])
					map_line += '..'
				x += 1
			map["content"].append(list(map_line))
			line = f.readline()
		line = f.readline()
		while len(line) != 0:
			if line[len(line) - 1] == '\n':
				line = line[:len(line) - 1]
			map["moves"] += line
			line = f.readline()
	return map

def move_box(map, positions, move):
	vertical_move = move[1] != 0

	if not vertical_move and (positions[0][0] < positions[1][0]) == (move[0] > 0):
		positions[0], positions[1] = positions[1], positions[0]

	for pos in positions:
		new_pos = pos + move
		if map["content"][new_pos[1]][new_pos[0]] == '#':
			return False
		elif map["content"][new_pos[1]][new_pos[0]] != '.':
			pass
			box = [new_pos.copy(), new_pos + [-1 + 2 * (map["content"][new_pos[1]][new_pos[0]] == '['), 0]]
			if not move_box(map, box, move):
				return False
		map["content"][new_pos[1]][new_pos[0]] = map["content"][pos[1]][pos[0]]
		map["content"][pos[1]][pos[0]] = '.'
	return True

def move_robot(map, move):
	new_pos = map["robot"] + move
	if map["content"][new_pos[1]][new_pos[0]] == '#':
		return False
	elif map["content"][new_pos[1]][new_pos[0]] != '.':
		box = [new_pos.copy(), new_pos + [-1 + 2 * (map["content"][new_pos[1]][new_pos[0]] == '['), 0]]
		old_content = deepcopy(map["content"])
		if move_box(map, box, move) == False:
			map["content"] = old_content
			return False
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
for y in range(len(map["content"])):
	for x in range(len(map["content"][0])):
		if map["content"][y][x] == '[':
			sum += y * 100 + x
print(sum)