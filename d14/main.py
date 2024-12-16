from numpy import array

def load_input():
	robots = []
	with open("input.txt") as f:
		for line in f:
			pos, vel = line.split()
			pos = pos.split(',')
			vel = vel.split(',')
			pos[0] = pos[0][2:]
			vel[0] = vel[0][2:]
			pos = array([int(e) for e in pos])
			vel = array([int(e) for e in vel])
			robots.append([pos, vel])
	return robots


def part1():
	robots = load_input()
	map_size = array([101, 103])
	map_center = map_size / 2
	map_center = array([int(e) for e in map_center])
	nb_round = 100
	quarter_tl = 0
	quarter_tr = 0
	quarter_bl = 0
	quarter_br = 0
	for robot in robots:
		robot[0] = (robot[0] + robot[1] * nb_round) % map_size
		if (robot[0][0] == map_center[0] or robot[0][1] == map_center[1]):
			continue
		if (robot[0][1] < map_center[1]):
			if (robot[0][0] < map_center[0]):
				quarter_tl += 1
			else:
				quarter_tr += 1
		else:
			if (robot[0][0] < map_center[0]):
				quarter_bl += 1
			else:
				quarter_br += 1
	print(quarter_tl * quarter_tr * quarter_bl * quarter_br)


def find_group(robots, group_size=50):
	tested_pos = set()
	robots_positions = set([tuple(robot[0]) for robot in robots])
	stack = []
	for robot in robots_positions:
		if robot not in tested_pos:
			stack.append(robot)
			curr_group_size = 0
			while len(stack) != 0:
				curr_pos = stack.pop()
				if curr_pos not in tested_pos:
					curr_group_size += 1
					if curr_group_size == group_size:
						return True
					tested_pos.add(curr_pos)
					if (curr_pos[0] - 1, curr_pos[1]) in robots_positions:
						stack.append((curr_pos[0] - 1, curr_pos[1]))
					if (curr_pos[0] + 1, curr_pos[1]) in robots_positions:
						stack.append((curr_pos[0] + 1, curr_pos[1]))
					if (curr_pos[0], curr_pos[1] - 1) in robots_positions:
						stack.append((curr_pos[0], curr_pos[1] - 1))
					if (curr_pos[0], curr_pos[1] + 1) in robots_positions:
						stack.append((curr_pos[0], curr_pos[1] + 1))
	return False


def part2():
	robots = load_input()
	nb_round = 0
	map_size = array([101, 103])
	while not find_group(robots):
		for robot in robots:
			robot[0] = (robot[0] + robot[1]) % map_size
		nb_round += 1
	for y in range(map_size[1]):
		for x in range(map_size[0]):
			found = False
			for robot in robots:
				if tuple(robot[0]) == (x, y):
					found = True
					break
			print("#" if found else ".", end="")
		print()
	print(nb_round)

part1()
part2()