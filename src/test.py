# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    test.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: dmeijer <dmeijer@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2021/12/15 16:00:24 by dmeijer       #+#    #+#                  #
#    Updated: 2021/12/16 16:16:15 by dmeijer       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import asyncio
from random import shuffle
from pushswap import PushSwapObject
import process

gSem = None

async def Test(exec: str, numbers: list[int]):
	obj = PushSwapObject(numbers)
	code, out, err = await process.ExecuteProcess(exec, map(str, numbers), gSem)
	instr_count = 0
	if code != 0:
		return False, None
	while True:
		data = out.readline()
		if not data:
			break
		line = data.decode("ascii").rstrip()
		execute_instruction(line, obj)
		instr_count += 1
	if not obj.is_sorted():
		return False, None
	return True, instr_count

def execute_instructions(instructions: list, object: PushSwapObject) -> bool:
	for inst in instructions:
		if execute_instruction(inst, object) == False:
			return False
	return True

def execute_instruction(instr: str, object: PushSwapObject) -> bool:
	if instr == "ra":
		object.ra()
	elif instr == "rb":
		object.rb()
	elif instr == "rr":
		object.rr()
	elif instr == "sa":
		object.sa()
	elif instr == "sb":
		object.sb()
	elif instr == "ss":
		object.ss()
	elif instr == "rra":
		object.rra()
	elif instr == "rrb":
		object.rrb()
	elif instr == "rrr":
		object.rrr()
	elif instr == "pb":
		object.pb()
	elif instr == "pa":
		object.pa()
	else:
		print("Unkown instruction:{}".format(instr))
		return False
	return True

async def main():
	global gSem
	test_lists = []
	gSem = asyncio.Semaphore(10)
	for i in range(0, 50):
		l = list(range(0, i + 1))
		shuffle(l)
		test_lists.append(l)
	await asyncio.gather(*[Test("../../push_swap", test_list) for test_list in test_lists])

if __name__ == "__main__":
	asyncio.run(main())