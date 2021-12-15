# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    checker.py                                         :+:    :+:             #
#                                                      +:+                     #
#    By: dmeijer <dmeijer@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2021/12/15 16:00:27 by dmeijer       #+#    #+#                  #
#    Updated: 2021/12/15 16:25:58 by dmeijer       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

from collections import deque
from platform import python_branch

class PushSwapObject:
	stackA = deque()
	stackB = deque()

	# def rx(self, stack, val):
	# 	stack.rotate(val)
	# check if this works

	def __init__(self, arr: list[int]):
		for x in arr:
			self.stackA.append(x)

	def ra(self, val = -1):
		self.stackA.rotate(val)
	
	def rb(self, val = -1):
		self.stackB.rotate(val)
	
	def rr(self, val = -1):
		self.ra(val)
		self.rb(val)

	def rra(self, val = -1):
		self.ra(-val)
	
	def rrb(self, val = -1):
		self.rb(-val)

	def rrr(self, val = -1):
		self.rr(-val)
	
	def pa(self):
		self.stackA.appendleft(self.stackB.popleft())
	
	def pb(self):
		self.stackB.appendleft(self.stackA.popleft())

	def sa(self):
		first = self.stackA.popleft()
		second = self.stackA.popleft()
		self.stackA.appendleft(first)
		self.stackA.appendleft(second)
	
	def sb(self):
		first = self.stackB.popleft()
		second = self.stackB.popleft()
		self.stackB.appendleft(first)
		self.stackB.appendleft(second)
	
	def ss(self):
		self.sa()
		self.sb()

	def printa(self):
		for x in self.stackA:
			print("{} ".format(x), end=";")
		print("")

	def printb(self):
		for x in self.stackB:
			print("{} ".format(x), end=";")
		print("")

	def is_sorted(self) -> bool:
		if len(self.stackB) != 0:
			return False
		return sorted(self.stackA) == list(self.stackA)