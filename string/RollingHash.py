# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/ALDS1_14_B/judge/10436038/Python3


class RollingHash:
    def __init__(self, mod=(1 << 61) - 1, base=107):
        self.mod = mod
        self.base = base

    def hash(self, s):
        hash_s = 0
        for i in s:
            hash_s *= self.base
            hash_s += ord(i) - ord("a") + 1
            hash_s %= self.mod
        return hash_s

    def match(self, s, t):
        if len(t) > len(s):
            return []

        lt = len(t)
        hash_t = self.hash(t)
        hash_s = self.hash(s[:lt])
        res = [] if hash_t != hash_s else [0]

        minus = pow(self.base, lt - 1, self.mod)
        for i in range(lt, len(s)):
            hash_s -= minus * (ord(s[i - lt]) - ord("a") + 1)
            hash_s *= self.base
            hash_s += ord(s[i]) - ord("a") + 1
            hash_s %= self.mod
            if hash_s == hash_t:
                res.append(i - lt + 1)
        return res
