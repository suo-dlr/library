from collections import deque


class SlidingWindowAggregation:
    def __init__(self, func, e):
        self.af = deque()
        self.ab = deque()
        self.b = deque()
        self.e = e
        self.func = func

    def push(self, x):
        b = self.b
        ab = self.ab

        b.append(x)
        if not ab:
            ab.append(x)
        else:
            ab.append(self.func(x, ab[-1]))

    def pop(self):
        af = self.af
        b = self.b
        ab = self.ab
        if not af:
            while b:
                ab.pop()
                v = b.pop()
                if not af:
                    af.appendleft(v)
                else:
                    af.appendleft(self.func(v, af[0]))
        if af:
            af.popleft()

    def get_sum(self):
        res = self.e
        if self.af:
            res = self.func(res, self.af[0])
        if self.ab:
            res = self.func(res, self.ab[-1])
        return res
