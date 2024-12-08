def load_input():
	input = []
	with open('input.txt') as f:
		for line in f:
			if line[len(line) - 1] == '\n':
				line = line[:len(line) - 1]
			input.append(line)
	return input

def find_word(input, word, pos, dir):
	i = 1
	while i < len(word) and input[pos[1] + i * dir[1]][pos[0] + i * dir[0]] == word[i]:
		i += 1
	if (i == len(word)):
		return True
	return False

def find_words(input, word, pos):
	occ = 0
	for dir_x in range(-1, 2):
		if (dir_x == -1 and pos[0] < len(word) - 1):
			continue
		if (dir_x == 1 and len(input[0]) - pos[0] < len(word)):
			continue

		for dir_y in range(-1, 2):
			if (dir_y == -1 and pos[1] < len(word) - 1):
				continue
			if (dir_y == 1 and len(input) - pos[1] < len(word)):
				continue
			occ += find_word(input, word, pos, (dir_x, dir_y))
	return occ


def part1():
	input = load_input()
	nb_occ = 0
	i = 0
	while i < len(input):
		start_pos = -1
		while True:
			start_pos = input[i].find("X", start_pos + 1)
			if (start_pos == -1):
				break
			nb_occ += find_words(input, "XMAS", (start_pos, i))
		i += 1
	print(nb_occ)
	

def part2():
	input = load_input()
	nb_occ = 0
	i = 0
	while i < len(input) - 2:
		j = 0
		while (j < len(input[i]) - 2):
			if ((input[i][j] == "M" or input[i][j] == "S")
				and (input[i][j + 2] == "M" or input[i][j + 2] == "S")):
				found = find_word(input, "MAS" if input[i][j] == "M" else "SAM", (j, i), (1, 1))
				if (found):
					found = find_word(input, "MAS" if input[i][j + 2] == "M" else "SAM", (j + 2, i), (-1, 1))
				nb_occ += found
			j += 1
		i += 1
	print(nb_occ)

part1()
part2()