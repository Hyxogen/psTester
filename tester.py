# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    tester.py                                          :+:    :+:             #
#                                                      +:+                     #
#    By: dmeijer <dmeijer@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2021/12/16 08:46:15 by dmeijer       #+#    #+#                  #
#    Updated: 2021/12/16 11:26:06 by dmeijer       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

from random import random, shuffle
from src.test import test
from src.testresult import TestResult
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import asyncio

numbers = range(0, 50)
shuffle_count = 10

def test_single(scount: int, num: range) -> TestResult:
	num_list = list(num)
	success_count = 0
	results = []
	for i in range(0, scount + 1):
		shuffle(num_list)
		result = test("./../push_swap", num_list)
		results.append(result)
		if result != -1:
			success_count += 1
	return TestResult(num, results, success_count)


for i in range(0, 100):
	res = test_single(1, range(0, i))
	print("{}={}".format(i, "OK" if res.success else "KO"))
	
testResult = test_single(100, range(0, 500))
print("Ave:{} Med:{} Mode:{} Var:{} Std:{} Min:{}, Max:{}".format(testResult.average(), testResult.median(), testResult.mode(), testResult.variance(), testResult.standard_deviation(), testResult.min_val(), testResult.max_val()))