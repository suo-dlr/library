# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/DSL_2_B/judge/10435876/Python3


class BinaryIndexedTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def at(self, i):
        return self.get(i) - self.get(i - 1)

    def set(self, i, x):
        self.add(i, x - self.at(i))
