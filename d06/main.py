import numpy as np

def load_input():
	map = {
		"pos": None,
		"obstacles": set(),
		"size": [0, 0],
		"direction": np.array([0, -1])

	}
	with open('input.txt') as f:
		for line in f:
			if (map["size"][0] == 0):
				map["size"][0] = len(line) - 1
			map["size"][1] += 1
			for i in range(len(line)):
				if line[i] == '^':
					map["pos"] = np.array([i, map["size"][1] - 1])
				elif line[i] == '#':
					map["obstacles"].add((i, map["size"][1] - 1))
	return map

def part1():
	map = load_input()
	visited_pos = set()
	while (map["pos"][0] >= 0 and map["pos"][0] < map["size"][0] and map["pos"][1] >= 0 and map["pos"][1] < map["size"][1]):
		visited_pos.add(tuple(map["pos"]))
		if (tuple(map["pos"] + map["direction"]) in map["obstacles"]):
			map["direction"][0], map["direction"][1] = -map["direction"][1], map["direction"][0]
		else:
			map["pos"] += map["direction"]
	print(len(visited_pos))

def has_loop(map):
	pos = map["pos"].copy()
	dir = map["direction"].copy()
	visited_pos = set()
	while (pos[0] >= 0 and pos[0] < map["size"][0] and pos[1] >= 0 and pos[1] < map["size"][1]):
		visited_pos.add(tuple(pos) + tuple(dir))
		if (tuple(pos + dir) in map["obstacles"]):
			dir[0], dir[1] = -dir[1], dir[0]
		else:
			pos += dir
			if ((tuple(pos) + tuple(dir)) in visited_pos):
				return True
	return False


def part2():
	map = load_input()
	loop_nb = 0
	for x in range(map["size"][0]):
		for y in range(map["size"][1]):
			if ((x, y) in map["obstacles"] or tuple(map["pos"]) == (x, y)):
				continue
			map["obstacles"].add((x, y))
			if has_loop(map):
				loop_nb += 1
			map["obstacles"].remove((x, y))
	print(loop_nb)

	# loop_pos_obs = set()
	# start_pos = map["pos"].copy()
	# while (map["pos"][0] >= 0 and map["pos"][0] < map["size"][0] and map["pos"][1] >= 0 and map["pos"][1] < map["size"][1]):
	# 	if (tuple(map["pos"] + map["direction"]) in map["obstacles"]):
	# 		map["direction"][0], map["direction"][1] = -map["direction"][1], map["direction"][0]
	# 	else:
	# 		new_pos = map["pos"] + map["direction"]
	# 		map["obstacles"].add(tuple(new_pos))
	# 		if (tuple(start_pos) != tuple(new_pos) and tuple(new_pos) not in loop_pos_obs and has_loop(map)):
	# 			loop_pos_obs.add(tuple(new_pos))
	# 		map["obstacles"].remove(tuple(new_pos))
	# 		map["pos"] = new_pos
	# print(len(loop_pos_obs))

part1()
part2()