# require: https://github.com/suo-dlr/library/blob/main/data_structure/SegmentTree.py
# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/GRL_5_D/judge/10437199/Python3


class EularTour:
    # edges は [i, cst], 0-indexed
    def __init__(self, size, edges):
        self.size = size
        self.edges = edges
        self.tour()
        self.sum = SegmentTree(2 * self.size, self.cost, 0, lambda x, y: x + y)
        self.min = SegmentTree(2 * self.size, self.dep, 1 << 60, min)

    # オイラーツアーを行う
    def tour(self):
        in_ord = [-1] * self.size
        out_ord = [-1] * self.size
        dep = [-1] * (2 * self.size)
        cost = [-1] * (2 * self.size)
        a = [-1] * (2 * self.size)
        parent = [-1] * self.size

        go = [[0, 0, 0]]
        idx = 0
        while go:
            i, w, d = go.pop()
            if i >= 0:
                in_ord[i] = idx
                cost[idx] = w
                a[idx] = i
                dep[idx] = d * (self.size << 1) + idx
                idx += 1
                go.append([~i, -w, d - 1])

                for ni, nw in self.edges[i]:
                    if in_ord[ni] != -1:
                        parent[i] = ni
                        continue
                    go.append([ni, nw, d + 1])
            else:
                i = ~i
                out_ord[i] = idx
                cost[idx] = w
                a[idx] = i
                dep[idx] = d * (self.size << 1) + idx
                idx += 1

        self.in_ord = in_ord
        self.out_ord = out_ord
        self.dep = dep
        self.cost = cost
        self.a = a
        self.parent = parent

    # u, v のLCAを求める．戻り値は (LCA のオイラーツアーにおけるindex, 頂点番号)
    def lca(self, u, v):
        u, v = self.in_ord[u], self.in_ord[v]
        if u > v:
            u, v = v, u
        idx = self.min._get(u, v + 1) % (self.size << 1)
        a = self.a[idx]
        return idx, (a if idx == self.in_ord[a] else self.parent[a])

    # i-j 間のコストをwに変更
    def change_cost(self, u, v, w):
        if self.in_ord[u] > self.in_ord[v]:
            u, v = v, u
        self.sum._set(self.in_ord[v], w)
        self.sum._set(self.out_ord[v], -w)

    def add_cost(self, u, v, w):
        if self.in_ord[u] > self.in_ord[v]:
            u, v = v, u
        self.sum._add(self.in_ord[v], w)
        self.sum._add(self.out_ord[v], -w)

    def path_sum(self, u, v):
        in_u = self.in_ord[u]
        in_v = self.in_ord[v]

        return self.sum._get(0, in_u + 1) + self.sum._get(0, in_v + 1) - self.sum._get(0, self.lca(u, v)[0] + 1) * 2
