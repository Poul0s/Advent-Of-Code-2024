from math import floor

def load_input():
	input = [
		[],
		[]
	]
	with open('input.txt') as f:
		updates = False
		for line in f:
			if (updates == False):
				if (line == "\n"):
					updates = True
				else:
					order_rule = line.split("|")
					input[0].append([int(order_rule[0]), int(order_rule[1])])
			else:
				input[1].append([int(x) for x in line.split(",")])
	return input

def is_updates_correct(updates, nb_bef, nb_aft):
	for i in range(len(updates)):
		j = 0
		while (j < len(updates)):
			if (j != i):
				if (j < i):
					if ((updates[i] in nb_aft and updates[j] in nb_aft[updates[i]])
							or (updates[j] in nb_bef and updates[i] in nb_bef[updates[j]])):
						return False
				else:
					if ((updates[i] in nb_bef and updates[j] in nb_bef[updates[i]])
							or (updates[j] in nb_aft and updates[i] in nb_aft[updates[j]])):
						return False
			j += 1
	return True

def part1():
	input = load_input()
	nb_bef = {}
	nb_aft = {}
	for rule in input[0]:
		if (rule[0] not in nb_aft):
			nb_aft[rule[0]] = set()
		nb_aft[rule[0]].add(rule[1])


		if (rule[1] not in nb_bef):
			nb_bef[rule[1]] = set()
		nb_bef[rule[1]].add(rule[0])
		

	res = 0
	for updates in input[1]:
		if (is_updates_correct(updates, nb_bef, nb_aft)):
			res += updates[floor(len(updates) / 2)]
	print(res)

def part2():
	input = load_input()
	nb_bef = {}
	nb_aft = {}
	for rule in input[0]:
		if (rule[0] not in nb_aft):
			nb_aft[rule[0]] = set()
		nb_aft[rule[0]].add(rule[1])


		if (rule[1] not in nb_bef):
			nb_bef[rule[1]] = set()
		nb_bef[rule[1]].add(rule[0])
		

	res = 0
	for updates in input[1]:
		good = is_updates_correct(updates, nb_bef, nb_aft)
		if (not good):
			new_list = [updates[0]]
			for i in range(1, len(updates)):
				j = 0
				while (j <= len(new_list)):
					new_list.insert(j, updates[i])
					if (not is_updates_correct(new_list, nb_bef, nb_aft)):
						new_list.pop(j)
					else:
						break
					j += 1
			res += new_list[floor(len(new_list) / 2)]
	print(res)

part1()
part2()