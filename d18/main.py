from numpy import array

def load_input():
	obstacles = []
	with open("input.txt") as f:
		for line in f:
			obstacles.append(tuple([int(e) for e in line.split(',')]))
	return obstacles


def part1():
	byte_fallen = 1024
	map_obstacle = load_input()[:byte_fallen]
	pos = array([0, 0])
	end = (70, 70)
	vertices = {}
	vertices[tuple(pos)] = {"visited": True, "time": 0}
	while tuple(pos) != end:
		vertices[tuple(pos)]["visited"] = True
		for dir in (array([1, 0]), array([0, 1]), array([-1, 0]), array([0, -1])):
			new_pos = pos + dir
			cost = vertices[tuple(pos)]["time"] + 1
			if (new_pos >= (0, 0)).all() and (new_pos <= end).all() \
				and tuple(new_pos) not in map_obstacle:
				if tuple(new_pos) not in vertices:
					vertices[tuple(new_pos)] = {"visited": False, "time": None}
				if vertices[tuple(new_pos)]["time"] is None or vertices[tuple(new_pos)]["time"] > cost:
					vertices[tuple(new_pos)]["time"] = cost
					vertices[tuple(new_pos)]["visited"] = False

		costless_v = None
		for pos, v in vertices.items():
			if v["visited"] == False and (costless_v is None or vertices[costless_v]["time"] > v["time"]):
				costless_v = pos
		
		if costless_v is None:
			print("unfinishable map")
			break

		pos = array(costless_v)
	print(pos, vertices[tuple(pos)])


def part2():
	map_obstacle = load_input()
	start_byte_fallen = 1024
	max_byte = len(map_obstacle)
	end = (70, 70)
	byte_fallen = 0
	
	while start_byte_fallen + 1 != byte_fallen:
		unfinishable = False
		byte_fallen = int((max_byte + start_byte_fallen) / 2)
		print("byte_fallen", byte_fallen, start_byte_fallen, max_byte)
		pos = array([0, 0])
		vertices = {}
		vertices[tuple(pos)] = {"visited": True, "time": 0}
		
		while tuple(pos) != end:
			vertices[tuple(pos)]["visited"] = True
			for dir in (array([1, 0]), array([0, 1]), array([-1, 0]), array([0, -1])):
				new_pos = pos + dir
				cost = vertices[tuple(pos)]["time"] + 1
				if (new_pos >= (0, 0)).all() and (new_pos <= end).all() \
					and tuple(new_pos) not in map_obstacle[:byte_fallen]:
					if tuple(new_pos) not in vertices:
						vertices[tuple(new_pos)] = {"visited": False, "time": None}
					if vertices[tuple(new_pos)]["time"] is None or vertices[tuple(new_pos)]["time"] > cost:
						vertices[tuple(new_pos)]["time"] = cost
						vertices[tuple(new_pos)]["visited"] = False

			costless_v = None
			for pos, v in vertices.items():
				if v["visited"] == False and (costless_v is None or vertices[costless_v]["time"] > v["time"]):
					costless_v = pos
			
			if costless_v is None:
				print("unfinishable")
				max_byte = byte_fallen
				unfinishable = True
				break

			pos = array(costless_v)
		if not unfinishable:
			print("finishable")
			start_byte_fallen = byte_fallen
	print(map_obstacle[byte_fallen - 1], byte_fallen)

part1()
part2()