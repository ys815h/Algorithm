from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n+1):
    graph[i].sort()
    
def dfs(v):
    print(v, end = ' ')

    for nv in graph[v]:
        if visit[nv] == 0:
            visit[nv] = 1
            dfs(nv)


visit = [0] * (n+1)
visit[v] = 1
dfs(v)
print()

def bfs(v):
    q = deque()
    q.append(v)
    visit = [0] * (n+1)
    visit[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for nv in graph[v]:
            if visit[nv] == 0:
                visit[nv] = 1
                q.append(nv)
                
bfs(v)