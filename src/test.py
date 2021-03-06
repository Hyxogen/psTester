# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    test.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: dmeijer <dmeijer@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2021/12/15 16:00:24 by dmeijer       #+#    #+#                  #
#    Updated: 2021/12/16 14:25:58 by dmeijer       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

from asyncio import subprocess
from src.checker import PushSwapObject
import subprocess
import sys

# args = sys.argv
# numbers = []
# args.pop(0)
# executable = args.pop(0)
# for arg in args:
# 	numbers.append(int(arg))



def test(exec: str, numbers: list[int]) -> int:
	obj = PushSwapObject(numbers)
	proc = subprocess.run(["./" + exec, *list(map(str, numbers))], text=True, capture_output=True)
	instructions = proc.stdout.split("\n")
	if proc.returncode != 0:
		return -1
	ret = execute_instructions(instructions, obj)
	if ret == False:
		return -1
	if obj.is_sorted() == False:
		# print("Not sorted")
		# obj.printa()
		return -1
	return len(instructions)

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
	elif instr == "":#TODO just not parse this instruction
		return True
	else:
		print("Unkown instruction:{}".format(instr))
		return False
	return True

# # x = "pb\npb\nrrb\npb\nrb\npb\nrb\npb\nrr\npb\nrb\npb\nrb\npb\nrrb\nrrb\npb\nrb\nrb\nrb\nrb\npa\npa\npa\npa\npa\npa\npa\npa\npa"
# # y = PushSwapObject(numbers)
# # print(execute_instructions(x.split("\n"), y))

# ret = test(executable, numbers)

# if ret <= -1:
# 	print("KO")
# else:
# 	print("OK[{}]".format(ret))

# ret = test(executable, numbers)

# if ret <= -1:
# 	print("KO")
# else:
# 	print("OK[{}]".format(ret))