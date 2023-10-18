# 10974 차이를 최대로 (실버 2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().strip())
a = list(map(int, input().strip().split()))

a.sort()

st = []
visit = [0 for _ in range(n)]
log = 0
def dfs(v):
    global log

    if len(st) == n:
        cnt = 0
        for i in range(1, n):
            cnt += abs(a[ st[i-1] ] - a[ st[i] ])
        if cnt > log:
            log = cnt
        return

    for j in range(n):
        if visit[j] == 0:
            visit[j] = 1
            st.append(j)
            dfs(j)
            visit[j] = 0
            st.pop()

    return
dfs(0)
print(log)
# 6
# 20 1 15 8 4 10