# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/GRL_6_A/judge/10436119/Python3


from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for i in range(n)]

    def add_edge(self, u, v, c):
        self.edges[u].append([v, c, len(self.edges[v])])
        self.edges[v].append([u, 0, len(self.edges[u]) - 1])

    def bfs(self, t):
        go = deque([t])
        time = [-1] * self.n
        time[t] = 0
        while go:
            i = go.popleft()
            ti = time[i]
            for j, c, _ in self.edges[i]:
                if not c or time[j] > -1:
                    continue
                time[j] = ti + 1
                go.append(j)
        self.time = time

    def dfs(self, s, t):
        st = [(s << 1, 1 << 60)]
        ret = 0

        while st:
            i, f = st.pop()
            m = i & 1
            i >>= 1

            if i == t:
                ret = f
                continue

            if m and ret:
                e = self.edges[i][self.iter[i]]
                e[1] -= ret
                self.edges[e[0]][e[2]][1] += ret
                continue

            if m:
                self.iter[i] += 1

            for j in range(self.iter[i], len(self.edges[i])):
                to, cap, _ = self.edges[i][j]
                self.iter[i] = j
                if cap > 0 and self.time[i] < self.time[to]:
                    st.append(((i << 1) ^ 1, f))
                    st.append((to << 1, min(f, cap)))
                    break

        return ret

    def flow(self, s, t):
        res = 0
        while True:
            self.bfs(s)
            if self.time[t] == -1:
                break
            self.iter = [0] * self.n
            f = self.dfs(s, t)
            while f:
                res += f
                f = self.dfs(s, t)

        return res
