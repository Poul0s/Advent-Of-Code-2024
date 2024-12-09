from numpy import array

def load_input():
	map = {
		"size": [0, 0],
		"antennas": {},
	}

	with open("input.txt") as f:
		for line in f:
			if map["size"][0] == 0:
				map["size"][0] = len(line) - 1
			map["size"][1] += 1
			for i in range(len(line)):
				if (line[i] >= 'a' and line[i] <= 'z') or (line[i] >= 'A' and line[i] <= 'Z') or (line[i] >= '0' and line[i] <= '9'):
					if line[i] not in map["antennas"]:
						map["antennas"][line[i]] = []
					map["antennas"][line[i]].append(array((i, map["size"][1] - 1)))
	return map

def is_point_in_map(point, map_size):
	return point[0] >= 0 and point[0] < map_size[0] \
		and point[1] >= 0 and point[1] < map_size[1]

def part1():
	map = load_input()
	antinodes = set()
	for antennas in map["antennas"].values():
		for i in range(len(antennas)):
			for j in range(i + 1, len(antennas)):
				vec = antennas[j] - antennas[i]
				curr_antinodes = antennas[i] - vec, antennas[j] + vec
				for antinode in curr_antinodes:
					if is_point_in_map(antinode, map["size"]):
						antinodes.add(tuple(antinode))
	print(len(antinodes))




def part2():
	map = load_input()
	antinodes = set()
	for antennas in map["antennas"].values():
		for i in range(len(antennas)):
			antinodes.add(tuple(antennas[i]))
			for j in range(i + 1, len(antennas)):
				vec = antennas[j] - antennas[i]
				curr_antinodes = []

				curr_antinode = antennas[i] - vec
				while is_point_in_map(curr_antinode, map["size"]):
					curr_antinodes.append(curr_antinode)
					curr_antinode = curr_antinode - vec

				curr_antinode = antennas[j] + vec
				while is_point_in_map(curr_antinode, map["size"]):
					curr_antinodes.append(curr_antinode)
					curr_antinode = curr_antinode + vec

				for antinode in curr_antinodes:
					antinodes.add(tuple(antinode))
	print(len(antinodes))

part1()
part2()