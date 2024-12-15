from functools import lru_cache

def load_input():
	with open("input.txt") as f:
		return f.read().split(' ')

@lru_cache
def blink(stones):
	i = 0
	if len(stones) > 5:
		res = []
		pad = int(len(stones) / 4)
		sep = 0
		while (sep <= len(stones)):
			part = stones[sep:sep + pad]
			sep += pad
			part = blink(part)
			res = res + part
		return res

	stones = list(stones)
	while i < len(stones):
		if stones[i] == "0":
			stones[i] = "1"
		elif len(stones[i]) % 2 == 0:
			mid = int(len(stones[i]) / 2)
			new_stone = stones[i][mid:].lstrip('0')
			if len(new_stone) == 0:
				new_stone = '0'
			stones[i] = stones[i][:mid]
			i += 1
			stones.insert(i, new_stone)
		else:
			stones[i] = str(int(stones[i]) * 2024)
		i += 1

	return stones

def part1():
	stones = load_input()
	for _ in range(25):
		stones = blink(tuple(stones))
	print(len(stones))

def part2():
	stones = load_input()
	for i in range(75):
		print("turn", i, len(stones))
		stones = blink(tuple(stones))
	print(len(stones))

part1()
part2()