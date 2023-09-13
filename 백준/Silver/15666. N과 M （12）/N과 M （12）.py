# 15666 N과 M (12) (실버 2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()

st = []

def dfs(v):

    if len(st) == M:
        print(' '.join(map(str, st)))
        return
    
    log = 0
    for i in range(v, N):
        if log != arr[i]:
            log = arr[i]
            st.append(arr[i])
            dfs(i)
            st.pop()
    return
dfs(0)