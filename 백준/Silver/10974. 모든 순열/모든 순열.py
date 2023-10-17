# 10974 모든 순열 (실버 3)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().strip())

st = []
visit = [0 for _ in range(N+1)]

def dfs(v):

    if len(st) == N:
        # print(' '.join(map(str, st)))
        print(*st)
        return
    
    for i in range(1, N+1):
        if visit[i] == 0:
            visit[i] = 1
            st.append(i)
            dfs(i)
            st.pop()
            visit[i] = 0
    return
dfs(0)