# 15663 N과 M (9) (실버 3)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split())

visit = [0] * N

arr = list(map(int, input().strip().split()))
arr.sort()
st = []
def dfs(v):

    if len(st) == M:
        print(' '.join(map(str, st)))
        return

    cnt = 0
    for i in range(N):
        if visit[i] == 0 and cnt != arr[i]:
            cnt = arr[i]
            visit[i] = 1
            st.append(arr[i])
            dfs(i)
            st.pop()
            visit[i] = 0
    return
dfs(0)

