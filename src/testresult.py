# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    testresult.py                                      :+:    :+:             #
#                                                      +:+                     #
#    By: dmeijer <dmeijer@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2021/12/15 16:56:47 by dmeijer       #+#    #+#                  #
#    Updated: 2021/12/16 10:01:14 by dmeijer       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #
import math
from statistics import mean, median, mode, stdev, variance

class TestResult:
	def __init__(self, num_range: range, results: list, succcess_count: int):
		self.num_range = num_range
		self.results = results
		self.success_count = succcess_count
		self.success = succcess_count = len(results)
		self.results_sorted = sorted(results)

	def average(self) -> float:
		if self.success == False:
			return 0
		return mean(self.results_sorted)
	
	def median(self) -> float:
		if self.success == False:
			return 0
		return median(self.results_sorted)
	
	def mode(self) -> float:
		if self.success == False:
			return 0
		return mode(self.results_sorted)
	
	def variance(self) -> float:
		if self.success == False:
			return 0
		return variance(self.results)
	
	def standard_deviation(self) -> float:
		if self.success == False:
			return 0
		return stdev(self.results)
	
	def min_val(self) -> int:
		if self.success == False:
			return 0
		return min(self.results)
	
	def max_val(self) -> int:
		if self.success == False:
			return 0
		return max(self.results)


def is_better(b: TestResult, a: TestResult):
	a_av = a.average()
	a_std = a.standard_deviation()
	b_av = b.average()
	b_count = len(b.results)
	test = (1.65 * a_std) / math.sqrt(b_count)
	if b_av < (a_av - test):
		return True
	return False
