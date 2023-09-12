# 15652 N과 M (4) (실버 3)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split())
st = []

def dfs(v):
    if len(st) == M:
        print(' '.join(map(str, st)))
        return
    
    for i in range(v, N+1):
        st.append(i)
        dfs(i)
        st.pop()
dfs(1)