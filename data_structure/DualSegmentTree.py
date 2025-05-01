# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/DSL_2_D/judge/10435890/Python3


class DualSegmentTree:
    # n->要素数, l->リスト, e_upd->単位元(更新用), fun_upd->二項関数(更新用), e_acq->単位元(取得用), fun_acq->二項関数(取得用)
    def __init__(self, n, l, e_upd, fun_upd, e_acq, fun_acq):
        self.e_upd = e_upd
        self.fun_upd = fun_upd
        self.e_acq = e_acq
        self.fun_acq = fun_acq
        self.n = 1 << (n - 1).bit_length()
        self.tree = [self.e_upd] * self.n + l + [self.e_upd] * (self.n - len(l))

    # 0-indexedで[l, r)の要素をxに更新
    def _set(self, l, r, x):
        l += self.n
        r += self.n
        while r > l:
            if l & 1:
                self.tree[l] = self.fun_upd(x, self.tree[l])
                l += 1
            if r & 1:
                self.tree[r - 1] = self.fun_upd(x, self.tree[r - 1])
                r -= 1
            l >>= 1
            r >>= 1

    # 0-indexedで idx の値を求める
    def _get(self, idx):
        idx += self.n
        res = self.e_acq
        while idx > 0:
            res = self.fun_acq(res, self.tree[idx])
            idx >>= 1
        return res
