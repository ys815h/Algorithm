# 15664 N과 M (10) (실버 2)

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
    
    log = 0
    for i in range(v, N):
        if visit[i] == 0 and log != arr[i]:
            log = arr[i]
            visit[i] = 1
            st.append(arr[i])
            dfs(i)
            visit[i] = 0
            st.pop()
    return
dfs(0)
