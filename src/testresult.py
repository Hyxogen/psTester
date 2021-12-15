from statistics import mean, median, mode, stdev, variance


class TestResult:
	num_range = range[int]
	results = list[int]
	results_sorted = list[int]
	success_count = int
	success = bool

	def __init__(self, num_range: range[int], results: list[int], succcess_count: int):
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