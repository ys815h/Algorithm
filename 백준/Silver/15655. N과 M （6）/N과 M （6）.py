# 15655 N과 M (6) (실버 3)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split())
arr = list(map(int, list(input().strip().split())))
visit = [0 for _ in range(N)]
arr.sort()
st = []

def dfs(v):
    if len(st) == M:
        print(' '.join(map(str, st)))
        return
    for i in range(v, N):
        if visit[i] == 0:
            visit[i] = 1
            st.append(arr[i])
            dfs(i)
            st.pop()
            visit[i] = 0
    return
dfs(0)