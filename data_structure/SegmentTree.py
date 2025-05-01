# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/DSL_2_B/judge/10435880/Python3


class SegmentTree:
    # n->要素数, l->リスト, e->単位元, comp->二項関数
    def __init__(self, n, l, e, comp):
        self.e = e
        self.comp = comp
        self.n = 1 << (n - 1).bit_length()
        self.tree = [self.e] * self.n + l + [self.e] * (self.n - len(l))
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = comp(self.tree[2 * i], self.tree[2 * i + 1])

    # 0-indexedでidx番目の要素をxに更新
    def _set(self, idx, x):
        idx += self.n
        self.tree[idx] = x
        idx >>= 1
        while idx > 0:
            self.tree[idx] = self.comp(self.tree[2 * idx], self.tree[2 * idx + 1])
            idx >>= 1

    def _add(self, idx, x):
        idx += self.n
        self.tree[idx] += x
        idx >>= 1
        while idx > 0:
            self.tree[idx] = self.comp(self.tree[2 * idx], self.tree[2 * idx + 1])
            idx >>= 1

    # 0-indexedで[l, r)の値を求める
    def _get(self, l, r):
        l += self.n
        r += self.n
        res = self.e
        while r > l:
            if l & 1:
                res = self.comp(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.comp(res, self.tree[r - 1])
                r -= 1
            l >>= 1
            r >>= 1
        return res

    def __repr__(self):
        return f"{[self._get(i, i + 1) for i in range(self.n)]}"
