# 11724 연결 요소의 개수

# 1번 노드를 루트로 지정
# 2번 노드 ~ n번 노드까지 각 노드의 부모 노드를 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().strip())

graph = [ [] for _ in range(n+1) ]

for _ in range(n-1):
    s, e = map(int, input().strip().split())
    graph[s].append(e)
    graph[e].append(s)

# for i in graph:
#     i.sort()

visit = [0]*(n+1)
visit[1] = 1
v = 1

# for i in range(2, n+1):
#     print(graph[i][0])

def dfs(v):
    for nv in graph[v]:
        if visit[nv] == 0:
            visit[nv] = v
            dfs(nv)

dfs(v)
for i in range(2, len(visit)):
    print(visit[i])