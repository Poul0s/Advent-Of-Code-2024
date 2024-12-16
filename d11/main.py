from functools import cache

def load_input():
	with open("input.txt") as f:
		return f.read().split(' ')

@cache
def blink(stone, blink_nb):
	if blink_nb == 0:
		return 1
	
	if stone == "0":
		return blink("1", blink_nb - 1)
	elif len(stone) % 2 == 0:
		mid =  int(len(stone) / 2)
		new_stone = stone[mid:].lstrip('0')
		if len(new_stone) == 0:
			new_stone = '0'
		stone = stone[:mid]
		return blink(stone, blink_nb - 1) + blink(new_stone, blink_nb - 1)
	else:
		return blink(str(int(stone) * 2024), blink_nb - 1)

def part1():
	stones = load_input()
	res = 0
	for stone in stones:
		res += blink(stone, 25)
	print(res)

def part2():
	stones = load_input()
	res = 0
	for stone in stones:
		res += blink(stone, 75)
	print(res)

part1()
part2()