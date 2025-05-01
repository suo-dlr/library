class RollbackUnionFind:
    def __init__(self, length):
        self.parent = [i for i in range(length + 1)]
        self.size = [1] * (length + 1)
        self.history = []

    def root(self, i):
        p = i
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def check(self, a, b):
        return self.root(a) == self.root(b)

    def unite(self, a, b):
        a, b = self.root(a), self.root(b)
        if self.size[a] < self.size[b]:
            a, b = b, a

        self.history.append(
            (
                a,
                self.size[a],
                b,
                self.size[b],
            )
        )

        if a == b:
            return

        self.size[a] += self.size[b]
        self.parent[b] = a

    def undo(self):
        if not self.history:
            return
        a, sa, b, sb = self.history.pop()

        self.parent[a] = a
        self.size[a] = sa
        self.parent[b] = b
        self.size[b] = sb
