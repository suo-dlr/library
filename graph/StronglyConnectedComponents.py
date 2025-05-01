# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/GRL_3_C/judge/10437060/Python3


class StronglyConnectedComponents:
    # n -> 頂点数, edges -> 辺 で各頂点に対する帰りがけの順番と成分ごとの切れ目を返す
    def dfs(self, n, edges, order):
        t = [-1] * n
        d = []
        seen = [False] * n
        cnt = 0
        for i in order:
            if seen[i]:
                continue
            st = [~i, i]
            d.append(cnt)
            while st:
                i = st.pop()
                if i < 0:
                    i = ~i
                    if t[i] > -1:
                        continue
                    t[i] = cnt * n + i
                    cnt += 1
                else:
                    if seen[i]:
                        continue
                    seen[i] = True
                    for j in edges[i]:
                        if seen[j]:
                            continue
                        st.append(~j)
                        st.append(j)
            d.append(cnt)
        return t, d

    # n -> 頂点数, edges -> 辺, -> redges -> 逆辺 でsccを返す
    def scc(self, n, edges, redges):
        t, d = self.dfs(n, edges, range(n))
        t.sort(reverse=True)
        t, d = self.dfs(n, redges, [i % n for i in t])
        t.sort()
        t = [i % n for i in t]

        res = []
        for i in range(0, len(d), 2):
            res.append(t[d[i] : d[i + 1]])
        return res
