# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    pushswap.py                                        :+:    :+:             #
#                                                      +:+                     #
#    By: dmeijer <dmeijer@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2021/12/15 16:00:27 by dmeijer       #+#    #+#                  #
#    Updated: 2021/12/16 15:51:33 by dmeijer       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

from collections import deque


class PushSwapObject:
    def __init__(self, arr: list):
        self.stackA = deque()
        self.stackB = deque()
        for x in arr:
            self.stackA.append(x)

    def rx(self, stack: deque, val):
        stack.rotate(-val)

    def rrx(self, stack: deque, val):
        self.rx(stack, -val)

    def sx(self, stack: deque):
        first = stack.popleft()
        second = stack.popleft()
        stack.appendleft(first)
        stack.appendleft(second)

    def ra(self, val=1):
        self.rx(self.stackA, val)

    def rb(self, val=1):
        self.rx(self.stackB, val)

    def rr(self, val=1):
        self.ra(val)
        self.rb(val)

    def rra(self, val=1):
        self.rx(self.stackA, -val)

    def rrb(self, val=1):
        self.rx(self.stackB, -val)

    def rrr(self, val=1):
        self.rra(val)
        self.rrb(val)

    def pa(self):
        self.stackA.appendleft(self.stackB.popleft())

    def pb(self):
        self.stackB.appendleft(self.stackA.popleft())

    def sa(self):
        self.sx(self.stackA)

    def sb(self):
        self.sx(self.stackB)

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
