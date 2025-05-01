# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/GRL_1_B/judge/10436057/Python3


class BellmanFord:
    def __init__(self, size, inf=1 << 63):
        self.size = size
        self.inf = inf
        self.edge = [[] for _ in range(size + 1)]

    def add_edge(self, from_, to, time):
        self.edge[from_].append([to, time])

    def main(self, s):
        time = [self.inf] * self.size
        time[s] = 0
        upd = {s}
        for _ in range(self.size):
            new = set()
            for i in upd:
                ti = time[i]
                for j, dt in self.edge[i]:
                    if time[j] > ti + dt:
                        time[j] = ti + dt
                        new.add(j)
            upd = new
            if not upd:
                break

        if upd:
            return []
        else:
            return time
