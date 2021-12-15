from asyncio import subprocess
from xmlrpc.client import boolean
from checker import PushSwapObject
import subprocess
import sys

args = sys.argv
numbers = []
args.pop(0)
executable = args.pop(0)
for arg in args:
	numbers.append(int(arg))

# print("Exec:{} numbers:{}".format(executable, numbers))

def test(exec: str, argv, n) -> int:
	obj = PushSwapObject(n)
	proc = subprocess.run(["./" + exec, *argv], text=True, capture_output=True)
	instructions = proc.stdout.split("\n")
	if proc.returncode != 0:
		return -1
	if execute_instructions(instructions, obj) == False:
		return -1
	if obj.is_sorted == False:
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
	elif instr == "sa":
		object.rr()
	elif instr == "rra":
		object.rra()
	elif instr == "rrb":
		object.rrb()
	elif instr == "rrr":
		object.rrr()
	else:
		return False
	return True

if test(executable, args, numbers) == False:
	print("KO")
else:
	print("OK")