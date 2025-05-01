# verify: https://onlinejudge.u-aizu.ac.jp/status/users/suo/submissions/1/GRL_1_A/judge/10436089/Python3


from heapq import heappush, heappop


class Dijkstra:
    def main(n, edges, s):
        time = [-1] * n
        h = [s]
        time[s] = 0
        while h:
            i = heappop(h)
            t = i // n
            i %= n
            if time[i] < t:
                continue
            for j, dt in edges[i]:
                if time[j] != -1 and time[j] <= t + dt:
                    continue
                time[j] = t + dt
                heappush(h, (t + dt) * n + j)

        return time
