# 11724 연결 요소의 개수

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    graph[i].sort()

visit = [0]* (n+1)
cnt = 0

def dfs(v):
    for nv in graph[v]:
        if visit[nv] == 0:
            visit[nv] = 1
            dfs(nv)

for i in range(1, n+1):
    if visit[i] == 0:
        visit[i] = 1
        dfs(i)
        cnt += 1
print(cnt)