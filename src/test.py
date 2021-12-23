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

from typing import List

from pushswap import PushSwapObject
from testresult import TestResult, comp_result
from testresult import is_better
from savefile import SaveFile
import process

gSem = None
gTotal = 0


async def Test(exec: str, numbers: list) -> int:
    global gTotal
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
    gTotal += 1
    print(gTotal)
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
    return TestResult(number_range, results, success_count)


async def print_result(result: TestResult):
    print("Ave:{}, Med:{}, Mod:{}, Var:{}, Std:{}, Min:{}, Max:{}".format(result.average(), result.median(),
                                                                          result.mode(),
                                                                          result.variance(),
                                                                          result.standard_deviation(), result.min_val(),
                                                                          result.max_val()))


async def NewTestRun(execn: str, shuffle_count: int, test_range: range) -> List[TestResult]:
    ranges = []
    results = []
    for i in test_range:
        ranges.append(range(0, i))
    for number_range in ranges:
        result = await TestRange(execn, shuffle_count, number_range)
        results.append(result)
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


def print_result_new(new: TestResult, comp: TestResult):
    if new.num_range != comp.num_range:
        print("Invalid comparison!")
    val = comp_result(comp, new)
    if val < 0:
        print("\033[0mRange ({},{}) Average:\033[0;32m{}\033[0m Best Average:\033[0;31m{}".format(
            new.num_range.start, new.num_range.stop, new.average(), comp.average()))
    elif val > 0:
        print("\033[0mRange ({},{}) Average:\033[0;31m{}\033[0m Best Average:\033[0;32m{}".format(
            new.num_range.start, new.num_range.stop, new.average(), comp.average()))
    else:
        print("\033[0mRange ({},{}) Average:\033[0;37m{}\033[0m Best Average:\033[0;37m{}".format(
            new.num_range.start, new.num_range.stop, new.average(), comp.average()))


async def run_and_save(save_file: SaveFile, execn: str, shuffle_count: int, num_range: range):
    results = await NewTestRun(execn, shuffle_count, num_range)
    for result in results:
        comp = save_file.get_best(result.num_range)
        if not comp:
            save_file.add_result(result, True)
            print("No previous entry to compare to")
        else:
            save_file.add_result(result, is_better(result, comp))
            print_result_new(result, comp)
    save_file.save_file()


async def main():
    global gSem
    gSem = asyncio.Semaphore(500)
    shuffle_count = 10000
    save_file = SaveFile("../data/data.json")
    execn = "../../push_swap"
    await asyncio.gather(
        run_and_save(save_file, execn, 1000, range(0, 11)),
        # run_and_save(save_file, execn, shuffle_count, range(20, 21)),
        run_and_save(save_file, execn, shuffle_count, range(50, 51)),
        # run_and_save(save_file, execn, shuffle_count, range(100, 101)),
        # run_and_save(save_file, execn, shuffle_count, range(200, 201)),
        # run_and_save(save_file, execn, shuffle_count, range(300, 301)),
        run_and_save(save_file, execn, shuffle_count, range(400, 401)),
        run_and_save(save_file, execn, shuffle_count, range(500, 501))
    )


if __name__ == "__main__":
    asyncio.run(main())
