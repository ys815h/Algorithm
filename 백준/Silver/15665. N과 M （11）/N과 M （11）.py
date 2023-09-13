# 15665 N과 M (11) (실버 2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()
# visit = [0]*N
st = []


def dfs(v):
    if len(st) == M:
        print(' '.join(map(str, st)))
        return
    
    log = 0
    for i in range(N):
        if arr[i] != log:
            log = arr[i]
            st.append(arr[i])
            dfs(i)
            st.pop()
    return
dfs(0)