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
from testresult import TestResult
import process

gSem = None


async def Test(exec: str, numbers: list) -> int:
    obj = PushSwapObject(numbers)
    code, out, err = await process.ExecuteProcess(exec, map(str, numbers), gSem)
    instr_count = 0
    if code != 0:
        return -1
    while True:
        data = await out.readline()
        if not data:
            break
        line = data.decode("ascii").rstrip()
        if not execute_instruction(line, obj):
            return -1
        instr_count += 1
    if not obj.is_sorted():
        return -1
    print("OK[{}]".format(instr_count))
    return instr_count


async def TestRange(execn: str, shuffle_count: int, number_range: range) -> TestResult:
    test_lists = []
    results = []
    success_count = 0
    for i in range(0, shuffle_count):
        test_list = list(number_range)
        shuffle(test_list)
        test_lists.append(test_list)
    for test_list in test_lists:
        result = await Test(execn, test_list)
        results.append(result)
        success_count += 1 if result >= 0 else 0
    # await asyncio.gather(*[results.append(Test(execn, testList)) for testList in test_lists])
    return TestResult(number_range, results, success_count)


async def NewTestRun(execn: str, shuffle_count: int, test_range: range) -> list:
    ranges = []
    results = []
    for i in test_range:
        ranges.append(range(0, i))
    for number_range in ranges:
        result = await TestRange(execn, shuffle_count, number_range)
        results.append(result)
    # await asyncio.gather(*[results.append(TestRange(execn, shuffle_count, number_range)) for number_range in ranges])
    return results

def execute_instructions(instructions: list, object: PushSwapObject) -> bool:
    for inst in instructions:
        if not execute_instruction(inst, object):
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
        print("Unknown instruction:{}".format(instr))
        return False
    return True


async def main():
    global gSem
    gSem = asyncio.Semaphore(10)
    # await NewTestRun("../../push_swap", 20, range(0, 20))
    await asyncio.gather(NewTestRun("../../push_swap", 20, range(0, 20)))


if __name__ == "__main__":
    asyncio.run(main())
