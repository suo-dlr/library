from sys import setrecursionlimit
from collections import defaultdict
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
setrecursionlimit(1 << 20)


class AuxiliaryTree:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.dfs()

    def dfs(self):
        n = self.n
        dep = [0] * n
        parent = [-1] * n
        in_ord = []
        st = [0]

        while st:
            i = st.pop()
            in_ord.append(i)
            pi = parent[i]
            di = dep[i]
            for j in self.edges[i]:
                if j == pi:
                    continue
                parent[j] = i
                dep[j] = di + 1
                st.append(j)

        anc = [[i] for i in parent]
        for j in range(len(bin(n)) - 1):
            for ai in anc:
                if ai[-1] == -1:
                    ai.append(-1)
                else:
                    ai.append(anc[ai[-1]][j])

        self.dep = dep
        self.in_ord = [0] * n
        for idx, i in enumerate(in_ord):
            self.in_ord[i] = idx
        self.anc = anc

    def lca(self, u, v):
        dep = self.dep
        anc = self.anc
        if dep[u] < dep[v]:
            u, v = v, u

        dd = dep[u] - dep[v]
        i = 0
        while dd:
            if dd & 1:
                u = anc[u][i]
            dd >>= 1
            i += 1

        if u == v:
            return u

        for i in range(len(anc[0]) - 1, -1, -1):
            if anc[u][i] != anc[v][i]:
                u = anc[u][i]
                v = anc[v][i]
        return anc[u][0]

    # 頂点集合 v と、それらの LCA からなる木をつくる
    def comp(self, v):
        if not v:
            return None, None

        v.sort(key=lambda x: self.in_ord[x])
        dep = self.dep
        childs = defaultdict(list)
        st = [v[0]]
        for i in range(len(v) - 1):
            w = self.lca(v[i], v[i + 1])

            if v[i] != w:
                t = st.pop()
                while st and dep[w] < dep[st[-1]]:
                    childs[st[-1]].append(t)
                    t = st.pop()

                if not st or st[-1] != w:
                    st.append(w)
                childs[w].append(t)

            st.append(v[i + 1])

        while len(st) > 1:
            childs[st[-2]].append(st.pop())

        return childs, st[-1]
