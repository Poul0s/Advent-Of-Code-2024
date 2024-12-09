def load_input():
	disk = []
	with open("input.txt") as f:
		input = f.read()
		curr_id = 0
		reading_free = False
		for c in input:
			if reading_free:
				if int(c) != 0:
					disk.append([-1, int(c)])
			else:
				if int(c) != 0:
					disk.append([curr_id, int(c)])
				curr_id += 1
			reading_free = not reading_free
	return disk

def first_free_space_pos(disk):
	i = 0
	while i < len(disk):
		if disk[i][0] == -1:
			return i
		i += 1
	return -1

def part1():
	disk = load_input()
	free_space = first_free_space_pos(disk)
	while (free_space != -1):
		last_block = disk[len(disk) - 1]
		new_elem_size = min(disk[free_space][1], last_block[1])
		new_elem = [last_block[0], new_elem_size]
		
		last_block[1] -= new_elem_size
		if last_block[1] == 0:
			disk.pop()
		if disk[len(disk) - 1][0] == -1:
			disk.pop()

		if (free_space < len(disk)):
			disk[free_space][1] -= new_elem_size
			if disk[free_space][1] == 0:
				disk.pop(free_space)
		disk.insert(free_space, new_elem)
		free_space = first_free_space_pos(disk)
	res = 0
	i = 0
	while len(disk) > 0:
		res += i * disk[0][0]
		i += 1
		disk[0][1] -= 1
		if (disk[0][1] == 0):
			disk.pop(0)
	print(res)

	
def part2():
	disk = load_input()
	i = len(disk) - 1
	while i > 0:
		if disk[i][0] == -1:
			i -= 1
			continue
		j = 0
		while j < i:
			if (disk[j][0] == -1 and disk[j][1] >= disk[i][1]):
				break
			j += 1
		if (j < i):
			file = disk[i].copy()
			disk[i][0] = -1
			disk.insert(j, file)
			
			if disk[i][0] == -1:
				disk[i][1] += disk[i + 1][1]
				disk.pop(i + 1)
			else:
				i += 1
			
			if (i < len(disk) - 2 and disk[i + 1][0] == -1):
				disk[i][1] += disk[i + 1][1]
				disk.pop(i + 1) 

			disk[j + 1][1] -= file[1]
			if (disk[j + 1][1] == 0):
				disk.pop(j + 1)
				i -= 1
		i -= 1
	curr_p = 0
	i = 0
	res = 0
	while i < len(disk):
		if (disk[i][0] == -1):
			curr_p += disk[i][1]
		else:
			while (disk[i][1] > 0):
				res += disk[i][0] * curr_p
				disk[i][1] -= 1
				curr_p += 1
		i += 1
	print(res)


part1()
part2()