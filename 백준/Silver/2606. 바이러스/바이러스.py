import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range (m):
    s, e = map(int, input().split())
    graph[e].append(s)
    graph[s].append(e)

for i in range(n+1):
    graph[i].sort()


visit = [0] * (n+1)
visit[1] = 1

cnt = 0

def dfs(v):

    global cnt
    cnt += 1


    for nv in graph[v]:
        if visit[nv] == 0:
            visit[nv] = 1
            dfs(nv)
dfs(1)
cnt -= 1

print(cnt)
