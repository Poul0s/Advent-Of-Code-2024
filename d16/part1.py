from numpy import array

def load_input():
	vertices, start, end = [], array([0, 0]), [0, 0]
	with open("input.txt") as f:
		y = -1
		for line in f:
			y += 1
			for x in range(len(line)):
				if line[x] == 'S':
					start[0], start[1] = x, y
				elif line[x] == 'E':
					end[0], end[1] = x, y

				if (line[x] != '#' and line[x] != '\n'):
					vertices.append({
						"pos": (x, y),
						"time": None,
						"time_dir": None,
						"visited": False
					})
	return vertices, start, end

v_pos_cache = {}
def find_vertice(vertices, pos):
	if pos in v_pos_cache:
		return v_pos_cache[pos]
	for i in range(len(vertices)):
		if vertices[i]["pos"] == pos:
			v_pos_cache[pos] = vertices[i]
			return vertices[i]
	v_pos_cache[pos] = None
	return None


vertices, pos, end = load_input()
curr_vertice = find_vertice(vertices, tuple(pos))
curr_vertice["time"] = 0
curr_vertice["time_dir"] = array([1, 0])
while list(curr_vertice["pos"]) != end:
	curr_vertice["visited"] = True
	# estimating cost
	for dir in (array([1, 0]), array([0, 1]), array([-1, 0]), array([0, -1])):
		v = find_vertice(vertices, tuple(array(curr_vertice["pos"]) + dir))
		if v:
			cost = curr_vertice["time"] + 1
			if (curr_vertice["time_dir"] != dir).any():
				cost += 1000
				dir_add = curr_vertice["time_dir"] + dir
				if (curr_vertice["time_dir"] + dir)[0] == 0:
					cost += 1000
			if v["time"] == None or v["time"] > cost:
				v["time"] = cost
				v["time_dir"] = dir
				v["visited"] = False


	#choosing costless vertice
	costless_v = None
	for v in vertices:
		if v["visited"] == False and v["time"] is not None and (costless_v is None or costless_v["time"] > v["time"]):
			costless_v = v
	
	if costless_v is None:
		print("unfinishable map")
		break

	curr_vertice = costless_v

print(curr_vertice["time"])







