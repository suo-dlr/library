# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/DSL_1_A/judge/10435893/Python3


class UnionFind:
    def __init__(self, length):
        self.parent = [i for i in range(length + 1)]
        self.size = [1] * (length + 1)

    def root(self, i):
        p = i
        while self.parent[p] != p:
            p = self.parent[p]
        while i != p:
            tmp = i
            i = self.parent[i]
            self.parent[tmp] = p
        return p

    def check(self, a, b):
        return self.root(a) == self.root(b)

    def unite(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.parent[b] = a
