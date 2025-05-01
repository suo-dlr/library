# require: https://github.com/suo-dlr/library/blob/main/data_structure/SegmentTree.py
# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/GRL_5_D/judge/10437287/Python3


class HLDecomposition:
    def __init__(self, n, edges, data, e=1 << 60, comp=min):
        self.n = n
        self.edges = edges
        self.parent = [-1] * n
        self.size = [1] * n
        self._dfs1()

        self.order = [0] * n  # 行きがけ順にノードを並べたもの
        self.head = [-1] * n
        self._dfs2()

        self.revord = [0] * n
        for idx, i in enumerate(self.order):
            self.revord[i] = idx

        self.data = data
        self.seg = SegmentTree(n, [data[i] for i in self.order], e, comp)
        self.e = e
        self.comp = comp

    # 部分木のサイズを計算
    def _dfs1(self):
        st = [~0, 0]
        while st:
            i = st.pop()
            if i >= 0:
                pi = self.parent[i]
                for j in self.edges[i]:
                    if j == pi:
                        continue
                    self.parent[j] = i
                    st.append(~j)
                    st.append(j)
            else:
                i = ~i
                pi = self.parent[i]
                s = 1
                s0 = -1
                for idx, j in enumerate(self.edges[i]):
                    if j == pi:
                        continue
                    sj = self.size[j]
                    s += sj
                    if sj > s0:
                        self.edges[i][0], self.edges[i][idx] = self.edges[i][idx], self.edges[i][0]
                        s0 = sj
                self.size[i] = s

    def _dfs2(self):
        st = [0]
        oi = 0
        self.head[0] = 0
        while st:
            i = st.pop()
            self.order[oi] = i
            oi += 1
            pi = self.parent[i]
            for idx, j in enumerate(self.edges[i][::-1]):
                if j == pi:
                    continue
                st.append(j)
                if idx == len(self.edges[i]) - 1:
                    self.head[j] = self.head[i]
                else:
                    self.head[j] = j

    def lca(self, u, v):
        while True:
            if self.revord[u] > self.revord[v]:
                u, v = v, u
            if self.head[u] == self.head[v]:
                return u
            v = self.parent[self.head[v]]

    def query(self, u, v):
        res = self.e
        while True:
            if self.revord[u] > self.revord[v]:
                u, v = v, u
            if self.head[u] == self.head[v]:
                res = self.comp(res, self.seg._get(self.revord[u], self.revord[v] + 1))
                break
            res = self.comp(res, self.seg._get(self.revord[self.head[v]], self.revord[v] + 1))
            v = self.parent[self.head[v]]
        return res

    def query_edge(self, u, v):
        res = self.e
        while True:
            if self.revord[u] > self.revord[v]:
                u, v = v, u
            if self.head[u] == self.head[v]:
                res = self.comp(res, self.seg._get(self.revord[u] + 1, self.revord[v] + 1))
                break
            res = self.comp(res, self.seg._get(self.revord[self.head[v]], self.revord[v] + 1))
            v = self.parent[self.head[v]]
        return res

    def update(self, u, w):
        self.seg._set(self.revord[u], w)

    def add(self, u, w):
        iu = self.revord[u]
        self.seg._add(iu, w)

    def update_edge(self, u, v, w):
        if self.parent[u] == v:
            self.update(u, w)
        else:
            self.update(v, w)

    def add_edge(self, u, v, w):
        if self.parent[u] == v:
            self.add(u, w)
        else:
            self.add(v, w)
